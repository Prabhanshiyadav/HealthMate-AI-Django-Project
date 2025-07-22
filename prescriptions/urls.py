from django.urls import path
from .views import write_prescription_view, view_prescriptions

app_name = 'prescriptions'

urlpatterns = [
    path('write/', write_prescription_view, name='write_prescription'),
    path('view/', view_prescriptions, name='view_prescriptions'),  # ✅ Clean and correct
]
