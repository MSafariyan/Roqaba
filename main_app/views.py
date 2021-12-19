from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import Book, Product, Publisher, Book_Price_history
from django.contrib.auth.decorators import login_required
from .forms import editProductForm
from django.forms.models import model_to_dict
from django.http import JsonResponse
import pandas as pd


def index(request):
    products = Product.objects.order_by("-current_price")[:50]
    return render(
        request, "main_app/index.html", {"title": "Home", "products": products}
    )


def show_product(request, id):
    try:
        product = Product.objects.filter(id=id).first()
        publishers = Publisher.objects.all()
        child = Book.objects.filter(parent=id).order_by("publisher").all()
        books = Book.objects.filter(parent=id).order_by("publisher")
        labels = []
        block = []
        for book in books:
            row = []
            for candel in Book_Price_history.objects.filter(Book_id=book.pk):
                row = [
                    *row,
                    (
                        candel.Book_id.pk,
                        candel.Book_id.publisher.publisher_name,
                        candel.current_price,
                        candel.special_price,
                    ),
                ]
                labels.append(candel.created_at)
            block.append((row))
        labels = list(set(labels))
        print(labels)
        labels = sorted(labels)
        labels = labels[::-1]
        print(labels)
    except:
        raise Http404
    print(block)
    return render(
        request,
        "main_app/show-product.html",
        {
            "title": product.title,
            "product": product,
            "children": child,
            "data": block,
            "labels": labels,
        },
    )


@login_required
def edit_product(request, id):
    product = Product.objects.filter(id=id).first()
    if request.method == "POST":
        data = request.POST.getlist("products[]")
        # remove old related books
        oldRelated = Book.objects.filter(parent=product).all()
        for book in oldRelated:
            book.parent = None
            book.save()
        #     # add new products
        for ids in data:
            book = Book.objects.filter(id=ids).first()
            book.parent = product
            book.save()
        #     # update product details
        product.title = request.POST.get("product_name")
        product.current_price = request.POST.get("current_price")
        product.special_price = request.POST.get("special_price")
        product.save()
        #     # back to product page
        product = Product.objects.filter(id=id).first()
        child = Book.objects.filter(parent=id).order_by("special_price").all()
        return redirect(show_product, id)
    else:
        books = Book.objects.filter(parent=product).all()
        selected = list(
            books.values("id", "title", "publisher__publisher_name")
        )
        data = {
            "product_name": product.title,
            "current_price": product.current_price,
            "special_price": product.special_price,
            "selected": selected,
        }
        print(data)
        form = editProductForm(
            initial=data,
        )
    return render(
        request,
        "main_app/edit-product.html",
        {
            "title": product.title,
            "product": product,
            "form": form,
            "data": data,
        },
    )
