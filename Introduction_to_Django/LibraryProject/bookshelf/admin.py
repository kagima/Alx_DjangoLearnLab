from django.contrib import admin
from .models import Book

# Register the Book model with the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('author', 'publication_year')            # Filters on right
    search_fields = ('title', 'author')                     # Search bar

