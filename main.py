import json
books = []
#here we are importing the json module and creating an empty list called books
def save_books():
    with open("books.json", "w")as file:
        json.dump(books, file, indent=4)
        #this function is used to save the books to a json file
def load_books():
    global books

    try:
        with open("books.json", "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
        #this function is used to load the books from a json file
load_books()
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
def view_books():
    print("\n===== BOOKS =====")
    for book in books:  
        print("Title :", book["title"])
        print("Author:", book["author"])
        print("--------------------")
def search_books():
     print("search for books....")
     search = input("enter the title of the books you want to search: ")
     #found is a boolean variable that is used to check if the book is found or not
     found = False 
     for book in books:
                #here we are checking if the title of the book is equal to the search term
                if search == book["title"]:
                    found = True
                    print("\n===== BOOKS =====")
                    print("Title :", book["title"])
                    print("Author:", book["author"])
                    print("--------------------")
                    break
                #here we are checking if the title of the book is not equal to the search term
     if not found:
                 print("No books found with the title:", search)
#here we are creating a while loop that will run until the user chooses to exit the program
while True:
    #our main menu
    print("\n===== LIBRARY =====")
    print("1. Add Book") 
    print("2. View Books")
    print("3. search for books")
    print("4. Exit")

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
        print("Exiting the program...")
        break
    else:
        print("Invalid choice")
        print("Book added successfully!")
