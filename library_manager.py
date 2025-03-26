#project = Personal Library Manager 
# A library management system keep track of the book present in the library . it is an important piece of software whichis a must a school and colleges 

book_list = list ()
#menu items 
menu = """
1) Add Book 
2) Remove Book 
3) View book 
4) press E to Exit 
"""  

def add_book(booklist,book):
    booklist.append(book)
    print("book added sucessfully")

def remove_book (booklist,book):
    if book in booklist:
        booklist.remove(book)
        print("book remove sucessfully")
    else:
        print("book not found in this list ")

#display all book result 
def display_list(booklist):
    if booklist:
        print("added book ->",",". join(booklist))
    else:
        print("no book in the list.") 

#exist program 
def exist_program():
    print("thank you for visiting the book library system.")
    quit()


#main program loop 
while True:
    print (menu)
    choice = input("your choice : ")

    if choice == "1": 
        book_name = input ("enter the book name to add: ")
        add_book(book_list, book_name)

    elif choice == "2":
        book_name = input ("enter the book name to remove: ")
        remove_book(book_list, book_name)
    
    elif choice == "3":
        display_list(book_list)

    elif choice.lower() == "e":
        exist_program()

    else:
        print("invalid entry")
        input("press enter to return to the main menu ")