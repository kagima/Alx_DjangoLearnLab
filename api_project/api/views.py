from rest_framework import generics
from .models import Book
from rest_framework import ViewSets
from .serializers import BookSerializer

# Class-based view to handle book listing
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer for serialization


# Book set view
class BookViewSet(ViewSets.ModelViewSet):
    """"
      Book set view that handles all the CRUD operations for books.
      
    """
    queryset = Book.objects.all() # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer for serialization