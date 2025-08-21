from django.shortcuts import render ,HttpResponse

def index(request):
    return render(request, 'index.html1')


def library_availibility(request):
    
    return render(request,"lib.html")
def book_issue(request):
    
    return render(request,"issued.html")
def solved_p(request):
    
    return render(request,"pyqs.html")
def lib_e(request):
    
    return render(request,"lib_enrollment.html")
