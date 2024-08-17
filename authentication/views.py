from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home (request):
    context = {
        'title': 'Project | BOCS'
    }

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
        
    return render(request, 'authentication/index.html', context)

def login(request):
    return render(request, 'authentication/dashboard.html')

def signup(request):
    return render(request, 'authentication/signup.html')

def signout(request):
    # return render(request, 'authentication/signout.html')
    pass