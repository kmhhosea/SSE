from django.urls import path
from . import views


app_name = 'scholars'


urlpatterns = [
path('', views.index, name='index'), # SPA shell


# Auth
path('api/register/', views.api_register, name='api_register'),
path('api/login/', views.api_login, name='api_login'),
path('api/logout/', views.api_logout, name='api_logout'),


# Profiles
path('api/profile/', views.api_get_my_profile, name='api_get_my_profile'),
path('api/profile/update/', views.api_update_profile, name='api_update_profile'),
path('api/members/', views.api_members, name='api_members'),


# Posts and comments
path('api/posts/', views.api_posts, name='api_posts'),
path('api/posts/create/', views.api_create_post, name='api_create_post'),
path('api/posts/<int:post_id>/', views.api_post_detail, name='api_post_detail'),
path('api/posts/<int:post_id>/comment/', views.api_create_comment, name='api_create_comment'),


# Resources
path('api/resources/', views.api_resources, name='api_resources'),
path('api/resources/upload/', views.api_upload_resource, name='api_upload_resource'),


# Notifications
path('api/notifications/', views.api_notifications, name='api_notifications'),
]