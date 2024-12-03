class Libraly:
    def __init__(self, books):
        self.books = books
    
    def add_book(self, book_title):
        if book_title in self.books:
            print(f"Book {book_title} is already in the Libraly")
        else:
            self.books[book_title] = True
            print(f"Book {book_title} is added succesfully")
        
    def borrow(self,book_title):
        if book_title in self.books:
            self.books[book_title] = False
            print(f"Book {book_title} is succesfully borrowed")
        elif book_title not in self.books:
            print(f"Book {book_title} does not exist in the libraly")
        elif not self.books[book_title]:
            print(f"Book {book_title} is not available currently")
        
    def return_book(self, book_title):
        if book_title not in self.books:
            print(f"Book {book_title} does not belong to the libraly")
        elif self.book[book_title]:
            print(f"Book {book_title} is already available")
        else:
            self.books[book_title] = True
            print(f"Book {book_title} is returned succcesfully")
        
    def list_available_books(self):
        
        available_books = [book for book, available in self.books.items() if available]
        if available_books:
            print("Available books: ")
            for book in available_books:
                print(f" {book}")
        else:
            print("No available books")
            
books = {
    "Под Игото": True,
    "1984": True,
    "Малкият принц": False
}

libraly = Libraly(books)

while True:
    print("Choose what do to: 1. Add Book; 2. Borrow book; 3. Return book; 4. List available books, 5. Exit")
    choice = int(input())
    if choice == 1:
        book_title = input("Input a name of the book: ")
        libraly.add_book(book_title)
    elif choice == 2:
        book_title = input("Input a name of the book: ")
        libraly.borrow(book_title)
    elif choice == 3:
        book_title = input("Input a name of the book: ")
        libraly.return_book(book_title)
        
    elif choice == 4:
            libraly.list_available_books()

    elif choice == 5:
       print("Exiting the program")
       break
    else:
       print("Not a valid choice. Choose between 1-5") 
    