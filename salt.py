import hashlib
import random
import string

def generate_salt(length=8):
    salt_characters=string.ascii_letters + string.digits + string.punctuation
    salt=''.join(random.choice(salt_characters) for _ in range(length))
    return salt

def hash_password(password, salt):
    salted_password=password + salt
    hash_object=hashlib.sha256()
    hash_object.update(salted_password.encode('utf-8')) 
    hashed_password=hash_object.hexdigest()
    return hashed_password

def check_password(password, hashed_password, salt):
    salted_password=password+salt
    hash_object=hashlib.sha256()
    hash_object.update(salted_password.encode("utf-8"))
    hashed_input_password=hash_object.hexdigest()
    return hashed_password==hashed_input_password

password_file = {}
num_users = int(input("Enter the number of users: "))
for i in range(num_users):
    username = input(f"Enter the username for User{i+1}:")
    password = input(f"Enter the password for User{i+1}: ") 
    password_file[username] = password

hashed_password_file = {}
for username, password in password_file.items():
    salt=generate_salt()
    hashed_password=hash_password(password, salt)
    hashed_password_file[username]={"hashed_password": hashed_password, 'salt':salt}

with open("hashed_passwords.txt", 'w') as file:
    for username, data in hashed_password_file.items():
        file.write(f"{username}:{data['hashed_password']}:{data['salt']}\n")

username=input("Enter username: ")
password=input("Enter password: ")

hashed_password = None
salt = None
with open('hashed_passwords.txt', 'r') as file:
    for line in file:
        stored_username, stored_hashed_password, stored_salt=line.strip().split(":")
        if stored_username==username:
            hashed_password = stored_hashed_password
            salt=stored_salt
            break

if hashed_password is not None and salt is not None:
    if check_password(password, hashed_password, salt):
        print("Login successful.")
    else:
        print("Login failed. Invalid username or password.")
else:
    print("Login failed. Invalid username or password.")
