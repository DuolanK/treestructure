from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['role', 'first_name', 'last_name', 'manager']


admin.site.register(Employee, EmployeeAdmin)



