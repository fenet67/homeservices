from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
     
     return render(request, 'index.html')
    
def services(request):

    return render(request, 'services.html')
def signup (request):

    return render(request, 'signup.html')
def signin (request):

    return render(request, 'signin.html')