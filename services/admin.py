from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'priority', 'status', 'created_at')
    list_filter = ('priority', 'status', 'department')
    search_fields = ('name', 'email', 'service_type')
