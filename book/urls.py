from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#http://127.0.0.1:8000       -->Anasayfa
#http://127.0.0.1:8000/Home  -->Anasayfa
#http://127.0.0.1:8000/Books -->Kitaplar

urlpatterns = [
    path('',views.index),
    path('<book_id>',views.details,name="book_details"),
    path("category/<int:category_id>",views.getbooksByCategoryId),
    path("category/<str:category_name>",views.getbooksByCategoryName,name='books_by_category'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# static_url --> settings'te
# media peth --> url için