from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from main import views

router = DefaultRouter()
router.register(r"api", views.ObjectViewSet, basename='api_all')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls