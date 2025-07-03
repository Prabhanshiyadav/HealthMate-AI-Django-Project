from .models import HealthEntry
from .forms import HealthEntryForm
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        form = HealthEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HealthEntryForm()

    entries = HealthEntry.objects.all().order_by('-date')
    return render(request, 'tracker/home.html', {'form': form, 'entries': entries})

def add_metric(request):
    return render(request, 'tracker/add_metric.html')

def view_metrics(request):
    return render(request, 'tracker/metrics.html')
