from django.shortcuts import render ,HttpResponse
from datetime import datetime 
from .models import enrollmentdetail 

def index(request):
    return render(request, 'index.html')


def library_availibility(request):
    
    return render(request,"lib.html")
def book_issue(request):
    
    return render(request,"issued.html")
def solved_p(request):
    
    return render(request,"pyqs.html")
def save_lib_e(request):
    if request.method=="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        password =request.POST.get('password')
        Details=enrollmentdetail(name=name,email=email,password=password,date=datetime.today())
        Details.save()


    
    return render(request,"lib_enrollment.html")
