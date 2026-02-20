# Real-Time Individual Chat Application

**Built with Django (MVT) + Django Channels (WebSocket)**

---

## 📌 Project Overview

This is a real-time one-to-one chat application built using **Django MVT architecture** and **Django Channels** for WebSocket communication.
It supports authenticated messaging, online presence tracking, read receipts, and message persistence.

---

## 🚀 Tech Stack (As Required)

* Python 3.x
* Django 4.2
* Django Channels 4
* SQLite (default DB)
* HTML, CSS, JavaScript
* Bootstrap 5 (UI Styling)

---

## ✅ Features Implemented

### Authentication

* User Registration (Email-based login)
* Secure Login / Logout
* Custom User Model
* Only authenticated users can access chat

### Real-Time Chat

* WebSocket-based private messaging
* Messages saved to database
* Instant delivery without refresh
* Auto-scroll to latest message

### Presence System

* Online indicator (🟢)
* Last seen timestamp when offline

### Message Features

* ✓ Sent indicator
* ✓✓ Read indicator (when chat opened)
* Prevent empty messages
* Message history loading

### Bonus Features

* Typing indicator (`User is typing...`)
* Unread message count badge

---

## 🏗️ Architecture (Strict MVT Followed)

| Layer    | Responsibility                           |
| -------- | ---------------------------------------- |
| Model    | Database schema (CustomUser, Message)    |
| View     | Handles HTTP requests and context        |
| Template | UI Rendering only (No business logic)    |
| Consumer | WebSocket handling (real-time messaging) |

---

## 📂 Project Structure

```
chat_app/
│
├── accounts/            # Custom user + authentication
├── chat/                # Chat logic + WebSocket consumer
├── templates/           # HTML UI
├── chat_app/            # Settings & ASGI config
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd chat_app
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate      (Windows)
source venv/bin/activate   (Mac/Linux)
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

If `requirements.txt` not available:

```
pip install django==4.2 channels==4.0 daphne==4.0
```

---

### 4️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```
python manage.py createsuperuser
```

---

### 6️⃣ Run Development Server

```
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 🧪 How to Test the Chat

1. Register **two different users**
2. Login in:

   * Browser Window → User1
   * Incognito Window → User2
3. Open chat between them
4. Send messages → Real-time updates
5. Close one tab → Last seen updates

---

## 🔐 Security Implementations

* Authenticated WebSocket connection only
* CSRF-protected forms
* Validation for duplicate users
* Prevent empty messages
* No logic inside templates (MVT enforced)

---

## 📦 Database

Using SQLite (`db.sqlite3`) for simplicity as required.

---

## 📽️ (Optional Submission)

Include:

* GitHub Repository Link
* Test Credentials
* Screen Recording (if required)

---

## 👤 Sample Test Credentials

| Email                                     | Password |
| ----------------------------------------- | -------- |
| [test1@gmail.com](mailto:test1@gmail.com) | 1234     |
| [test2@gmail.com](mailto:test2@gmail.com) | 1234     |

---

## 🎯 Evaluation Criteria Covered

✔ Clean MVT Structure
✔ Proper WebSocket Handling
✔ Authentication Security
✔ Online Presence Accuracy
✔ Read Receipts
✔ Maintainable Code Structure

---

## 👨‍💻 Author

Developed as part of technical evaluation task using Django Channels.

---
