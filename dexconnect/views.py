from django.http import HttpResponse
from django.shortcuts import render
from home.models import Signup,Contribute
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'categories.html')

def contribute(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        link = request.POST.get('link')
        desc = request.POST.get('desc')
        contribute = Contribute(name=name, email=email, phone=phone, link=link, desc=desc)
        contribute.save()
        messages.success(request, 'Thank you for the Contribution!')
    return render(request, 'contribute.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        signup = Signup(name=name, email=email, phone=phone)
        signup.save()
        messages.success(request, 'Your SignUp is successful!')
    return render(request, 'signup.html')