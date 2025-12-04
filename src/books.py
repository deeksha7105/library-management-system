class Books:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        self.books.append({
            "book_id": book_id,
            "title": title,
            "author": author,
            "status": "Available"
        })
        return f"Book '{title}' added successfully."

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book
        return "Book not found."
