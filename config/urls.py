from django.contrib import admin
from django.urls import include, path


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('books/',include('book.urls')),
    path('',include('pages.urls')),
]
