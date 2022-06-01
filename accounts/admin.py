from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(BaseUserAdmin):
   
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {
            "fields": ("first_name", "last_name", 'national_id', "email", 'phone_number')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined",'birth_date')}),
    )
admin.site.register(User, UserAdmin)
