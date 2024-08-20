from django.urls import path
from . import views


#http://127.0.0.1:8000      -->Anasayfa
#http://127.0.0.1:8000/Home  -->Anasayfa
#http://127.0.0.1:8000/Books -->Kitaplar





urlpatterns = [
    path('Books',views.books),
    path('Details',views.details),
    path('Martı',views.martı),
    path('Prens',views.prens),
]