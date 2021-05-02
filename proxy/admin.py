from django.contrib import admin

from proxy.models import KeepIt


@admin.register(KeepIt)
class KeepItAdmin(admin.ModelAdmin):
    pass
