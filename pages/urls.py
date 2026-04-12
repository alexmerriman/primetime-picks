from django.urls import path
from . import views

urlpatterns = [
    path('programmes/<int:programme_id>/', views.programme_detail, name='programme_detail'),
    path('programmes/', views.programme_list, name='programme_list'),
    path('', views.index, name='index'),
]