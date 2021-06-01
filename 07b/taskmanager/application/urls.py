from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register(r"api", views.NewTaskViewSet, basename='api_all')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signin/', views.api_signin, name='api_signin'),
]

urlpatterns += router.urls
