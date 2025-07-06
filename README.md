# CollegeHub (Flask + Bootstrap)

A simple, intuitive College Management System built with:

* **Flask** (Python Backend)
* **Bootstrap 5** (Frontend Styling)
* **HTML & JavaScript (Fetch API)**
* **JSON files** (Data Persistence)

---

## 🎯 Features

* **Manage** Courses, Students, and Lecturers
* **Add** and **View** records via web forms
* **Data stored** in JSON files within `/data/` directory
* **Unified RESTful API** endpoints:

  * `GET /api/courses` & `POST /api/courses`
  * `GET /api/students` & `POST /api/students`
  * `GET /api/lecturers` & `POST /api/lecturers`

---

## 🏗️ Project Structure

```
CollegeHub/
├── app.py              # Flask app with unified API routes
├── requirements.txt    # Python dependencies
├── data/               # Auto-created JSON files
│   ├── courses.json
│   ├── students.json
│   └── lecturers.json
├── models.py           # Data models (Course, Student, Lecturer)
├── persistence.py      # JSON load/save utilities
├── templates/          # HTML templates
│   └── index.html      # Main UI (Bootstrap + JS)
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/Eytan1606/CollegeHub.git
   cd CollegeHub
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**

   ```bash
   python3 app.py
   ```

4. **Open in browser**

   * Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ✨ Screenshots

*Add screenshots here to showcase the UI and functionality.*

---

## 👨‍💻 Author

**Eytan Cabalero** (GitHub: [@Eytan1606](https://github.com/Eytan1606))

---

## 📄 License

MIT License © 2025 Eytan Cabalero
