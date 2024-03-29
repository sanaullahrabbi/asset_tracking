from django.test import TestCase
from .models import Company, Employee, Device, DeviceLog
from django.utils import timezone


class CompanyModelTestCase(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(name="Test Company")
        self.assertEqual(company.name, "Test Company")


class EmployeeModelTestCase(TestCase):
    def test_employee_creation(self):
        company = Company.objects.create(name="Test Company")
        employee = Employee.objects.create(
            company=company, name="John Doe", phone="1234567890", designation="Manager"
        )
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.company, company)


class DeviceModelTestCase(TestCase):
    def test_device_creation(self):
        device = Device.objects.create(
            name="Test Device", description="Test description", serial_number="12345"
        )
        self.assertEqual(device.name, "Test Device")
        self.assertEqual(device.description, "Test description")
        self.assertEqual(device.serial_number, "12345")


class DeviceLogModelTestCase(TestCase):
    def test_devicelog_creation(self):
        company = Company.objects.create(name="Test Company")
        employee = Employee.objects.create(
            company=company, name="John Doe", phone="1234567890", designation="Manager"
        )
        device = Device.objects.create(
            name="Test Device", description="Test description", serial_number="12345"
        )
        devicelog = DeviceLog.objects.create(
            device=device, employee=employee, check_out_condition="Good"
        )
        self.assertEqual(devicelog.device, device)
        self.assertEqual(devicelog.employee, employee)
        self.assertEqual(devicelog.check_out_condition, "Good")
