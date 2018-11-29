from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
# Create your models here.


GROUP_ROLES = (
    ('owners', 'The owners can'),
    ('editors', 'The editors can'),
)

ORDINARY_ROLE_GROUPS = (
    ('admins', 'The admins can', 'Admins'),
    ('users', 'Any logged in users can', 'RegularUsers'),
    ('visitors', 'Any visitors to the website can', 'Anonymous'),
)
ORDINARY_ROLES = tuple([(r, s) for (r, s, g) in ORDINARY_ROLE_GROUPS])

ROLES = GROUP_ROLES + ORDINARY_ROLES

ACTIONS = (
    ('create', 'create a new object'),
    ('edit', 'edit the object'),
    ('view', 'view the object'),
    ('delete', 'delete the object'),
)

PERMISSION_STRATEGIES = [
    {'role': r, 'action': a, 'description': ' '.join([R, A])}
    for (r, R) in ROLES
    for (a, A) in ACTIONS
]


class PermissionController(models.Model):
    role = models.CharField(max_length=200, choices=ROLES)
    action = models.CharField(max_length=200, choices=ACTIONS)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class PermissionStrategy(models.Model):
    description = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class PermissionedModel(models.Model):
    class Meta:
        abstract = True

    granted_permissions = models.ManyToManyField(
        PermissionStrategy, limit_choices_to=~Q(role='admins'))
    permission_controllers = models.ManyToManyField(PermissionController)

    def get_content_type(self):
        return ContentType.objects.get_for_model(self)

    def get_ordinary_groups(self):
        return [(r, Group.objects.get(name=g)) for (r, s, g) in ORDINARY_ROLE_GROUPS]

    def create_group(self, role):
        return Group.objects.create(name=self._get_name(role))

    def create_permission(self, action):
        name = self._get_name(action)
        return Permission.objects.create(
            name=name, codename=name, content_type=self.get_content_type())

    def _get_name(self, v):
        return f'{self.get_content_type()}_{self.pk}_{v}'

    def setup_permission_controllers(self):
        group_roles = [role for (role, _) in GROUP_ROLES]
        actions = [action for (action, _) in ACTIONS]
        perms = []
        groups = []
        for action in actions:
            perms.append((action, self.create_permission(action)))
        for role in group_roles:
            groups.append((role, self.create_group(role)))
        all_roles = groups + self.get_ordinary_groups()
        for (role, group) in all_roles:
            for (action, perm) in perms:
                self.permission_controllers.add(PermissionController.objects.create(
                    role=role, permissioned_object=group, action=action, permission=perm))

    def allow_admins(self):
        pcs = self.permission_controllers.filter(role='admins')
        for pc in pcs:
            pc.group.permissions.add(pc.permission)

    def apply_permission_strategy(self):
        perms = PermissionStrategy.objects.exclude(role='admins')
        denied_permissions = perms.difference(self.granted_permissions)
        for ps in self.granted_permissions:
            pc = self.permission_controllers.get(
                role=ps.role, action=ps.action)
            pc.group.permissions.add(pc.permission)
        for ps in denied_permissions:
            pc = self.permission_controllers.get(
                role=ps.role, action=ps.action)
            pc.group.permissions.remove(pc.permission)
        self.allow_admins()

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.setup_permission_controllers()
        self.apply_permission_strategy()
        return super().save(*args, **kwargs)
