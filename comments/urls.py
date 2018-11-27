from django.urls import  path
from comments.views import Serve

app_name = "comments"
urlpatterns = [
    path('pages/<int:pk>/', Serve.as_view(), name="serve"),
]
