from django.shortcuts import render, redirect
from .forms import CSOEventForm
from .models import CSOEvent

def report_event(request):
    if request.method == "POST":
        form = CSOEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_success')
    else:
        form = CSOEventForm()

    return render(request, 'report_event.html', {'form': form})

def report_success(request):
    return render(request, 'report_success.html')

def dashboard(request):
    events = CSOEvent.objects.all()

    event_data = [
        {
            "location": event.location,
            "severity": event.severity,
            "volume": event.overflow_volume_m3,
            "start_time": event.start_time.strftime("%Y-%m-%d %H:%M"),
        }
        for event in events
    ]

    return render(request, 'dashboard.html', {"events": event_data})

