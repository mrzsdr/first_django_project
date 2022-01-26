from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})
    #return HttpResponse('<p>home view</p>')

def book_detail(request, id):
    try:
       book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book not found')
    return render(request, 'book_detail.html', {'book': book})     
    #return HttpResponse('<p>book_detail view with the id {}</p>'.format(id))  

# Create your views here.
