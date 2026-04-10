book = ["DSA", "Java", "CSS", "Html"]

def catalogue():
    print("---Choose an option---")
    print("1.Insert a book in the catalogue")
    print("2.Insert a book in desired position")
    print("3.Remove a book from the catalogue")
    print("4.Remove all books in catalogue")
    print("5.Display the catalogue")
    print("6.Exit") 

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("The books already saved in catalogue:", book)
            new = input("Enter the name of book: ")
            book.append(new)
            print("The books saved in catalogue:", book)
            catalogue()

        case 2:
            print("The books already saved in catalogue:", book)
            new = input("Enter the name of book: ")
            pos = int(input("Enter the position: "))
            book.insert(pos - 1, new)
            print("The book saved in the desired position:", book)
            catalogue()
        
        case 3:
            print("The books already saved in catalogue:", book)
            pos = int(input("Enter the position of the book in catalogue: "))
            book.pop(pos - 1)
            print("The book has been removed:", book)
            catalogue()

        case 4:
            book.clear()
            print("Catalogue cleared.")
            new = input("Enter a new book: ")
            book.append(new)
            print("The books saved in catalogue:", book)
            catalogue()

        case 5:
            print("The books saved in the catalogue:", book)
            catalogue()

        case 6:
            print("Exited")
            return   # ✅ IMPORTANT: stop recursion

        case _:
            print("Invalid choice, please try again")
            catalogue()

catalogue()