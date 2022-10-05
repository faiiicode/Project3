from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')



def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first name']
        secondname = request.POST['last name']
        email = request.POST['email']
        passw1 = request.POST['psw']
        passw2 = request.POST['psw-repeat']

        if passw1 == passw2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Already exist user name")
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
              messages.info(request, "Already exist email")
              return redirect('registration')

            else:
             user =User.objects.create_user(username=username, password=passw1, email=email, first_name=firstname,
                                        last_name=secondname)

             user.save();
             return redirect('login')


        else:
            messages.info(request,"paasswrd no mtch")
            return redirect('registration')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
