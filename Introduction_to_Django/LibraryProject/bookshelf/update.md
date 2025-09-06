
---

### `update.md`

```markdown
# Update Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.all()
# Output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
