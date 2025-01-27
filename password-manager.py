"""
In this project we will Create, Read, Update & Delete the passwords and encrypt them and then store them in a text file.
Although, it is not a good idea to store it in a text file and we should do it in a DataBase for the better security. 
This is just a project for practice, where I have used the text file for the same.
"""

from cryptography.fernet import Fernet

# encrypting the password (use only one time for extracting the key)
"""
def write_key() :
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""

# write_key()

# decrypting the password
def load_key() :
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Dummy access for master user
while True:
    master_user = str(input("What is your name?: "))
    master_pwd = str(input("What is your master password?: "))

    if master_user == "Anthony Stark" and master_pwd == "I am Iron Man" :
        print("Hello Sir, I am J.A.R.V.I.S your personal AI assistant it is nice to have you back. Your systems are ready to do the operations.")
        break
    else :
        print("Invalid User, Try Again")
        continue

key = load_key() + master_pwd.encode()
fer = Fernet(key)    

# view function
def view_password() :
    with open("passwords.txt", "r") as f:
        for line in f.readlines():            
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, | Password: {fer.decrypt(passw.encode()).decode()}")


# add function
def add_password() :
    name = str(input("Account Name: "))
    pwd = str(input("Password: "))

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")

# For the master user
while True :

    mode = str(input("Would you like to add a new password or view the existing ones (A for Add || V for View)? or press Q to quit: ").lower())
    
    if mode == "q" :
        break
    elif mode == "v" :
        view_password()
    elif mode == "a" :
        add_password()
    else :
        print("Invalid Mode")
        continue