# 🔐 Cryptography Toolkit for Secure Data Management

A Python-based command-line cryptography toolkit that provides secure file encryption, password management, and image steganography. This project demonstrates practical applications of cryptography and data protection using a simple interactive menu.

---

## 📖 Overview

The **Cryptography Toolkit for Secure Data Management** is designed to help users protect sensitive information through encryption and secure storage techniques. The toolkit combines multiple security utilities into a single command-line application, making it suitable for educational purposes, cybersecurity practice, and personal data protection.

The application allows users to:

* Encrypt files with a password
* Decrypt encrypted files
* Store and retrieve credentials securely
* Hide secret messages inside images
* Extract hidden messages from images

---

## ✨ Features

* 🔒 Password-based file encryption
* 🔓 Secure file decryption
* 🔑 Password manager for storing credentials
* 🖼️ Image steganography for hiding messages
* 📩 Extract hidden messages from images
* Interactive command-line interface
* Modular Python implementation

---

## 📂 Project Structure

```text
Cryptography-Toolkit-for-Secure-Data-Management/
│
├── main.py
├── crypto_utils.py
├── password_manager.py
├── steganography.py
├── requirements.txt
├── README.md
└── LICENSE
```

### Module Description

| File                  | Description                                |
| --------------------- | ------------------------------------------ |
| `main.py`             | Main application with interactive CLI menu |
| `crypto_utils.py`     | Handles file encryption and decryption     |
| `password_manager.py` | Secure password vault implementation       |
| `steganography.py`    | Hide and extract messages from images      |

---

## ⚙️ Functionality

### 1. File Encryption

Encrypt any supported file using a user-provided password.

**Workflow**

* Enter input file
* Enter output file name
* Enter password
* Encrypted file is generated

---

### 2. File Decryption

Decrypt previously encrypted files using the correct password.

**Workflow**

* Select encrypted file
* Choose output file
* Enter password
* Original file is restored

---

### 3. Password Manager

Securely manage login credentials using a master password.

Available operations:

* Add new account
* Retrieve stored credentials
* List saved services

Example:

```
Master Password
    │
    ▼
Password Manager
    ├── Add Entry
    ├── Get Entry
    └── List Services
```

Each entry contains:

* Service Name
* Username
* Password

---

### 4. Hide Message in Image

Uses image steganography to embed a secret message inside an image.

Workflow:

1. Select image
2. Enter secret message
3. Save output image

The resulting image appears visually unchanged while containing the hidden message.

---

### 5. Extract Hidden Message

Reads an encoded image and extracts the embedded secret message.

Workflow:

1. Select encoded image
2. Hidden message is displayed

---

## 🖥️ Command-Line Menu

```
=== Cryptography Toolkit ===

1. Encrypt File
2. Decrypt File
3. Password Manager
4. Hide Message in Image
5. Extract Message from Image
6. Exit
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/HBR2055/Cryptography-Toolkit-for-Secure-Data-Management.git
```

### Navigate to the Project

```bash
cd Cryptography-Toolkit-for-Secure-Data-Management
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

---

## 💡 Example Usage

### Encrypt a File

```
Choice: 1

Input file:
document.pdf

Output file:
document.enc

Password:
********
```

---

### Decrypt a File

```
Choice: 2

Encrypted file:
document.enc

Output file:
document.pdf

Password:
********
```

---

### Password Manager

```
Choice: 3

Master Password:
********

1. Add Entry
2. Get Entry
3. List Services
```

---

### Hide a Secret Message

```
Choice: 4

Image:
image.png

Message:
Confidential Information

Output:
secret_image.png
```

---

### Extract Hidden Message

```
Choice: 5

Image:
secret_image.png

Hidden Message:
Confidential Information
```

---

## 🛠 Technologies Used

* Python 3
* File Encryption
* Password-Based Security
* Image Steganography
* Command-Line Interface (CLI)

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* File Encryption
* File Decryption
* Password-Based Authentication
* Secure Credential Storage
* Image Steganography
* Modular Python Programming
* Secure Data Management

---

## ⚠️ Disclaimer

This project is intended for educational purposes and cybersecurity practice. It demonstrates cryptographic techniques and secure data management concepts. It should not be relied upon for protecting highly sensitive or production-critical information without additional security review and testing.

---

## 👨‍💻 Author

**(HBR2055)**

Cybersecurity Enthusiast | Information Technology Graduate

GitHub: https://github.com/HBR2055

---

## ⭐ Support

If you found this project useful:

* Star ⭐ the repository
* Fork 🍴 the project
* Report issues
* Submit improvements through Pull Requests

Contributions are always welcome.
