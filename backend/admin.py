from django.contrib import admin

# Register your models here.
from backend.models import Customers, Employees, Orders


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("companyname", "companytype", "street", "house", "city")
    search_fields = ["companyname", "companytype__companytype", "street", "house", "city"]


@admin.register(Employees)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "codename")
    search_fields = ("firstname", "lastname", "codename")


@admin.register(Orders)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("orderid", "customer")
    list_display = ("orderid", "customer")
