# Task Manager Web App

A simple to-do list web application built with Python and Flask. Users can add, edit, delete, and mark tasks as completed. This is my beginner project to learn full-stack web development, and it’s hosted online using Render.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.2-green)

## About the Project
This app lets you manage tasks easily. You can:
- Add tasks with a title, description, priority (Low, Medium, High), and deadline.
- Edit or delete tasks.
- Mark tasks as done or not done.
- View all tasks in a clean, mobile-friendly interface.

I built this to practice Python, web development, and deploying an app online.

## Screenshot
![Task List](screenshots/task_list.png)  
*The homepage shows your tasks and a form to add new ones.*

## Technologies Used
- **Python** and **Flask** for the backend (server).
- **SQLite** for storing tasks.
- **HTML**, **CSS**, and **Bootstrap** for the frontend (webpages).
- **Render** for hosting the app online.

## How to Run Locally
1. **Install Python** (3.8 or higher) from [python.org](https://www.python.org/downloads/).
2. **Clone the project**:
   ```bash
   git clone https://github.com/ranjithkumarjally/task_manager.git
   cd task_manager
   ```
3. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install required tools**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the app**:
   ```bash
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in a browser to use the app.

## Project Structure
- `app.py`: Main app code.
- `models/task.py`: Defines how tasks are stored.
- `templates/`: HTML pages for the app.
- `static/`: CSS and JavaScript for styling and interactivity.
- `requirements.txt`: List of tools needed.
- `.gitignore`: Ignores unnecessary files.


## Contact
- **Name**: Ranjith Kumar Jally
- **Email**: [iamranjithjally@gmail.com]
- **GitHub**: [ranjithkumarjally](https://github.com/ranjithkumarjally)

Thanks for checking out my project!