
from django.shortcuts import render, redirect
from .models import Contact, Project
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})