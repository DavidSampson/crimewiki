from django.urls import path, re_path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_id>/', views.detail, name='detail'),
    path('types/<type>/', views.create, name='create')
]
