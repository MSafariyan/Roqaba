from django.shortcuts import render, HttpResponse, Http404
from main_app.models import Book, Publisher, Product, Book_Price_history
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

@csrf_exempt
def get_book(request):
    # product = Product.objects.filter().all()
    if request.is_ajax():
        term = request.GET.get('term') 
        product = Book.objects.filter(title__search=term).all()
        print(term)
        data = list(product.values('id', 'title', 'publisher__publisher_name'))
        print(type(data))
        return JsonResponse(data, safe=False )
    
    
def liveSearch(request):
    if request.is_ajax():
        q = request.GET.get("q")
        
        product = Product.objects.filter(title__search=q).all()
        data = list(product.values('id','title','current_price','special_price','img'))
        return JsonResponse(data, safe=False, status=200)
    
def chart(request):
    return False