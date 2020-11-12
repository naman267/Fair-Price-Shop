from django.urls import path
from . import views

urlpatterns = [
    path("",views.Index.as_view(),name='ShopHome'),
    path("about/",views.About.as_view(),name='about'),
    path("contact/",views.Ccontact.as_view(),name='contact'),
    path("search",views.Search.as_view(),name='search'),
    path("tracker",views.Tracker.as_view(),name='tracker'),
    path("products/<int:myid>",views.Prodview.as_view(),name='productview'),
    path("checkout",views.Checkout.as_view(),name='checkout'),
    path("buy/<int:myid>",views.Buy.as_view(),name='buy'),
    path("login",views.Handlelogin.as_view(),name='login'),
    path("signup",views.Handlesignup.as_view(),name='signup'),
    path("logout",views.Handlelogout.as_view(),name='logout'),
    path("Donate",views.Donate.as_view(),name='donate')
]

