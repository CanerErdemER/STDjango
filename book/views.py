from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from . models import books,Category

# Create your views here.
data={
    "roman":"roman kategorisine ait kitaplar",
    "hikaye":"hikaye kategorisine ait kitaplar",
    "deneme":"deneme kategorisine ait kitaplar",
    
}

db={
    "books":[
        {
            "title":"Kürk Mantolu Madonna",
            "writer":"Sabahattin Ali",
            "publish_date":"1943",
            "image":"KM_Madonna.jpg",
            "slug":"KM_Madonna",
            "isActive":True,
            "isupdated":True,
            "stock":0,
            "description":"Kürk Mantolu Madonna, Sabahattin Ali'nin 1943 yılında yayımladığı bir romanıdır. Kitapta dokunaklı bir aşk hikâyesi anlatılmaktadır.",
            
        },
        
        {
            "title":"Yalnız Efe",
            "writer":"Ömer Seyfettin",
            "publish_date":"1919",
            "image":"Y_Efe.jpg",
            "slug":"Y_Efe",
            "isActive":True,
            "stock":5,
            "isupdated":True,
            "description":"Kezban isimli bir genç kızın babası ve kendisinin uğradığı haksızlık sonucunda dağa çıkması, haksızlığa uğrayan herkes için mücadele etmesi anlatılmaktadır.",
        },
        
        {
            "title":"Kendine Hoş Geldin",
            "writer":"Miraç Çağrı Aktaş",
            "publish_date":"2019",
            "image":"KH_Geldin.jpg",
            "slug":"KH_Geldin",
            "isActive":True,
            "stock":5,
            "isupdated":True,
            "description":"Kendine Hoş Geldin adlı kitabında sizi, kendinizi bulmaya ve hak ettiğiniz değeri kendinize vermeye çağırıyor. Bu kitapla duygu dünyanızın yegane başrolü olan benliğinize geri dönecek ve kendinize tüm içtenliğinizle “Hoş Geldin!” diyeceksiniz.",
        },
    ],
    "categories":[
        {"id":1,"name":"roman","slug":"roman"},
        {"id":2,"name":"hikaye","slug":"hikaye"},
        {"id":3,"name":"deneme","slug":"deneme"},
        
        ]
}


def index(request):
    book_S=books.objects.all()
    categorys=Category.objects.all()
    return render (request,'books/index.html',{
        'categories':categorys,
            'books':book_S,
    })

def details(request,book_id):
    # try:
    #     book = books.objects.get(pk=book_id)
    # except:
    #     raise Http404()
    
    book=get_object_or_404(books,pk=book_id)
    ctx={
        'book':book
    }
    return render(request,'books/details.html',ctx)


def getbooksByCategoryName(request,category_name):
    try:
        category_text=data[category_name]
        return render(request,'books/book_s.html',{
            'category': category_name,
            'category_text': category_text
            })
    except:
        return HttpResponseNotFound("Kategori mevcut değil.")

def getbooksByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Kategori mevcut değil.")
    
    category_name=category_list[category_id-1]
    
    redirect_url=reverse('books_by_category',args=[category_name])
    
    return redirect (redirect_url)
   
