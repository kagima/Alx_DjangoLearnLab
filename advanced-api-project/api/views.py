from  django.db import transaction
from django.db.models import Q
from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Book List View and permissions
class BookListView(generics.ListAPIView):
    """Read-only endpoint that lists all books.
    Permission:
    - AllowAny (public read).
    Customizations:
    - Query params:
        ?year=YYYY                 -> exact publication year
        ?year_min=YYYY&year_max=YYYY -> inclusive range
        ?author=<id>               -> filter by author id
        ?author_name=substring     -> case-insensitive author name match
        ?search=...                -> title/author name search (DRF SearchFilter)
        ?ordering=publication_year -> sort by year (prefix with '-' for desc)
    - Adds select_related('author') to cut DB queries when including author ids.   
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title', 'id']
    ordering = ['title']
    
    def get_queryset(self):
        qs = Book.objects.select_related('author').all()
        
        year = self.request.query_params.get('year')
        year_min = self.request.query_params.get('year_min')
        year_max = self.request.query_params.get('year_max')
        author = self.request.query_params.get('author')
        author_name = self.request.query_params.get('author_name')
        
        if year:
            try:
                qs = qs.filter(publication_year=int(year))
            except ValueError:
                raise ValidationError({"year": "Year must be an integer (YYYY)."})
        
        if year_min or year_max:
            try:
                if year_min:
                    qs = qs.filter(publication_year__gte=int(year_min))
                if year_max:
                    qs = qs.filter(publication_year__lte=int(year_max))
            except ValueError:
                raise ValidationError({"year": "year_min/year_max must be integers."})
            
        if author:
            try:
                qs = qs.filter(author_id=int(author))
            except ValueError:
                raise ValidationError({"author": "author must be an integer (author id)."})
            
        if author_name:
            qs = qs.filter(author__name__icontains=author_name)
        return qs
    
# Class for book detail view
class BookDetailView(generics.RetrieveAPIView):
    """
        Read-only view that returns a single book by primary key (id)
        Permissions:
        - AllowAny (public read)
    """  
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# Class for book creation view
class BookCreateView(generics.CreateAPIView):
    """Create a new book
       Permissions:
       - Authenticated users only
       Customizations:
       - perform_create: wrap in a transaction and normalize title whitespace.
       - Additional server-side guard to ensure title isn't blank after stripping, complementing serializer validation.
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    @transaction.atomic
    def perform_create(self, serializer):
        title = (self.request.data.ge("title") or "").strip()
        if not title:
            raise ValidationError({"title": "Title cannot be blank."})
        serializer.save(title=title)
        
# Class for book update view
class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book (PUT/PATCH)
       Permissions:
       - Authenticated users only
       Customizations:
       - Perform_update: normalize title, stay atomic.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    
    @transaction.atomic
    def perform_update(self, serializer):
        title = (self.request.data.get("title") or "").strip()
        if title == "":
            raise ValidationError({"title": "Title cannot be blank."})
        serializer.save(title=title if title else serializer.instance.title)
        
# Class for book delete view
class BookDeleteView(generics.DestroyAPIView):
    """Delete a book.
       Permissions:
       - Authenticated users only
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]                                                         
    
