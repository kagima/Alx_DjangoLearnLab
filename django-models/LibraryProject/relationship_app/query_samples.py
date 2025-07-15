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
        return None