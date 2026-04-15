from django.urls import path
from . import views

urlpatterns = [
    path('programmes/create/', views.ProgrammeCreate.as_view(), name='programme_create'),
    path('programmes/update/<pk>/', views.ProgrammeUpdate.as_view(), name='programme_update'),
    path('programmes/delete/<pk>/', views.ProgrammeDelete.as_view(), name='programme_delete'),
    path('programmes/<int:programme_id>/', views.programme_detail, name='programme_detail'),
    path('programmes/', views.programme_list, name='programme_list'),
    path('', views.index, name='index'),
]