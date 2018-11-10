from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Attendence
from .forms import addStudent
def index(request):
    d="5"
    yo=Attendence.objects.all()
    # return HttpResponse("hye fahala ")
    return render(request,'index.html',{'yo':yo})

def details(request,usn):
    yo=Attendence.objects.filter(usn=usn)
    return render(request,'attendenceDetails.html',{'yo':yo})
def addSttudent(request):
    if request.method == 'POST':
        form = addStudent(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = addStudent()
    return render(request,'addStudent.html',{'form':form})
