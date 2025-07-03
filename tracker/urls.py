from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_metric, name='add_metric'),
    path('metrics/', views.view_metrics, name='view_metrics'),
]
