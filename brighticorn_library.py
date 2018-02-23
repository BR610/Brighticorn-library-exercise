
books = ["Dune", "Pride and Prejudice"]


def menu():

    # Print welcome title
    print "Brighticorn's Books"
    print "-------------------"
    print "You can add/view/check/exit"
    #command = raw_input("Please enter your choice: ")
    #print "Action: " + command

    #command = command.lower()
    while True:
        command = raw_input("Please enter your choice: ")
        command = command.lower()
        print "Action: " + command

        if command == "exit":
            print "goodbye!"
            return

        if command == "add":
            print "Add Book!"
            new_book = raw_input("Which book would you like to add? ")
            books.append(new_book)
            print "Added: {}".format(new_book)
            print books

        elif command == "view":
            print "View Book!"
            for book in books:
                print book
            '''i = 0
            while i < len(books):
                print books[i]
                i = i + 1'''

        elif command == "check":
            print "Check for a Book!"
            to_check = raw_input("Which book would you like to check the library for? ")

            if to_check in books:
                print "Found {} in the library! ".format(to_check)
            else:
                print "{} not found. ".format(to_check)

        else:
            print "Sorry, that is not a option of this program"

menu()
