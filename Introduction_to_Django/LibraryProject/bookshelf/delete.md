
---

### **4️⃣ `delete.md`** ❌ (fix)

```markdown
# Delete Book

```python
from bookshelf.models import Book

# Get the specific book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>

