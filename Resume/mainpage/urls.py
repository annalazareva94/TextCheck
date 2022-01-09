from django.urls import path
from . import views


urlpatterns = [
    path ('', views.index, name='main page'),
    path ('resume', views.resume, name='resume'),
]