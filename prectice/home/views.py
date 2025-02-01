from django.shortcuts import render , HttpResponse

# Create your views here.

def Index(request):
    return HttpResponse("Hello World ")

def Contact1(request, id):
    return HttpResponse(id )

def Contact2(request, id):
    return HttpResponse(id )
def Contact3(request, id):
    return HttpResponse(id )

def Contact4(request, course):
    return HttpResponse(course)
    
