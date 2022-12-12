import defs

foundBook = []
clientCart = []

def searchForBook(cursor):
    userInput = input("Enter book title to search: ")
    cursor.execute("SELECT * FROM book")
    record = cursor.fetchall()
    for r in record:
        if(r[1] == userInput):
            print("[", len(foundBook)+1, "] ", r[1], " written by", r[2], " Quantity:", r[4], "Price: $", r[5])
            foundBook.append(r) #get all found books
    #if any books found or not
    #print(foundBook[0][0])
    if(len(foundBook) < 0):
        #print(foundBook)
    #else:
        print("no book found")

    else:
        addCart(cursor)


def addCart(cursor):
    run = True
    username = defs.loggedInUsername
    while(run):
        option = int(input("Enter book number to add (enter 0 to exit and ship order): "))
        if(option <= 0):
            run = False
            break
        #assume number entered is correct
        book = foundBook[option-1]
        cursor.execute("INSERT INTO checkout (orderID, username, ISBN, title, price, quantity) VALUES (DEFAULT, %s, %s, %s, %s, %s)", (username, book[0], book[1], book[5], 1))
        print("Book added to cart")
    #when user would like to exit
    #order(cursor)



def order(cursor):
    username = defs.loggedInUsername
    #print(type(username))
    #print("YOUR CART: ")
    sql = "SELECT ISBN, title, price FROM checkout WHERE username = %s"
    cursor.execute(sql, (username,))
    record = cursor.fetchall()
    #for r in record:
    #    print(r)
    print("ODERING INFO")
    ship_address = input("Enter shipping address: ")
    bill_address = input("Enter billing address: ")
    ship_status = "Not Shipped"
    #record = cursor.fetchall()
    for r in record:
        cursor.execute("INSERT INTO client_order (orderID, username, ship_address, bill_address, progress, ISBN, price) VALUES (DEFAULT, %s, %s, %s, %s, %s, %s)", (defs.loggedInUsername, ship_address, bill_address, ship_status, r[0], r[2]))
    print("Thank you for shopping Look Inna Book")