from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
