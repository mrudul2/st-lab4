# test_library_book.py

import unittest
from library_book import LibraryBook

class TestLibraryBook(unittest.TestCase):
    def setUp(self):
        """Set up a sample book for testing."""
        self.book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald")

    def test_initial_availability(self):
        """Test if a new book is initially available."""
        self.assertTrue(self.book.is_available())

    def test_borrow_book(self):
        """Test borrowing an available book."""
        self.book.borrow_book()
        self.assertFalse(self.book.is_available())

    def test_return_book(self):
        """Test returning a borrowed book."""
        self.book.borrow_book()
        self.book.return_book()
        self.assertTrue(self.book.is_available())

    def test_borrow_unavailable_book(self):
        """Test that borrowing an already borrowed book raises an error."""
        self.book.borrow_book()
        with self.assertRaises(ValueError):
            self.book.borrow_book()

    def test_return_available_book(self):
        """Test that returning an already available book raises an error."""
        with self.assertRaises(ValueError):
            self.book.return_book()
    
    def test_multiple_borrow_return_cycles(self):
        """Test borrowing and returning the book multiple times."""
        self.book.borrow_book()
        self.book.return_book()
        self.book.borrow_book()
        self.assertFalse(self.book.is_available())

    def test_borrow_and_return_sequence(self):
        """Test a sequence of borrow and return operations."""
        self.assertTrue(self.book.is_available())
        self.book.borrow_book()
        self.assertFalse(self.book.is_available())
        self.book.return_book()
        self.assertTrue(self.book.is_available())


if __name__ == '__main__':
    unittest.main()
