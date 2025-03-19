from django.shortcuts import render
from .models import RecruiterContact
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact, RecruiterContact
# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def software_development(request):
    return render(request,'software_development.html')

def recruitment(request):
    return render(request,'recruitment.html')


def recruiters(request):
    return render(request,'home.html')


def contactpage(request):
    return render(request,'contact.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name, phone_number, email, subject, message)
        # Save data to the database

        if name and email and phone_number and subject and message:
            contact = Contact(
                name=name,
                phone_number=phone_number,
                email=email,
                subject=subject,
                message=message
            )
            contact.save()
            print("Data saved successfully!")
            # Send SMS notification
            
        
        # Check if it's an AJAX request
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": "Your message has been sent successfully!"})

        # If not an AJAX request, redirect to home (for normal form submission)
        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")  

    return render(request, "home.html")

def software_development(request):
    return render(request,'software-development.html')


def recruitment(request):
    return render(request,'recruitment.html')

def recruiters(request):
    return render(request,'home.html')






def Recruitercontact(request):
    return render(request,'Recruitercontact.html')


def RecruitersServices(request):
    return render(request,'Recruiterservices.html')

def Recruiterabout(request):
    return render(request,'Recruiterabout.html')


def recruitercontact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name, phone_number, email, subject, message)
        # Save data to the database

        if name and email and phone_number and subject and message:
            contact = RecruiterContact(
                name=name,
                phone_number=phone_number,
                email=email,
                subject=subject,
                message=message
            )
            contact.save()
            print("Data saved successfully!")
            # Send SMS notification
            
        
        # Check if it's an AJAX request
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": "Your message has been sent successfully!"})

        # If not an AJAX request, redirect to home (for normal form submission)
        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")  

    return render(request, "home.html")



