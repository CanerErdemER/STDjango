from django.urls import path
from book import views
from pages import views

#http://127.0.0.1:8000/Users      -->Anasayfa
#http://127.0.0.1:8000/Home  -->Anasayfa
#http://127.0.0.1:8000/Books -->Kitaplar

urlpatterns = [
    path('',views.home),
    path('Home',views.home),
    path('about_us',views.aboutus),
    path('communication',views.communication),
    ]