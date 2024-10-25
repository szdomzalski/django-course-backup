from django.db.models import Avg
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all().order_by('title')
    total_books = books.count()
    average_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {'books': books, 'total': total_books, 'avg_rate': average_rating})


def book(request: HttpRequest, slug: str) -> HttpResponse:
    # try:
    #     specified_book = Book.objects.get(pk=id)
    # except Exception:
    #     raise Http404()
    specified_book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book.html', {'book': specified_book})
