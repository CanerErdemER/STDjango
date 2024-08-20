from django.urls import path
from . import views


#http://127.0.0.1:8000       -->Anasayfa
#http://127.0.0.1:8000/Home  -->Anasayfa
#http://127.0.0.1:8000/Books -->Kitaplar

urlpatterns = [
    path('',views.books),
    path('list',views.books),
    path('<book_name>',views.details),
    path("category/<int:category_id>",views.getbooksByCategoryId),
    path("category/<str:category_name>",views.getbooksByCategoryName,name='books_by_category'),
    ]