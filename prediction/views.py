from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'prediction/home.html')

def show_significant_features(request):
    return render(request, 'prediction/significant_features.html')