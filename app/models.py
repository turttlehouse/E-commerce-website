from django.db import models

# Create your models here.
from django.db import models 

class Category(models.Model): 
    name = models.CharField(max_length=50) 

    def __str__(self): 
        return self.name
    
class Product(models.Model): 
    Pname = models.CharField(max_length=50) 
    PCategory=models.ForeignKey(Category,on_delete=models.CASCADE)
    Pprice=models.FloatField()
    Pdescription=models.CharField(max_length=50)
    Pbrand=models.CharField(max_length=20)
    Pis_featured=models.BooleanField()
    Pimage=models.ImageField(null=True)
    def __str__(self): 
        return self.Pname