from django.contrib.auth.mixins import PermissionRequiredMixin


class ChangePermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        perms = self.get_permission_required()
        if self.request.user != self.get_object().author.userAuthor:
            return False
        return self.request.user.has_perms(perms)

    # def has_permission(self):
    #     if self.request.user != self.get_object().author.userAuthor:
    #         return False
    #     return True
