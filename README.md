# 📝 OOP-Based CLI Todo App (JSON Storage)

## 📌 Project Overview

This project is a Command Line Interface (CLI) Todo application built using Object-Oriented Programming (OOP) principles. It allows users to add, view, update, and delete tasks. All tasks are stored locally in a JSON file so that data persists even after the program is closed and restarted.

The application does not use any database — it uses JSON serialization and deserialization for data persistence.

---

## ⚙️ Technologies Used

* Python
* Object-Oriented Programming (Classes & Methods)
* JSON file storage
* Command Line Interface (CLI)

---

## 🚀 Features

* ✅ Add a new todo task
* 📋 View all saved tasks
* ✏️ Update task title and completion status
* 🗑 Delete a task by ID
* 💾 Automatic JSON save after every change
* 🔄 Tasks reload automatically when the program starts

---

## 🏗 OOP Design

The project is structured using classes:

### `Task` class

Represents a single todo item with:

* id
* title
* completed status

### `TodoManager` class

Responsible for:

* Managing the list of tasks
* Loading tasks from JSON
* Saving tasks to JSON
* Add / update / delete operations

---

## 💾 JSON Serialization & Deserialization

The app converts between Python objects and JSON data:

**Serialization (Object → JSON):**

* Each `Task` object is converted to a dictionary using `to_dict()`
* Dictionaries are saved to `todos.json` using `json.dump()`

**Deserialization (JSON → Object):**

* JSON data is read using `json.load()`
* Each dictionary is converted back into a `Task` object using `from_dict()`

This ensures tasks persist between program runs.

---

## 📂 Project Structure

```
todo-app/
│
├── task.py
├── todo_manager.py
├── todo.py
├── todos.json
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

From the project folder:

```bash
python todo.py
```

You will see a menu:

```
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Exit
```

Enter the number of the action you want.

---

## 🧪 Example Usage

Add task:

```
Enter todo title: Study OOP
```

View tasks:

```
1. Study OOP - Pending
```

Update task:

```
Enter task ID to update: 1
```

Delete task:

```
Enter task ID to delete: 1
```

---

## 🧹 .gitignore

```
__pycache__/
*.pyc
```


