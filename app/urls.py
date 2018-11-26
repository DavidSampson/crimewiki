from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

page_urlpatterns = [
    path('', views.PageIndex.as_view(), name='pages_index'),
    path('<int:pk>/', views.PageDetail.as_view(), name='page_detail'),
    path('types/<type>/', views.PageCreate.as_view(), name='page_create'),
]

user_urlpatterns = [
    path('<int:user_id>/', views.UserDetail.as_view(), name='user_detail'),
    path('login/', auth_views.LoginView.as_view(
        template_name="users/user_login.html", extra_context={'next':'/'}), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register')
]

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('pages/', include(page_urlpatterns)),
    path('users/', include(user_urlpatterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
