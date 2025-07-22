# prescriptions/urls.py
from django.urls import path
from .views import write_prescription_view, view_prescription_view

app_name = 'prescriptions'  # Add this to enable namespace usage

urlpatterns = [
    path('write/', write_prescription_view, name='write_prescription'),
    path('view/', view_prescription_view, name='view_prescription'),
]
