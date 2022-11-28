from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect


class ProfileUserPermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        perms = self.get_permission_required()
        if self.get_object() != self.request.user:
            return False
        return self.request.user.has_perms(perms)

    def handle_no_permission(self):
        pk = self.request.user.id
        return redirect(f'/accounts/{pk}/profile/user')
