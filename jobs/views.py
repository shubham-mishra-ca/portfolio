from django.shortcuts import render

# Create your views here.

def home(request):
    # render is is used to return HTML
    return render(request, 'jobs/home.html')