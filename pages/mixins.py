from django.core.exceptions import PermissionDenied

class LoginRequiredForEditMixin:
    def post(self, request, *args, **kwargs):
        if self.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            raise PermissionDenied
