from django.shortcuts import render
from .models import Book

# Function to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship/list_books.html', {'book': books})
