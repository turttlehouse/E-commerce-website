from django.shortcuts import render,redirect,HttpResponse
from .models import Product

# Create your views here.
def home(request):
    model=Product.objects.all().filter(Pis_featured=True)
    modela=Product.objects.all()
    return render(request,'index.html',{'cloth':model,'products':modela})

def aboutproduct(request,id):
    img=Product.objects.get(id=id)
    return render(request,'aboutproduct.html',{'details':img})
