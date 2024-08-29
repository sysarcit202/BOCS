from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login

# Create your views here.
def home (request):
    context = {
        'title': 'Project_BOCS'
    }

    return render(request, 'authentication/index.html', context)

def signup(request):
    context = {
        'title': 'Project_BOCS | Signup'
    }

    if request.method == 'POST':
        username = request.POST['Uname']
        email = request.POST['Uemail']
        pass1 = request.POST['Upass']
        pass2 = request.POST['Urpass']
        
        user = User.objects.create_user(username, email, pass1)
        user.fname = 'Ufname'
        user.lname = 'Ulname'

        user.save()
            
        messages.success(request, 'Your account has been successfully created.')

        return redirect('')

        # user = authenticate(username=username, password=pass1)
        
        # if user is not None:
        #     login(request, user)
        #     fname = user.first_name
        #     # messages.success(request, "Logged In Sucessfully!!")
        #     return render(request, "authentication/index.html",{"fname":fname})
        # else:
        #     messages.error(request, "Bad Credentials!!")
        #     return redirect('home')
    
    return render(request, 'authentication/signup.html', context)

def dashboard(request):
    context = {
        'title': 'Project_BOCS | Dashboard'
    }

    return render(request, 'authentication/dashboard.html', context)

def signout(request):
    # return render(request, 'authentication/signout.html')
    pass

