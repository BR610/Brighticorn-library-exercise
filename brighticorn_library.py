
books = ["Dune", "Pride and Prejudice"]


def menu():

    # Print welcome title
    print "Brighticorn's Books"
    print "-------------------"
    print "You can add/view/check/exit"
    command = raw_input("Please enter your choice:  ")
    print "Action: " + command

    command = command.lower()
    if command == "exit":
        print "goodbye!"

    elif command == "add":
        print "Add Book!"
        new_book = raw_input("Which book would you like to add? ")
        books.append(new_book)
        print "Added: {}".format(new_book)
        print books

    elif command == "view":
        print "View Book!"

    elif command == "check":
        print "Check for a Book!"

    else:
        print "Sorry, that is not a option of this program"

menu()
