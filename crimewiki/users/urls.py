from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html", extra_context={'next':'/'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]
