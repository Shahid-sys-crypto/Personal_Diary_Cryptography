import os
import getpass
from datetime import datetime
from cryptography.fernet import Fernet

def generate_key():
    if not os.path.exists("secret.key"):
        key=Fernet.generate_key()
        with open("secret.key","wb") as key_file:
            key_file.write(key)
def load_key():
    return open("secret.key","rb").read()
def encrypt_text(text):
    key=load_key()
    cipher=Fernet(key)
    return cipher.encrypt(text.encode())
def decrypt_text(encrypted_text):
    key=load_key()
    cipher=Fernet(key)
    return cipher.decrypt(encrypted_text).decode()
def create_entry():
    title=input("enter the title of your dairy entry:")
    content=input("enter your diary content")
    date=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    encrypted_content=encrypt_text(content)
    os.makedirs("entries",exist_ok=True)
    file_name=f"{date}_{title}.txt"
    with open(os.path.join("entries",file_name),"wb") as file:
        file.write(encrypted_content)
    print(f"diary entry '{title}' saved successfully")
def list_entries():
    os.makedirs("entries",exist_ok=True)
    entries=os.listdir("entries")
    if entries:
        print("your diary entries")
        for index,entry in enumerate(entries,start=1):
            print(f"{index}.{entry}")
    else:
        print("no diary entries found")
def read_entry():
    list_entries()
    file_name=input("enter the name of the entry to read")
    file_path=os.path.join("entries",file_name)
    try:
        with open(file_path,"rb") as file:
            encrypted_content=file.read()
        content=decrypt_text(encrypted_content)
        print("\n diary entry content")
        print(content)
    except FileNotFoundError:
        print("entry not found")
def authenticate():
    correct_password="password"
    password=getpass.getpass("enter your password")
    if password==correct_password:
        print("access granted")
        return True
    else:
        print("access denied")
        return False
def main():
    generate_key()
    if authenticate():
        while True:
            print("\n options")
            print("1.create a new entry")
            print("2.view all entrires")
            print("3.read an entry")
            print("4.exit")
            choice=input("enter your choice")
            if choice=="1":
                create_entry()
            elif choice=="2":
                list_entries()
            elif choice=="3":
                read_entry()
            elif choice=="4":
                print("goodbye")
                break
            else:
                print("invalid choice,please try again")
if __name__=="__main__":
    main()