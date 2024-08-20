from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
data={
    "roman":"roman kategorisine ait kitaplar",
    "hikaye":"hikaye kategorisine ait kitaplar",
    "deneme":"deneme kategorisine ait kitaplar",
    "siir":"siir kategorisine ait kitaplar",
}

def books(request):
    return HttpResponse('Kitaplar')

def details(request,book_name):
    return HttpResponse(f"{book_name}Detay Sayfası")

def getbooksByCategoryName(request,category_name):
    try:
        category_text=data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Kategori mevcut değil.")

def getbooksByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Kategori mevcut değil.")
    
    category_name=category_list[category_id-1]
    
    redirect_url=reverse('books_by_category',args=[category_name])
    
    return redirect (redirect_url)
   
