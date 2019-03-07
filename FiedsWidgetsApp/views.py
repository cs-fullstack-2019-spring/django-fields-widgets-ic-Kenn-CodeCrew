from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm


# Create your views here.
def index(request):
    if(request.method=="POST"):
        form=ApplicationForm(request.POST)
        if form.is_valid():
            # form.date = request.POST["date_year"] + "-" + request.POST["date_month"] + "-" + request.POST["date_day"]
            # print(form.date)
            form.save()
            print(request.POST)
        else:
            print("ERROR!!!!!!!!!!")
    return render(request, "FiedsWidgetsApp/index.html", {"form": ApplicationForm()})
