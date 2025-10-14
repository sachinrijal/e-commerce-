from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username","first_name","last_name",'date_joined', 'last_login', "is_active"]
    list_display_links = ["email","first_name","last_name",]
    ordering = ["-date_joined"]
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {"fields": ("email", "password","first_name",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", )}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email","first_name","last_name",)
    filter_horizontal=()
    list_filter=()


admin.site.register(User,CustomUserAdmin)
