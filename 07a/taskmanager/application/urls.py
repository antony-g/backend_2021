from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', views.api_index, name='api_index'),
    path('api/signin/', views.api_signin, name='api_signin'),
    path('api/all/', views.api_all_tasks, name='api_all_tasks'),
    path('api/select/', views.api_select_task, name='api_select_task'),
    path('api/create/', views.api_create_task, name='api_create_task'),
    path('api/update/', views.api_update_task, name='api_update_task'),
    path('api/delete/', views.api_delete_task, name='api_delete_task'),
]
