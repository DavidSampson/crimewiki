import re

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.urls import resolve

from pages.utilities import seqify


class MethodPermissionRequiredMixin(UserPassesTestMixin):
    def validate_perm(self, perm):
        perm_re = r'^[\w_][\w\d_]*.[\w_][\w\d_]*$'
        if isinstance(perm, Permission):
            return str(perm)
        elif re.match(perm_re, perm):
            return perm
        else:
            app = resolve(self.request.path).app_name
            return f'{app}.{perm}'

    def test_func(self):
        for verb, p in self.required_permissions.items():
            perms = [self.validate_perm(perm) for perm in seqify(p)]
            if self.request.method == verb.upper():
                return self.user.has_perms(perms)
        return True
