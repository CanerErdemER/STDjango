from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def books(request):
    return HttpResponse('Kitaplar')
def details(request):
    return HttpResponse("Detay Sayfası")
def martı(request):
    return HttpResponse("Martı Sayfası")
def prens(request):
    return HttpResponse("Prens Sayfası")
