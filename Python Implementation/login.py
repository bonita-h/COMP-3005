import defs

def logMenu(cursor):
    run = True
    while(run):
        option = input("'Login'(1) or 'Create New Account'(2): ")
        if(option == '1'):
            userLogin(cursor)
            run = False
        elif(option == '2'):
            createNewAccount(cursor)
            run = False
        else:
            print("No number input")
###



#global variables
isAdmin = False
#login
def userLogin(cursor):
    #get user input
    username = input("Enter username: ")
    password = input("Enter password: ")
    #search in database for user login info
    cursor.execute("SELECT username, password, admin FROM login")
    record = cursor.fetchall()
    isExists = False
    for r in record:
        if(r[0]==username and r[1]==password):
            defs.loggedInUsername = username
            isExists = True
            defs.isAdmin = r[2] #check whether user is admin(true) or client(false)
    #if user is found
    if(isExists):
            print("Successful login")
            if(defs.isAdmin):
                print("Hello ADMIN")
    else:
        print("Unccessful login - user does not exists or error in input")
        userLogin() #have user try again
###




def createNewAccount(cursor): #allows user to create new account and add to database
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    email   =  input("Enter email: ")
    address =  input("Enter address: ")
    admin = False
    if(input("Are you an admin? (y/n) ") == 'y'):
        defs.isAdmin = True
    bankID  =  input("Enter bank account ID: ")
    balance =  float(input("Enter bank balance: "))
    #assume everything is input and correct, add to database
    #add to bank
    cursor.execute("INSERT INTO bank (bankAccountID, balance) VALUES (%s, %s)", (bankID, balance))
    #add to login
    cursor.execute("INSERT INTO login (username, password, email, address, admin, bankAccountID) VALUES (%s, %s, %s, %s, %s, %s)", (username, password, email, address, admin, bankID))
    #if successful
    print("New Account Created")
    defs.loggedInUsername = username





