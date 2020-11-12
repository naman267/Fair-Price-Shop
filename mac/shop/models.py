from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=50)
    desc=models.CharField(max_length=3000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msgid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300)


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=111,default='')
    email=models.CharField(max_length=111,default='')
    phone=models.CharField(max_length=111,default='')
    address=models.CharField(max_length=111,default='')
    city=models.CharField(max_length=111,default='')
    state=models.CharField(max_length=111,default='')
    zip_code=models.CharField(max_length=111,default='')

    def __str(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=111,default='')
    cart_json=models.CharField(max_length=5000,default='{}')
    recentSearch=models.CharField(max_length=5000,default="{}")
    recommendedProduct=models.CharField(max_length=5000,default="{}")

    def __str(self):
        return self.user.username



class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."  


class Donation(models.Model):
    name=models.CharField(max_length=500)
    quantity=models.IntegerField(max_length=10)
    adderess=models.CharField(max_length=1000)
    phone=models.CharField(max_length=11,default="")
    
    def __str__(self):
        return self.name