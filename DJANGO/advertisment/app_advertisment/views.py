from django.shortcuts import render
from .models import Advertisement


def index(request):
    advertsement = Advertisement.objects.all()
    context = {'advertisement' : advertsement}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
