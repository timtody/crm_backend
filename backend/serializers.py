from django.contrib.auth.models import User, Group
from rest_framework import serializers

from backend.models import CompanyTypes, Customers, Employees


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class CompanyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyTypes
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # companytype = CompanyTypeSerializer()

    class Meta:
        model = Customers
        fields = "__all__"
        depth = 1
