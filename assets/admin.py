from django.contrib import admin
from .models import Company, Employee, Device, DeviceLog


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Display additional fields if needed


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "phone",
        "designation",
    )
    search_fields = ["name", "company__name", "phone"]
    list_filter = ("company",)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ("device", "employee", "check_out_time", "check_in_time")
    list_filter = ("device", "check_out_time", "check_in_time")
    search_fields = ("device__name", "employee__name")
