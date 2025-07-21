# prescriptions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm
from .models import Prescription
from appointments.models import Appointment
from prescriptions.models import Prescription


@login_required
def write_prescription_view(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.patient = form.cleaned_data['appointment'].patient
            prescription.save()
            return redirect('prescriptions:write_prescription')  # using namespace
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/write_prescription.html', {'form': form})


@login_required
def view_prescriptions(request):
    if request.user.is_doctor:
        prescriptions = Prescription.objects.all()
    else:
        prescriptions = Prescription.objects.filter(patient=request.user)
    return render(request, 'prescriptions/view_prescriptions.html', {'prescriptions': prescriptions})
