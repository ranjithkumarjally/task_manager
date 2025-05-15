# Task Manager Web Application

A full-stack to-do list web application built with Flask, SQLite, and Bootstrap. Users can create, edit, delete, and filter tasks, with a responsive interface and cloud deployment on Render. This project demonstrates skills in Python web development, database management, and modern web technologies.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## Demo
- **Live Demo**: [Task Manager on Render](https://your-render-url.onrender.com)
- **GitHub Repository**: [github.com/your-username/task-manager](https://github.com/your-username/task-manager)

## Screenshots
### Homepage with Task List
![Task List](screenshots/task_list.png)
*View and manage tasks with filtering options.*

### Add Task Form
![Add Task](screenshots/add_task.png)
*Create a new task with title, description, priority, and deadline.*

### Edit Task Form
![Edit Task](screenshots/edit_task.png)
*Update existing task details.*

## Tech Stack
- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap, Jinja2
- **JavaScript**: Vanilla JavaScript (minimal)
- **Deployment**: Render, Gunicorn
- **Version Control**: Git, GitHub

## Features
- **Task Management**:
  - Add tasks with title (required), description (optional), priority (Low, Medium, High), and deadline (optional).
  - Edit or delete existing tasks.
  - Mark tasks as completed or incomplete.
- **Filtering**: Sort tasks by priority (Low, Medium, High) or completion status (Completed, Incomplete).
- **User Experience**:
  - Responsive design with Bootstrap for mobile and desktop compatibility.
  - Flash messages for feedback (e.g., "Task added successfully!").
  - Form validation to ensure data integrity.
- **Deployment**: Hosted on Render with a public URL, using Gunicorn for production.
- **Modular Code**: Clean project structure with separate models, templates, and static files.

## Installation
Follow these steps to run the app locally.

### Prerequisites
- Python 3.8 or higher ([Download](https://www.python.org/downloads/))
- Git ([Install](https://git-scm.com/downloads))
- A terminal (e.g., Command Prompt, Terminal, or VS Code)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   python app.py
   ```

5. **Access the App**:
   - Open `http://127.0.0.1:5000` in a web browser.
   - Create, edit, or filter tasks to test the app.

## Usage
- **Add a Task**: Fill out the form on the homepage with a title, optional description, priority, and deadline, then click "Add Task."
- **Edit a Task**: Click "Edit" next to a task, update details, and save.
- **Delete a Task**: Click "Delete" (with confirmation) to remove a task.
- **Mark as Completed**: Click "Toggle" to change a task’s completion status.
- **Filter Tasks**: Use the dropdowns to filter by priority or status.

## Deployment
To deploy the app to Render for a public URL:

1. **Push to GitHub**:
   - Ensure your code is in a GitHub repository.
   - Include a `.gitignore` file to exclude `venv/` and `tasks.db`.

2. **Create a Render Account**:
   - Sign up at [render.com](https://render.com) with GitHub.
   - Create a new Web Service and connect your repository.

3. **Configure Render**:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variable**: `SECRET_KEY=your-secure-key`
   - **Instance Type**: Free

4. **Deploy**:
   - Click "Create Web Service" to build and deploy.
   - Access the app via the provided URL (e.g., `https://your-render-url.onrender.com`).

**Note**: SQLite may reset on Render restarts. For production, consider using PostgreSQL.

## Project Structure
```
task_manager/
├── app.py                # Main Flask app with routes
├── models/
│   └── task.py           # Task model for database
├── templates/
│   ├── base.html         # Base template with layout
│   ├── index.html        # Homepage with task list
│   └── edit.html         # Edit task form
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── script.js     # JavaScript for interactivity
├── requirements.txt      # Dependencies
├── .gitignore            # Files to ignore in Git
├── README.md             # Project documentation
└── LICENSE               # License file
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-name`).
5. Open a pull request with a description of your changes.

Please ensure code follows PEP 8 style guidelines and includes comments.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
- **Name**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [your-username](https://github.com/your-username)
- **LinkedIn**: [your-linkedin-profile](https://linkedin.com/in/your-profile)

Feel free to reach out with questions or suggestions!