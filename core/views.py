from django.shortcuts import render, redirect
from prescriptions.models import Prescription
from .forms import ContactForm

def view_prescriptions(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'core/view_prescriptions.html', {'prescriptions': prescriptions})

def home_view(request):
    return render(request, 'core/home.html')

def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
