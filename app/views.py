from django.shortcuts import render

def error_404(request, exception):
    return render(request,'app/404.html')

def error_500(request, exception):
    return render(request,'app/500.html')