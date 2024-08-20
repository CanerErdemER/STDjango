from django.urls import path
from . import views


#http://127.0.0.1:8000/Users      -->Anasayfa
#http://127.0.0.1:8000/Users/Home  -->Anasayfa
#http://127.0.0.1:8000/Users/Books -->Kitaplar





urlpatterns = [
    path('',views.home),
    path('Home',views.home),
    path('about_us',views.aboutus),
    path('Communication',views.communication),
    ]