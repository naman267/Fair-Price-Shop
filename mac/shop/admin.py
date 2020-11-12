from django.contrib import admin

# Register your models here.
from . models import Product , Contact,Order,OrderUpdate,Profile,Donation
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(Profile)
admin.site.register(Donation)