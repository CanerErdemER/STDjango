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
def index(request):
    return render(request,'books/index.html')

def books(request):
    list_item=''
    category_list =list(data.keys())
    for category in category_list:
        redirect_url=reverse("books_by_category",args=[category])
        list_item += f"<li><a href='{redirect_url}'>{category}</a></li>"
        html = f"<h1>Kitap Listesi</h1><br><ul>{list_item}</ul> "
    return HttpResponse(html)

def details(request,book_name):
    return HttpResponse(f"{book_name} detay sayfası")

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
   
