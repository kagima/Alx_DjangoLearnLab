from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Function to list all books
def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'book': books})


# class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    
# Function to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'application_app/register.html', {'form': form})
             
