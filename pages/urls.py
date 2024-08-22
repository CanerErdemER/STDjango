from django.urls import path
from book import views
from pages import views

#http://127.0.0.1:8000/Users  -->Anasayfa
#http://127.0.0.1:8000/Home  -->Anasayfa
#http://127.0.0.1:8000/Books -->Kitaplar

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('about',views.aboutus),
    path('contact',views.contact),
    ]