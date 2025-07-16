from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship/list_books.html', {'book': books})


# class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship/library_detail.html'
    context_object_name = 'library'
