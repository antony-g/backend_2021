from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_index, name='api_index'),
    path('api/signin/', views.api_signin, name='api_signin'),
    path('api/all/', views.api_all_tasks, name='api_all_tasks'),
    path('api/new/', views.api_new_task, name='api_new_task'),
    path('api/update/', views.api_update_task, name='api_update_task'),
    path('api/delete/', views.api_delete_task, name='api_delete_task'),
]
