from django.contrib import admin

from proxy.models import KeepIt


@admin.register(KeepIt)
class KeepItAdmin(admin.ModelAdmin):
    search_fields = ['url']
    list_filter = ['status_code']
