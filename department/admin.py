from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Department


class DepartmentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    fields = ('name', 'short_name', 'slug_name', 'parent',)
    # list_editable = ('is_active',)
    prepopulated_fields = {"slug_name": ("short_name",)}
    # Specify name of sortable property
    # sortable = 'order'

admin.site.register(Department, DepartmentAdmin)
