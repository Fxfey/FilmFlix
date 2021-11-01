import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

def menu():
    choice = 0
    while choice not in [1,2,3,4,5]:
        print("\nDisplay Menu")
        print("1 - Print All")
        print("2 - Add a Record")
        print("3 - Update a Record")
        print("4 - Delete a Record")
        print("5 - Exit")
        choice = int(input("Choice: "))

    else:
        if choice == 1:
            displayAll()
        
        elif choice == 2:
            addRecord()

        elif choice == 3:
            updateRecord()

        elif choice == 4:
            deleteRecord()

        elif choice == 5:
            print("Now Exiting.")



def displayAll():
    for row in cursor.execute("SELECT * FROM tblFilms"):
        print(row)



def addRecord():
    print("To add a record you will need the following details:")
    print("Title - Year - Rating - Runtime (minutes) - Genre")

    title = str(input("Title: "))
    year = str(input("Year: "))
    rating = str(input("Rating: "))
    runtime = str(input("Runtime: "))
    genre = str(input("Genre: "))

    for row in cursor.execute("SELECT * FROM tblFilms ORDER BY filmIDESC LIMIT 1"):
        filler = ''

    cursor.execute(f"insert into tblFilms (`filmID`,`title`yearReleased`,`rating`,`duration`,`genre`) Values ('{row[0]+1}'{title}','{year}','{rating}','{runtime}','{genre}');")

    conn.commit()

def updateRecord():
    print("To update a record you will need to know its ID")
            
    alterID = int(input("Enter the ID you would like to alter: "))
    title = str(input("Title: "))
    year = str(input("Year: "))
    rating = str(input("Rating: "))
    runtime = str(input("Runtime: "))
    genre = str(input("Genre: "))

    cursor.execute(f"UPDATE tblFilms SET title = '{title}', yearRelease= '{year}', rating = '{rating}', duration = '{runtime}', genre ={genre}' WHERE filmID = {alterID};")

    conn.commit()

def deleteRecord():
    deleted = int(input('Please enter the ID of the film you want to delete: '))

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {deleted};")

    conn.commit()


menu()
cursor.close
conn.close