from rest_framework import generics
from appointments.models import Appointment
from api.serializers.appointment_serializer import AppointmentSerializer

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
