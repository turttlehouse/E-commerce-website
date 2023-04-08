from django.shortcuts import render,redirect,HttpResponse
from .models import Product,Category
from .forms import addform,createuserform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
#from django.views.decorators.cache import cache_control


# Create your views here.
#cache_control(no_cache=True)
@login_required(login_url='/')
def home(request):
    model=Product.objects.all().filter(Pis_featured=True)
    modela=Product.objects.all()
    return render(request,'index.html',{'cloth':model,'products':modela})


@login_required(login_url='/')
def aboutproduct(request,id):
    img=Product.objects.get(id=id)
    return render(request,'aboutproduct.html',{'details':img})


@login_required(login_url='/')
def mensproduct(request):
    mp=Product.objects.all().filter(PCategory=1)
    return render(request,'mensproduct.html',{'men':mp})


@login_required(login_url='/')
def womenproduct(request):
    wp=Product.objects.all().filter(PCategory=2)
    return render(request,'womenproduct.html',{'women':wp})


def Createuser(request):
    model=addform()
    if request.method=="POST":
        form=addform(request.POST,request.FILES)
        form.save()
        return redirect("/")
    return render(request,'Sellsignup.html',{'model':model})

   
def signupclients(request):
    form=createuserform(request.POST)
    if form.is_valid():
        form.save()
        user=form.cleaned_data.get('username')
        messages.success(request,'Account was created for'+user)
        return redirect('/home')
    
    return render(request,'clientsignup.html',{'form':form})

def loginuser(request):
        if request.method=='POST':
            username = request.POST['name']
            password = request.POST['pp']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect ('/home')
            else:
                messages.info(request,"invalid username or password")
            
        return render(request,'login.html')

def logoutclients(request):
    logout(request)
    return redirect ('/')

def searchproduct(request):
    if request.method=="GET":
        y=request.GET.get('search')
        modela=Product.objects.all().filter(Q(Pname=y))
        return render (request,'index.html',{'products':modela})

        