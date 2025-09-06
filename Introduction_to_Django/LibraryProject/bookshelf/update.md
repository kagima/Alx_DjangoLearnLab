
---

### **3️⃣ `update.md`** ❌ (fix)

```markdown
# Update Book

```python
from bookshelf.models import Book

# Get the specific book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

