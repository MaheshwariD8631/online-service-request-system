from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'department', 'service_type', 'description', 'priority']

def home(request):
    return render(request, 'home.html', {
        'total': ServiceRequest.objects.count(),
        'open': ServiceRequest.objects.filter(status='Open').count(),
        'resolved': ServiceRequest.objects.filter(status='Resolved').count(),
    })

def add_request(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = ServiceForm()
    return render(request, 'add_request.html', {'form': form})

def request_list(request):
    data = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'request_list.html', {'requests': data})

def request_detail(request, pk):
    req = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'request_detail.html', {'req': req})

