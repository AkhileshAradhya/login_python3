from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Create your views here.
def home(request):     
    return render(request,"home.html")

def ulogin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass2 = request.POST['pass2']

        user = authenticate(username=username,password=pass2)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"index.html",{'fname':fname})
        else:
            messages.error(request,"Bad credentials!")
            return redirect('home')
    return render(request,"ulogin.html")

def signin(request):

    if request.method == "POST":
        #user = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.f_name = fname
        myuser.l_name = lname

        myuser.save()

        messages.success(request,"Your Account has been created!")

        return redirect('ulogin')
    
    return render(request,"signin.html")

def index(request):
    return render(request,"index.html")

def signout(request):
    pass