# DRF Generic Views for Book

This project uses Django REST Framework generic views to provide granular CRUD endpoints for the `Book` model.

## Endpoints

- `GET /api/books/` — **List** all books. Supports:
  - `?year=YYYY`
  - `?year_min=YYYY&year_max=YYYY`
  - `?author=<id>`
  - `?author_name=<substring>`
  - `?search=<text>` (title/author name)
  - `?ordering=publication_year` (prefix `-` for desc)
- `GET /api/books/<pk>/` — **Detail** for a single book.
- `POST /api/books/create/` — **Create** (auth required).
- `PUT/PATCH /api/books/<pk>/update/` — **Update** (auth required).
- `DELETE /api/books/<pk>/delete/` — **Delete** (auth required).

## Permissions

- Read-only for anonymous users (List/Detail).
- Create/Update/Delete require authentication.
- Global default (optional) in `settings.py`:
  `DEFAULT_PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly]`.
  Create/Update/Delete views still explicitly enforce `IsAuthenticated`.

## Notes

- Business rules (e.g., `publication_year` cannot be in the future) are enforced in `BookSerializer`.
- Additional view-level guards normalize `title` and ensure it is not blank.
- `BookListView` allows filtering, search, and ordering without installing `django-filter`.

## Testing

Use the DRF browsable API or curl/Postman. With curl, pass `-u <user>:<pass>` for write operations.
