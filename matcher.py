import sqlite3


conn = sqlite3.connect("school.db") # connection == creation of db
cursor = conn.cursor() # cursor to handle db writing and selection
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students 
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        age INTEGER,
        grades REAL,
        interests TEXT
        )
                """)

# cursor.execute("INSERT INTO students (name, surname, age, grades, interests)  VALUES (?,?,?,?,?)",
#               ("Teodor","Taran", 11, 100, "judo")
#              )
conn.commit()

cursor.execute("SELECT * FROM students")
row = cursor.fetchall()
for r in row:
    print(r)

conn.close()


# def menu():
#     print("1. Get coordinates")
#     print("2. Get current weather")
#     print("3. Suggest clothing")
#     print("4. Get weekly forecast")
#     print("5. Export database to CSV")
#     print("6. Choose another city")
#     print("0. Exit")
#
# def handle_choice(choice):
#     match choice:
#         case 1: print("Get coordinates")
#         case 2: print("Get current weather")
#         case 3: print("Suggest clothing")
#         case 4: print("Get weekly forecast")
#         case 5: print("Export database to CSV")
#         case 6: print("Choose another city")
#         case 0: print("Exit")
#         case _: print("Invalid choice. Please choose a number between 0-6.")
#
# while True:
#     menu()
#     choice = input("Choose an option (0-6): ")
#     handle_choice(choice)
#
# dispatcher = {
#     "1": lambda: print("Get coordinates"),
#     "2": lambda: print("Get current weather"),
#     "3": lambda: print("Suggest clothing"),
#     "4": lambda: print("Get weekly forecast"),
#     "5": lambda: print("Export database to CSV"),
#     "6": lambda: print("Choose another city"),
#     "0": lambda: print("Exit")
# }