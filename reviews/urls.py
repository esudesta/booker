from django.urls import path
from .views import home

app_name="reviews"

urlpatterns = [
    path("",home,name="home"),
]
