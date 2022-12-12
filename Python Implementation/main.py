import psycopg2
from psycopg2 import Error

import defs
from login import *
from checkout import *
from admin import *

#for testing
#username: new
#password: new
#email: new@email.com 
#address: address
#Admin: y
#bankID: 1006
#balance: 50.2


try:
    #connect to an existing database
    connection = psycopg2.connect(
        user = "postgres",
        password = "5541166414", #password used to login into pgAdmin
        #host = "", 
        #port = "", 
        database = "comp3005") 

    #create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    #print("PostgreSQL server information")
    #print(connection.get_dsn_parameters(), "\n")

    # Executing a SQL query
    #cursor.execute("SELECT version();")
    #cursor.execute("INSERT INTO bank (bankAccountID, balance) VALUES ('10005', '200')")
    #cursor.execute("SELECT bankAccountID, balance FROM bank")

    # Fetch result
    #record = cursor.fetchone()
    #record = cursor.fetchall()

    #for r in record:
        #print("bankAccountID: ", r[0], " banalce: ", r[1])
        #print("this type is: ", type(r[1]))
    #print("You are connected to - ", record, "\n")

    #   RUNNING PROGRAM
    #login
    logMenu(cursor)
    connection.commit()
    run = True
    while(run and defs.isAdmin == False): #if user
        print("     Exit [0]")
        print("     Search for a book by title [1]")
        print("     Add/Look at current cart [2]")
        print("     Checkout [3]")
        option = input("What would you like to view? ")
        if(option == "0"):
            run = False
        if(option == "1"):
            searchForBook(cursor)
        if(option == "2"):
            addCart(cursor)
        if(option == "3"):
            order(cursor)
        connection.commit()

    while(run and defs.isAdmin == True): #if admin
        print("     Exit[0]")
        print("     View Users [1]")
        print("     View Publishers [2]")
        option = input("What would you like to view? ")
        if(option == "0"):
            run = False
        if(option == "1"):
            viewUsers(cursor)
        if(option == "2"):
            viewPublishers(cursor)


    #when adding or deleting from database, commit the transaction
    connection.commit()
    #close cursor to prevent leak
    cursor.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")