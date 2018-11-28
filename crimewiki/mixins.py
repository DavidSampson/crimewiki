from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


class PermissionedObjectMixin:
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    owner_group = models.OneToOneField(
        Group, on_delete=models.CASCADE, blank=True)
    editor_group = models.OneToOneField(
        Group, on_delete=models.CASCADE, blank=True)
    change_permission = models.OneToOneField(
        Permission, on_delete=models.CASCADE, blank=True)
    delete_permission = models.OneToOneField(
        Permission, on_delete=models.CASCADE, blank=True)
    PERMISSION_CHOICES = (
        ('me', 'Only the owner'),
        ('owners', 'Only the owner and co-owners'),
        ('editors', 'The owner, co-owners, and editors'),
        ('users', 'Any logged in users')
    )
    change_permission_choice = models.CharField(
        choices=PERMISSION_CHOICES, default='users')
    delete_permission_choice = models.CharField(
        choices=PERMISSION_CHOICES, default='owners')

    def get_excluded_fields(self):
        return ['owner', 'owner_group', 'editor_group', 'change_permission', 'delete_permission']

    def get_model_name(self):
        return type(self).__name__

    def _name_str(self, role):
        return '_'.join([self.get_model_name(), self.pk, role])

    def create_group(self, role):
        return Group.objects.create(name=self._name_str(role))

    def get_content_type(self):
        return ContentType.objects.get_for_model(self)

    def create_permission(self, role):
        return Permission.objects.create(name=self._name_str(role), codename=self._name_str(role), content_type=self.get_content_type())

    def setup_groups_permissions(self):
        if not self.owner_group:
            self.owner_group = self.create_group('owner')
        if not self.editor_group:
            self.editor_group = self.create_group('editor')
        if not self.change_permission:
            self.change_permission = self.create_permission('change')
        if not self.delete_permission:
            self.delete_permission = self.create_permission('delete')

    def _set_permissions(self, perm, choice):
        admin_group = Group.objects.select(name='Admins')
        user_group = Group.objects.select(name='RegularUsers')

        if choice == 'me':
            self.owner.user_permissions.add(perm)
            self.owner_group.permissions.remove(perm)
            self.editor_group.permissions.remove(perm)
            user_group.permissions.remove(perm)
        elif choice == 'owners':
            self.owner.user_permissions.add(perm)
            self.owner_group.permissions.add(perm)
            self.editor_group.permissions.remove(perm)
            user_group.permissions.remove(perm)
        elif choice == 'editors':
            self.owner.user_permissions.add(perm)
            self.owner_group.permissions.add(perm)
            self.editor_group.permissions.add(perm)
            user_group.permissions.remove(perm)
        elif choice == 'users':
            self.owner.user_permissions.add(perm)
            self.owner_group.permissions.add(perm)
            self.editor_group.permissions.add(perm)
            user_group.permissions.add(perm)
        admin_group.permissions.add(perm)

    def set_permissions(self):
        perms = (
            (self.delete_permission, self.delete_permission_choice),
            (self.change_permission, self.change_permission_choice)
        )
        for (perm, choice) in perms:
            self._set_permissions(perm, choice)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        self.setup_groups_permissions()
        self.set_permissions()
        super().save(*args, **kwargs)
