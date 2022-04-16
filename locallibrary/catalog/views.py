from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genre = Genre.objects.all().count()

    num_books_with = Book.objects.filter(title__contains='oliver').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_books_with': num_books_with,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

    #context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]

    template_name = 'catalog/book_list.html'  # Specify your own template name/location
