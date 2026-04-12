from django.urls import path
from . import views

urlpatterns = [
    path('programmes/', views.programme_list, name='programme_list'),
    path('', views.index, name='index'),
]