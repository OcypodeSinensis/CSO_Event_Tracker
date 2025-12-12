from django.shortcuts import render, redirect
from .forms import CSOEventForm

def report_event(request):
    if request.method == "POST":
        form = CSOEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_success')  # redirect after submitting
    else:
        form = CSOEventForm()

    return render(request, 'report_event.html', {'form': form})


def report_success(request):
    return render(request, 'report_success.html')

