from django.urls import include, path
from pages import views

app_name = 'pages'
urlpatterns = [
    path('', views.PageIndex.as_view(), name='pages_index'),
    path('<int:pk>/', views.PageDetail.as_view(), name='page_detail'),
    path('types/<type>/', views.PageCreate.as_view(), name='page_create'),
]
