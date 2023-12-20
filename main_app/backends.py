from django.contrib.auth.backends import ModelBackend


# class AdminUserBackend(ModelBackend):
#     def user_can_authenticate(self, user):
#         if getattr(user, 'is_admin_site_login', False):
#             # If user is trying to login to admin site and is a photographer, deny authentication


#         # Check if the user belongs to the photographer group
#         # change later
#         # from django.db.models import Q
#         # if user.groups.filter(Q(name='Photographer') | Q(name='Client')).exists():
          
#         if user.groups.filter(name='Photographer').exists():
#             # Prevent login through the admin site
#             return False
#         return super().user_can_authenticate(user)


class AdminUserBackend(ModelBackend):
    def user_can_authenticate(self, user):
        # Only allow staff members to log in through the admin site
        if not user.is_staff:
            return False

        # Allow all other users to log in normally
        return super().user_can_authenticate(user)
