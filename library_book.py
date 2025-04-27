# library_book.py

class LibraryBook:
    def __init__(self, title, author, available=True):
        """Initialize the book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.available = available

    def borrow_book(self):
        """Borrow the book if it's available."""
        if not self.available:
            raise ValueError("Book is already borrowed.")
        self.available = False
        return self.available

    def return_book(self):
        """Return the book to the library."""
        if self.available:
            raise ValueError("Book is already in the library.")
        self.available = True
        return self.available

    def is_available(self):
        """Check if the book is available."""
        return self.available
