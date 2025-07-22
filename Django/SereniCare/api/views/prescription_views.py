from rest_framework import generics
from prescriptions.models import Prescription
from api.serializers.prescription_serializer import PrescriptionSerializer

class PrescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
