from django.urls.conf import include

from rest_framework import routers
from backend import views
from django.urls import path


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"customers", views.CustomerViewSet)
router.register(r"employees", views.EmployeeViewSet)
router.register(r"companytypes", views.CompanyTypeViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
