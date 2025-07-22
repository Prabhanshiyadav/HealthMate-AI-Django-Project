from django.urls import path
from api.views.user_views import UserListAPIView
from api.views.appointment_views import AppointmentListCreateAPIView
from api.views.prescription_views import PrescriptionListCreateAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='api-users'),
    path('appointments/', AppointmentListCreateAPIView.as_view(), name='api-appointments'),
    path('prescriptions/', PrescriptionListCreateAPIView.as_view(), name='api-prescriptions'),
]
