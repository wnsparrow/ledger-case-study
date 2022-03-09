from django.contrib import admin

from .models import AutoPolicy


@admin.register(AutoPolicy)
class AutoPolicyAdmin(admin.ModelAdmin):
    list_display = [
        "public_id",
    ]
