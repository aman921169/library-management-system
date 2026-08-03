import json
from re import search
books = []
#here we are importing the json module and creating an empty list called books
def save_books():
    with open("books.json", "w")as file:
        json.dump(books, file, indent=4)
        #this function is used to save the books to a json file

#here we are creating a function called load_books that will load the books from a json file
def load_books():
    global books

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
        #this function is used to load the books from a json file
load_books()

#here we are creating a function called find_book that will search for a book by title
def find_book(search):
     for book in books:
        if search.strip().lower() == book["title"].strip().lower():
            return book
     return None

#here we are creating a function called add_book that will allow the user to add a book to the list of books
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    book = {
        "title": title,
        "author": author,
        "available": True
    }
    books.append(book)
    save_books()
    print("Book added successfully!")

#here we are creating a function called view_books that will display the list of books
def view_books():
    print("\n===== BOOKS =====")
    for book in books:  
        status = "Yes" if book["available"] else "No"
        print("Title :", book["title"])
        print("Author:", book["author"])
        print("status:", "Available" if book["available"] else "Not Available")
        print("--------------------")

#here we are creating a function called search_books that will allow the user to search for a book by title
def search_books():
     print("search for books....")
     search = input("enter the title of the books you want to search:")

     book = find_book(search)
     if book:
        print("\n===== BOOKS =====")
        print("Title :", book["title"])
        print("Author:", book["author"])
        print("--------------------")
     else:
        print("No books found with the title:", search)
                #here we are checking if the title of the book is not equal to the search term

  #here we are creating a function called borrow_books that will allow the user to borrow a book  
def borrow_books():
     print("enter books you want to borrow")
     search = input("enter the title of the books you want to borrow: ")
     book = find_book(search)
     
     if book:
            if book["available"]:
                        book["available"] = False
                        save_books()
                        print("You have borrowed the book:", book["title"])
            else:
                        print("Sorry, the book is not available for borrowing.")
     else:
         print("No books found with the title:", search)

#here we are creating a function called return_books that will allow the user to return a book
def return_books():
    print("enter books you want to return")
    search = input("enter the title of the books you want to return:")
    found = False
    book = find_book(search)
    if book:
        if not book["available"]:
                        book["available"] = True
                        save_books()
                        print("You have returned the book:", book["title"])
        else:
                       print("this book is already in library")
    else:
        print("No books found with the title:", search)
                
#here we are creating a function called delete_books that will delete a book from the list of books
def delete_books():
     print("Enter the book title you wanna delete")
     search = input("enter the title of the books you want to delete:")
     book = find_book(search)
     if book:
                     books.remove(book)
                     save_books()
                     print("You have deleted the book:", book["title"])
     else:   
                    print("No books found with the title:", search)
            

#here we are creating a function called edit_books that will allow the user to edit a book's title and author
def edit_books():
     print("Enter the book title you wanna edit")
     search = input("enter the title of book you wanna edit:")
     book = find_book(search)
     if book:
                     new_title = input("Enter new title: ")
                     new_author = input("Enter new author:")
                     book["title"] = new_title
                     book["author"] = new_author
                     save_books()
                     print("Book updated successfully!")
     else:
                    print("No books found with the title:", search)

#here we are creating a while loop that will run until the user chooses to exit the program
while True:
    #our main menu
    print("\n===== LIBRARY =====")
    print("1. Add Book") 
    print("2. View Books")
    print("3. search for books")
    print("4. borrow books")
    print("5. return books")
    print("6. delete books")
    print("7. Edit books")
    print("8. Exit")
    #this is where we take the input from the user
    choice = input("Enter choice: ")

    if choice == "1":
        # add book here
        add_book()

    elif choice == "2":
        # view books here
        view_books()

    elif choice == "3":
        # search for books here
        search_books()

    elif choice == "4":
        # borrow books here
        borrow_books()

    elif choice == "5":
        # return books here
        return_books()

    elif choice == "6":
        # delete books here
        delete_books()

    elif choice == "7":
        # edit books here
        edit_books()

    elif choice == "8":
        # exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice")
