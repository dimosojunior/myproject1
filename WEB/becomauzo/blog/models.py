from django.db import models
from django.contrib.auth.models import User

class Customer(models .Model):
    user = models.OneToOneField(User, null=False,blank=False,on_delete=models.CASCADE)

    phone_field = models.CharField(max_length=200)

    def _str_(self):
        return self.user.username



class Category(models.Model):
    category_name = models.CharField(max_length=200,db_index=True)
    
    
    
    def _str_(self):
        return self.category_name

  

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_available_count =models.IntegerField(default=0)

    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='productImages')
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

