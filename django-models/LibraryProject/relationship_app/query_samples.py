from relationship_app.models import Author, Book, Library, Librarian

# Query 1
# Query to get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author_name}:")
        for book in author.books.all():
            print(f" - {book.title}")
        return author.books.all()
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
        return None
    
# Query 2
# List all books in a library.
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f" - {book.title}")
        return books    
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None         