from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if name == '':
            messages.info(request, 'Please fill all your details ')
            return redirect('/')
        else:
            new_contact = Contact(name=name, email=email,
                                  phone=phone, message=message)
            new_contact.save()

    return render(request, 'index.html')
