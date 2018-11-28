from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Role(models.Model):
    name = models.CharField()


class Action(models.Model):
    name = models.CharField()


class RoleCollection(models.Model):
    name = models.CharField()
    verbose_name = models.CharField()
    roles = models.ManyToManyField(Role)


class PermissionStrategy(models.Model):
    role_collection = models.ForeignKey(
        RoleCollection, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)


class RoleBroker(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    roles = models.ManyToManyField(Role, blank=True)
    actions = models.ManyToManyField(Action, blank=True)
    permission_strategies = models.ManyToManyField(
        PermissionStrategy, blank=True)

    def create_group(self, role):
        return Group.objects.create(name=self._get_name(role))

    def create_permission(self, action):
        name = self._get_name(action)
        return Permission.objects.create(name=name, codename=name, content_type=self.content_type)

    def _get_name(self, v):
        return f'{self.content_type}_{self.object_id}_{v}'

    def get_group(self, role):
        return Group.objects.filter(name=self._get_name(role))

    def get_permission(self, action):
        return Permission.objects.filter(name=self._get_name(action))

    def apply_permission_strategy(self, s):
        for role in self.roles:
            if role in s.role_collection:
                self.get_group(role).permissions.add(
                    self.get_permission(s.action))
            else:
                self.get_group(role).permissions.remove(
                    self.get_permission(s.action))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.roles = Role.objects.all()
            self.actions = Action.objects.all()
            for role in self.roles:
                self.create_group(role)
            for action in self.actions:
                self.create_permission(action)
        for s in self.permission_strategies:
            self.apply_permission_strategy(s)
        return super().save(*args, **kwargs)


class PermissionedModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            RoleBroker.objects.create(content_object=self)
        return super().save(*args, **kwargs)
