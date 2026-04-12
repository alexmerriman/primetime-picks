from django.shortcuts import render
from .models import Programme

def index(request):
    return render(request, 'base.html')

def programme_list(request):
    programmes = Programme.objects.all()
    context = {
        'programmes': programmes
    }
    return render(request, 'pages/programme_list.html', context)