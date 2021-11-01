import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

def menu():
    choice = 0
    while choice not in [1,2,3]:
        print("\nWelcome to FilmFlix")
        print("1 - Display Menu")
        print("2 - Editor Menu")
        print("3 - Exit")
        choice = int(input("Choice: "))
    else:
        if choice == 1:
            disMenu()
        elif choice == 2:
            altMenu()
        elif choice == 3:
            print("Now Exiting.")

def disMenu():
    choice = 0
    while choice not in [1,2,3,4]:
        print("\nDisplay Menu")
        print("1 - Print All")
        print("2 - Print Specific Genre")
        print("3 - Print Specific Rating")
        print("4 - To Exit")
        choice = int(input("Choice: "))
    else:
        if choice == 1:
            displayAll()

        elif choice == 2:
            genre = ''
            while genre not in ['Comedy','Action','Crime','Animation','Fantasy','Fighting']:
                print("The Genres available are")
                print('Comedy - Action - Crime - Animation - Fantasy - Fighting')
                genre = input("Choice: ")
            else:
                if genre != '':
                    for row in cursor.execute(f"\nSELECT * FROM tblFilms WHERE genre='{genre}'"):
                        print(row)

        elif choice == 3:
            rating = ''
            while rating not in ['PG','G','R']:
                print("The Ratings available are")
                print('PG - G - R')
                rating = input("Choice: ")
            else:
                if rating != '':
                    for row in cursor.execute(f"\nSELECT * FROM tblFilms WHERE rating='{rating}'"):
                        print(row)
        
        elif choice == 4:
            print("Now Exiting.")

def altMenu():
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

    title = input("Title: ")
    year = input("Year: ")
    rating = input("Rating: ")
    runtime = input("Runtime: ")
    genre = input("Genre: ")

    for row in cursor.execute("SELECT * FROM tblFilms ORDER BY filmID DESC LIMIT 1"):
        filler = ''

    cursor.execute(f"insert into tblFilms (`filmID`,`title`,`yearReleased`,`rating`,`duration`,`genre`) Values ('{row[0]+1}','{title}','{year}','{rating}','{runtime}','{genre}');")

    conn.commit()
    

def updateRecord():
    print("To update a record you will need to know its ID")
            
    alterID = int(input("Enter the ID you would like to alter: "))
    title = str(input("Title: "))
    year = str(input("Year: "))
    rating = str(input("Rating: "))
    runtime = str(input("Runtime: "))
    genre = str(input("Genre: "))

    cursor.execute(f"UPDATE tblFilms SET title = '{title}', yearReleased= '{year}', rating = '{rating}', duration = '{runtime}', genre ='{genre}' WHERE filmID = {alterID};")

    conn.commit()

def deleteRecord():
    deleted = int(input('Please enter the ID of the film you want to delete: '))

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {deleted};")

    conn.commit()
            
            

def displayAll():
    for row in cursor.execute("SELECT * FROM tblFilms"):
        print(row)

menu()
cursor.close
conn.close