import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

def menu():
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
            
            

def displayAll():
    for row in cursor.execute("SELECT * FROM tblFilms"):
        print(row)

menu()
cursor.close
conn.close