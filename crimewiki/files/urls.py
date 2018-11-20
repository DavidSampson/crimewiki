from django.urls import path

from . import views

app_name = 'files'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:file_id>/', views.detail, name='detail'),
    path('<int:file_id>/<str:file_name>', views.file_serve, name='file_serve')
]
