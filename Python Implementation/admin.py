def viewUsers(cursor):
    print("All users registered with the book store")
    cursor.execute("SELECT * FROM login")
    record = cursor.fetchall()
    for r in record:
        print("username:", r[0], "email:", r[2], "address:", r[3], "admin:", r[4])


def viewPublishers(cursor):
    print("All publishers available in book store")
    cursor.execute("SELECT * FROM publisher")
    record = cursor.fetchall()
    for r in record:
        print("ID:", r[0], "name:", r[1], "email:", r[3], "phone number:", r[4])