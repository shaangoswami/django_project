# 📝 textUTILS - Django String Processor

**textUTILS** is a web-based utility tool built using the **Django** framework. It allows users to perform various text-manipulation tasks—such as removing punctuation, cleaning up extra spaces, and converting case—through a simple, interactive web interface.

---

## 📂 Project Structure & File Explanations

Django projects follow a specific structure. Here is a breakdown of what the key files in this repository do:

### 1. Root Directory
* **`manage.py`**: The main command-line utility. You use this to interact with your project (e.g., starting the server, creating apps, or migrating the database).
* **`db.sqlite3`**: This is your database file. Django uses SQLite by default, which stores all data in this single file.

### 2. Core Project Folder (`django_project/`)
This folder acts as the configuration hub for the entire website.
* **`settings.py`**: The configuration file for the project. It handles security keys, lists installed apps, manages middleware, and connects to the database.
* **`urls.py`**: The "table of contents" for your website. It maps specific URL paths (like `/analyze`) to the logic stored in `views.py`.
* **`wsgi.py` / `asgi.py`**: These files are entry points for web servers to serve your project once it is deployed to a live environment.

### 3. Application Folder (`myapp/`)
This is where the actual features of **textUTILS** live.
* **`views.py`**: **The Logic Center.** This file contains the Python functions that take the text input from the user, process it (remove spaces, punctuations, etc.), and send the result back to the browser.
* **`models.py`**: Used to define the database schema. While this project is a utility tool, this file is essential if you want to save user history or settings in the future.

### 4. Frontend (`templates/`)
* **HTML Files**: This folder contains the user interface. Django uses these templates to render the visual pages you see in your browser.

---

## 🚀 Key Features
* **Punctuation Remover:** Strips out symbols like `!, @, #, $`.
* **Full Uppercase:** Instantly converts all input text to capital letters.
* **New Line Remover:** Consolidates multi-line text into a single paragraph.
* **Extra Space Remover:** Fixes messy formatting by removing double or trailing spaces.

---

## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shaangoswami/django_project.git](https://github.com/shaangoswami/django_project.git)
2. **Navigate to the folder:**
   cd django_project
3. **Run the developement server**
   python manage.py runserver
4. **Access the app**
   Open your browser and go to http://127.0.0.1:8000/
   
PREVIEW

![textUTILS-com](https://github.com/user-attachments/assets/fa00416a-42ed-4948-86b3-620dad3ce5ac)

💻 Technologies Used
Backend: Python & Django
Frontend: HTML5, CSS3
