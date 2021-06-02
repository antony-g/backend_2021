from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('login/', views.login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('social-auth/', include('social_django.urls', namespace='social')),
	path('', views.login_home, name='home'),

	path('api/all/', views.api_all_tasks, name='api_all_tasks'),
	path('api/new/', views.api_new_task, name='api_new_task'),
	path('api/update/', views.api_update_task, name='api_update_task'),
	path('api/delete/', views.api_delete_task, name='api_delete_task'),
]
