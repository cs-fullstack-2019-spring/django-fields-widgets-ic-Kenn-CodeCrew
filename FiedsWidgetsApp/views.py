from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm


# Create your views here.
def index(request):
    return render(request, "FiedsWidgetsApp/index.html", {"form": ApplicationForm()})
