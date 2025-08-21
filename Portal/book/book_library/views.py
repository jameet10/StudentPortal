from django.shortcuts import render ,HttpResponse

def index(request):
    
    return render(request, 'index.html1')

def library_availibility(request):
    
    return render(request,"lib.html")
def book_issue(request):
    
    return HttpResponse("This page is to set to show issued books ")
def solved_p(request):
    
    return HttpResponse("This page for the pyqs")