from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def loginUser(request):
    context={}
    if request.method =="POST":
        username=request.POST["username"]
        password=request.POST["username"]

        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request=user)
            return redirect('profilUser')
    return render(request,'users/login.html',context)


def registerUser(request):
    context={}
        
    
    return render(request,'users/login.html',context)
def AccountUser(request):
    context={}
        
    
    return render(request,'users/hesap.html',context)
def profilUser(request):
    context={}
        
    
    return render(request,'users/browse.html',context)