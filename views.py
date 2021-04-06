from django.shortcuts import render,redirect
from Page.models import Contact
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method== "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")

        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()


    return render(request, 'index.html')