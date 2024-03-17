from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# Register your models here.
admin.site.register([
    models.SocialMedia,
    ])

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    # fieldsets = BaseUserAdmin.fieldsets + (
    #     (None, {'fields': ['updated_at']}),
    # )
    pass