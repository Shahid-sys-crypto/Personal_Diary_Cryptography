# 🔐 Personal Diary with Cryptography (Python)

A secure **Personal Diary application** built using **Python** that allows users to write, store, and read diary entries in **encrypted form**.  
It uses **Fernet symmetric encryption** to protect diary content and basic password authentication for access control.

---

## ✨ Features

- 📝 Create encrypted diary entries
- 🔒 Encrypts and decrypts diary content automatically
- 📂 Stores entries securely in a local folder
- 📄 Lists all saved diary entries
- 🔑 Password-based authentication
- 🕒 Timestamped diary entries
- 🧑‍💻 Command-line interface

---

## 📁 Project Structure

Personal_Diary_Cryptography.py
secret.key
entries/
│ ├── 2026-02-04_title.txt
README.md


---

## 🛠️ Requirements

- Python **3.x**
- `cryptography` library

Install the required library using:
pip install cryptography


---

## ▶️ How to Run

1. Download or clone the project
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:

python Personal_Diary_Cryptography.py


5. Enter the password to access the diary

---

## 🧠 How It Works

### Encryption System

- A secret key is generated once and stored in `secret.key`
- Diary content is encrypted using **Fernet encryption**
- Encrypted text is stored as binary data
- Content is decrypted only when reading an entry

### Diary Entries

- Each entry is saved with:
  - Timestamp
  - Title
- Entries are stored in the `entries/` directory

### Authentication

- User must enter the correct password to access the diary
- Uses `getpass` to hide password input

---

## 🔘 Menu Options

1. **Create a new entry** – Write and save encrypted diary content  
2. **View all entries** – List stored diary files  
3. **Read an entry** – Decrypt and display selected entry  
4. **Exit** – Close the application  

---

## 🔐 Security Notes

- Diary content is encrypted, not plain text
- `secret.key` must be kept safe
- Password is hardcoded (for learning purposes)

---

## 🚀 Future Enhancements

- Hash-based password storage
- Change password feature
- Search diary entries
- GUI version using Tkinter
- Cloud backup support

---

## 👤 Author

**Shahid Farhan**  
Python mini-project demonstrating file handling and cryptography.
