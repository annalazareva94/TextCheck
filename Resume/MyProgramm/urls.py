from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprogramm, name='myprogramm'),
    path('wordslist/',views.WordsList, name='wordslist'),
    path('wordslist/result', views.Result, name='result')
]