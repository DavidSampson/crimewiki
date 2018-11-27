from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views


user_urlpatterns = [
    path('<int:user_id>/', views.UserDetail.as_view(), name='user_detail'),
    path('login/', auth_views.LoginView.as_view(
        template_name="user_login.html", extra_context={'next':'/'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register')
]

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('users/', include(user_urlpatterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
