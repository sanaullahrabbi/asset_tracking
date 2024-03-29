from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (works at {self.company.name})"


class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="logs")
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="device_logs"
    )
    check_out_time = models.DateTimeField(default=timezone.now)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_condition = models.CharField(max_length=100)
    check_in_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.device.name} - {self.employee.name}"
