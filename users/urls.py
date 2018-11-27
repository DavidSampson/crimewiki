from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views
app_name = 'users'
urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('login/', auth_views.LoginView.as_view(
        template_name="user_login.html", extra_context={'next':'/'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register')
]
