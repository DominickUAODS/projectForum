from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (None, {"fields":('birthDate',)}),)
    add_fieldsets=(
        *UserAdmin.add_fieldsets,
        (None,{"fields":('birthDate',)},)
    )

