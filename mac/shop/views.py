from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product,Contact,Order,OrderUpdate,Profile,Donation
from math import ceil
import json
from django.views.generic import View
from django.shortcuts import redirect
# Create your views here.
class Donate(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/donation.html")

    def post(self,request,*args,**kwargs):
        name = request.POST['name']
        qty = request.POST['quantity']
        adderess = request.POST['adderess']
        phone = request.POST['phone']
        donate = Donation(name=name, quantity=qty, adderess=adderess, phone=phone)
        donate.save()
        params = {'ok': True}
        return render(request, "shop/donation.html", params)

def donate(request):
    if request.method=='POST':
        name=request.POST['name']
        qty=request.POST['quantity']
        adderess=request.POST['adderess']
        phone=request.POST['phone']
        donate= Donation(name=name,quantity=qty,adderess=adderess,phone=phone)
        donate.save()
        params={'ok':True}
        return render(request,"shop/donation.html",params)
    return render(request,"shop/donation.html")

class Index(View):
    def get(self,request,*args,**kwargs):
        catprods = Product.objects.values('category', 'id')
        cats = {item["category"] for item in catprods}
        allProds = []
        user = Profile.objects.get(user=request.user)
        cart = user.cart_json
        recommend = user.recommendedProduct
        print("ho", cart)
        for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nslides = n // 3 + ceil((n / 3) - (n // 3))
            allProds.append([prod, range(1, nslides), nslides])

        params = {'allProds': allProds, 'cart_json': cart, 'recommend': recommend}
        return render(request, "shop/index.html", params)

#def index(request):

 #   catprods=Product.objects.values('category','id')
  #  cats={item["category"] for item in catprods}
  #  allProds=[]
  #  user=Profile.objects.get(user=request.user)
  #  cart=user.cart_json
  #  recommend=user.recommendedProduct
  #  print("ho",cart)
  #  for cat in cats:
   #     prod=Product.objects.filter(category=cat)
   #     n = len(prod)
   #     nslides = n // 3 + ceil((n / 3) - (n // 3))
   #     allProds.append([prod,range(1,nslides),nslides])

    #params={'allProds':allProds,'cart_json':cart,'recommend':recommend}
    #return render(request,"shop/index.html",params)

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/about.html")
def about(request):
    return render(request,"shop/about.html")

class Ccontact(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/contact.html")

    def post(self,request,*args,**kwargs):
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return render(request, "shop/contact.html")

def contact(request):
    if request.method=='POST':
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, "shop/contact.html")
class Tracker(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/tracker.html")

    def post(self,request,*args,**kwargs):
        print(request.method)
        if request.method == "POST":
            orderId = request.POST.get('orderId', '')
            email = request.POST.get('email', '')
            print(orderId, email)
            try:
                print(Order)
                order = Order.objects.filter(order_id=orderId, email=email)
                print(order[0])
                if (len(order) > 0):
                    print("order", order)
                    update = OrderUpdate.objects.filter(order_id=orderId)
                    updates = []
                    for item in update:
                        updates.append({'text': item.update_desc, 'time': item.timestamp})
                    print("yes", updates)
                    city = order[0].city
                    print("city", city)
                    if city == 'delhi':
                        city = 'Delhi'
                    response = json.dumps(
                        {"status": "success", "updates": updates, "itemsjson": order[0].item_json, 'city': city},
                        default=str)
                    return HttpResponse(response)
                else:
                    return HttpResponse('{"status":"no item"}')
            except Exception as e:
                return HttpResponse('{"status":"Error"}')

def tracker(request):
    print(request.method)
    if request.method=="POST":
     orderId=request.POST.get('orderId','')
     email=request.POST.get('email','')
     print(orderId,email)
     try:
         print(Order)
         order=Order.objects.filter(order_id=orderId,email=email)
         print(order[0])
         if (len(order)>0):
             print("order",order)   
             update=OrderUpdate.objects.filter(order_id=orderId)
             updates=[]
             for item in update:
                 updates.append({'text':item.update_desc,'time':item.timestamp})
             print("yes",updates)    
             city=order[0].city
             print("city",city)
             if city=='delhi':
                city='Delhi'
             response=json.dumps({"status":"success","updates":updates,"itemsjson":order[0].item_json,'city':city},default=str)
             return HttpResponse(response)
         else:
             return HttpResponse('{"status":"no item"}')
     except Exception as e:
         return HttpResponse('{"status":"Error"}')
    return render(request, "shop/tracker.html")

class Prodview(View):
    def get(self,request,myid,*args,**kwargs):
        product = Product.objects.filter(id=myid)
        print(product)
        params = {"product": product[0]}
        return render(request, "shop/prodView.html", params)

def prodView(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    params={"product":product[0]}
    return render(request, "shop/prodView.html" ,params)
def searchquery(query,item):
    query=query.lower()

    print(query)
    if query in item.product_name.lower() or query in item.category.lower() or query in item.sub_category.lower() or query in item.desc.lower():
        return True
    else:
        return False
class Search(View):
    def get(self,request,*args,**kwargs):
        query = request.GET.get('search', '')
        catprods = Product.objects.values('category', 'id')
        cats = {item["category"] for item in catprods}
        allProds = []
        for cat in cats:
            prodtemp = Product.objects.filter(category=cat)
            prod = [item for item in prodtemp if searchquery(query, item)]
            n = len(prod)
            nslides = n // 4 + ceil((n / 4) - (n // 4))
            if len(prod) != 0:
                allProds.append([prod, range(1, nslides), nslides])

        params = {'allProds': allProds}
        return render(request, "shop/index.html", params)


def search(request):
    query=request.GET.get('search','')
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    allProds = []
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchquery(query,item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allProds.append([prod, range(1, nslides), nslides])

    params = {'allProds': allProds}
    return render(request, "shop/index.html",params)
class Checkout(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/checkout.html")
    def post(self,request,*args,**kwargs):
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')

        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=items_json, name=name, email=email, phone=phone, address=address, city=city,
                      state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Order has been Placed")
        update.save()
        id = order.order_id
        thank = True
        print(items_json)
        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})


def checkout(request):
    print(request.method)
    if request.method == 'POST':
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')+" "+request.POST.get('address2', '')

        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=items_json,name=name, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Order has been Placed")
        update.save()
        id=order.order_id
        thank=True
        print(items_json)
        return render(request, "shop/checkout.html", {'thank': thank , 'id' : id  })
    return render(request,"shop/checkout.html")

class Buy(View):
    def get(self,request,myid,*args,**kwargs):
        product = Product.objects.filter(id=myid)
        print(product)
        params = {"product": product[0]}
        return render(request, "shop/buy.html", params)

    def post(self,request,*args,**kwargs):
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')+" "+request.POST.get('address2', '')

        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=items_json,name=name, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Order has been Placed")
        update.save()
        id=order.order_id
        thank=True
        return render(request, "shop/buy.html", {'thank': thank , 'id' : id  })

def buy(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    params={"product":product[0]}
    if request.method == 'POST':
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')+" "+request.POST.get('address2', '')

        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=items_json,name=name, email=email, phone=phone, address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Order has been Placed")
        update.save()
        id=order.order_id
        thank=True
        return render(request, "shop/buy.html", {'thank': thank , 'id' : id  })
    return render(request, "shop/buy.html" ,params)


class Handlelogin(View):
    def get(self,request,*args,**kwargs):
        account = True
        return render(request, "shop/login.html", {"account": account})
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            username = request.POST['Username']
            password = request.POST['passwordlogin']
            user = authenticate(username=username, password=password)

            print(user)
            if user is not None:
                login(request, user)
                # user=Profile.objects.get(user=request.user)
                # cart=user.cart_json
                # print("ho",cart)*/
                messages.success(request, 'Login Succesfully')
                account = True

                return render(request, "shop/index.html", {"account": account, "username": user})
            else:
                account = False
                return render(request, "shop/login.html", {"account": account})

def handlelogin(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['passwordlogin']
        user=authenticate(username=username,password=password)
        
        print(user)
        if user is not None:
            login(request,user)
            #user=Profile.objects.get(user=request.user)
            #cart=user.cart_json
            #print("ho",cart)*/
            messages.success(request,'Login Succesfully')
            account=True

            return render(request, "shop/index.html",{"account":account,"username":user})
        else:
            account=False
            return render(request,"shop/login.html",{"account":account})
    account=True        
    return render(request,"shop/login.html",{"account":account})

class Handlesignup(View):
    def get(self,request,*args,**kwargs):
        return render(request, "shop/signup.html")

    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cart = {}
        cart = json.dumps(cart)
        # 'pr2":[3,"John Player Tshirt (L/M/XXL)"],"pr6":[3,"Lancer Shoes"],"pr7":[4,"Levis Jeans"]}'
        # recommend={"pr2":[1,"John Player Tshirt"],"pr6":[1,"Lancer Shoes"],"pr7":[1,"Levis Jeans"]}
       
        recommend={"pr52":[1,"shop/images/hideandseek.jpg","Parle Platina Hide & Seek Chocolate Chip",52],"pr47":[1,"shop/images/Haldi.jpg","Mother's Choice Turmeric Powder / Haldi",47],"pr61":[1,"shop/images/Foil.jpg","Happy Home Aluminium Foil (21 m)",61]}                                    
        recommend = json.dumps(recommend)
        try:

            myuser = User.objects.create_user(username, email, password)
            profileuser = Profile(phone=phone, cart_json=cart, user=myuser, recommendedProduct=recommend)
            profileuser.save()
            login(request, myuser)

            messages.success(request, "Account Created")
            success = True
            return render(request, "shop/index.html", {"Account": success})

        except:
            return render(request, "shop/signup.html", {"Account": True})

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        cart={}
        cart=json.dumps(cart)
        #'pr2":[3,"John Player Tshirt (L/M/XXL)"],"pr6":[3,"Lancer Shoes"],"pr7":[4,"Levis Jeans"]}'
       # recommend={"pr2":[1,"John Player Tshirt"],"pr6":[1,"Lancer Shoes"],"pr7":[1,"Levis Jeans"]}
        recommend={"pr52":[1,"shop/images/hideandseek.jpg","Parle Platina Hide & Seek Chocolate Chip",52],"pr47":[1,"shop/images/Haldi.jpg","Mother's Choice Turmeric Powder / Haldi",47],"pr61":[1,"shop/images/Foil.jpg","Happy Home Aluminium Foil (21 m)",61]}                                                                                                                                                                 
        recommend=json.dumps(recommend)
        try:
            
            myuser=User.objects.create_user(username,email,password)
            profileuser=Profile(phone=phone,cart_json=cart,user=myuser,recommendedProduct=recommend)
            profileuser.save()
            login(request,myuser)

            messages.success(request,"Account Created")
            success=True
            return render(request,"shop/index.html",{"Account":success})
        
        except:
            return render(request,"shop/signup.html",{"Account":True})
    return render(request,"shop/signup.html")



class Handlelogout(View):
    def post(self,request,*args,**kwargs):
        datas = Profile.objects.get(user=request.user)

        cartJson = request.POST.get('cartJson', '{}')
        recommend = request.POST.get('recommend', '{}')

        print("yes", datas.phone)
        datas.cart_json = cartJson
        datas.recommendedProduct = recommend

        datas.save()

        print(cartJson)
        logout(request)
        logoutt = True
        return render(request, "shop/login.html", {"logout": logoutt});
    def get(self,request,*args,**kwargs):
        return render(request, "shop/login.html");


def handlelogout(request):
    if request.method=='POST':
        datas=Profile.objects.get(user=request.user)
       
        cartJson=request.POST.get('cartJson','{}')
        recommend=request.POST.get('recommend','{}')

        print("yes",datas.phone)       
        datas.cart_json=cartJson
        datas.recommendedProduct=recommend
        
        datas.save()
        
        print(cartJson)
        logout(request)
        logoutt=True
        return render(request,"shop/login.html",{"logout":logoutt})
    

    return Httpresponse("404 NOT FOUND")    
