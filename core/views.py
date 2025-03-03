from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def homepage(request):
    context = {
        "current_tab":"home"
    }
    return render(request, 'homepage.html', context)

def about_us(request):
    context = {
        "current_tab":"about_us"
    }
    return render(request, 'about_us_2.html', context)

def contact_us(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")   
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
       
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')
    
    context = {
        "current_tab":"contact_us"
    }
    return render(request, 'contact_us.html', context)

def services(request):
    context = {
        "current_tab":"services"
    }
    return render(request, 'services.html', context)


def pricing(request):
    context = {
        "current_tab":"pricing"
    }
    return render(request, 'pricing.html', context)