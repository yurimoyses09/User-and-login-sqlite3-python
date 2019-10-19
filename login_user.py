import sqlite3
import sys
from sqlite3 import Error
import getpass  # Oculta o que o usuario digita (senha)

login = globals
password = globals

try:
    conn = sqlite3.connect("Usernames_CLI.db")
    cursor = conn.cursor()
    # Cria uma tabela
    cursor.execute("""CREATE TABLE Users
             (Name of the user text, Login text,
              Password text)
                """)

except Error:
    print(Error)
finally:
    conn.close

create = str(input("\nDo you create new count? [y/n]: "))
if create == 'y':  # Usuario ja possui uma conta
    name = str(input("Your name: "))
    login = input("Create new login: ")
    password = getpass.getpass("Create new password: ")
    for n in range(0, 5):
        password_ = getpass.getpass("\nType the password again:")
        if password == password_:
            break
        elif password != password_:
            print("\nPasswords are not the same!!")
        elif n == 5:
            print("\nClosing program")
            sys.exit()
    cursor.execute("""INSERT INTO Users VALUES(?,?,?)""",
                   (name, login, password))
    print("Registered user.")
    conn.commit()

else:
    have = str(input("Do you already have an account? [y/n]: "))
    if have == 'y':
        login_ = input("Login: ")
        password_ = getpass.getpass(("Password: "))
        conn = sqlite3.connect("Usernames_CLI.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Users""")
        # Percorre o banco procura se existe os dados
        for row in cursor.fetchall():
            print(row)
        conn.close()
