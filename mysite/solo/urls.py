from django.urls import path

from . import views

app_name = 'solo'
urlpatterns = [
    path('', views.myview),
]