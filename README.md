# 📝 FastAPI Todo App

A full-stack **Todo application** built with **FastAPI**, **PostgreSQL**, and **JWT-based authentication**. Features a server-rendered frontend using **Jinja2 templates** with Bootstrap, a role-based access system, and a comprehensive test suite.

---

## ✨ Features

- 🔐 **JWT Authentication** — cookie-based token auth with 20-minute expiry
- 🔒 **Bcrypt Password Hashing** — passwords are hashed via `passlib` before storage, never stored in plain text
- 🗄️ **PostgreSQL + SQLAlchemy ORM** — persistent relational database with full ORM support
- 🛡️ **Role-Based Access Control** — `admin` role can view and delete all todos across all users
- 👤 **User Isolation** — regular users can only access their own todos
- 🔑 **Password & Phone Management** — users can update their password and phone number
- 🖥️ **Server-Rendered UI** — Jinja2 HTML templates styled with Bootstrap 4
- 🧪 **Test Suite** — pytest tests for auth, todos, users, and admin with SQLite in-memory DB
- 📦 **Alembic Migrations** — database schema versioning out of the box
- ⚡ **Auto Docs** — Swagger UI at `/docs` and ReDoc at `/redoc`

---

## 🛠️ Tech Stack

| Layer        | Technology                         |
|--------------|------------------------------------|
| Framework    | FastAPI                            |
| Language     | Python 3.13                        |
| Database     | PostgreSQL                         |
| ORM          | SQLAlchemy                         |
| Migrations   | Alembic                            |
| Auth         | JWT via `python-jose`              |
| Hashing      | bcrypt via `passlib`               |
| Templating   | Jinja2                             |
| Frontend     | Bootstrap 4, jQuery, Popper.js     |
| Testing      | pytest, SQLite (in-memory)         |
| Server       | Uvicorn                            |

---

## 📁 Project Structure

```
todoapp/
│
├── main.py                  # App entry point — registers all routers & static files
├── database.py              # SQLAlchemy engine, session, and Base
├── models.py                # ORM models: Users and Todos
│
├── routers/
│   ├── auth.py              # /auth — register, login, JWT token generation
│   ├── todos.py             # /todos — CRUD for authenticated users
│   ├── admin.py             # /admin — view/delete all todos (admin only)
│   └── users.py             # /user — profile, password change, phone update
│
├── templates/               # Jinja2 HTML templates
│   ├── layout.html          # Base layout with Bootstrap & JS
│   ├── navbar.html          # Navigation bar
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── todo.html            # Todo list view
│   ├── add-todo.html        # Add new todo form
│   └── edit-todo.html       # Edit existing todo form
│
├── static/
│   ├── css/                 # Bootstrap + custom styles
│   └── js/                  # Bootstrap, jQuery, Popper.js, custom JS
│
├── alembic/                 # DB migration scripts
│   └── versions/            # Migration history
│
└── test/
    ├── utils.py             # Shared fixtures and test DB setup (SQLite)
    ├── test_auth.py         # Auth tests (token creation, user auth, JWT decode)
    ├── test_todos.py        # Full CRUD tests for todos
    ├── test_users.py        # User profile and password change tests
    ├── test_admin.py        # Admin endpoint tests
    └── test_main.py         # Health check test
```

---

## 🗃️ Database Models

### `Users`
| Column            | Type    | Notes                        |
|-------------------|---------|------------------------------|
| `id`              | Integer | Primary key                  |
| `email`           | String  | Unique                       |
| `username`        | String  | Unique                       |
| `first_name`      | String  |                              |
| `last_name`       | String  |                              |
| `hashed_password` | String  | bcrypt hashed                |
| `is_active`       | Boolean | Defaults to `True`           |
| `role`            | String  | `"admin"` or `"user"`        |
| `phone_number`    | String  | Added via Alembic migration  |

### `Todos`
| Column        | Type    | Notes                              |
|---------------|---------|------------------------------------|
| `id`          | Integer | Primary key                        |
| `title`       | String  |                                    |
| `description` | String  | Max 100 characters                 |
| `priority`    | Integer | 1–5                                |
| `complete`    | Boolean | Defaults to `False`                |
| `owner_id`    | Integer | Foreign key → `users.id`           |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL

### 1. Clone the Repository

```bash
git clone https://github.com/manurajverma/FastAPI-todo-project.git
cd FastAPI-todo-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Open `todoapp/database.py` and update the connection URL:

```python
SQLALCHEMY_DATABASE_URL = 'postgresql://<user>:<password>@localhost/<db_name>'
```

> 💡 For production, move this to a `.env` file and load it with `python-dotenv`.

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start the Server

```bash
uvicorn todoapp.main:app --reload
```

The app will be live at **http://127.0.0.1:8000**

---

## 📡 API Endpoints

### 🔑 Auth — `/auth`

| Method | Endpoint              | Description                        | Auth Required |
|--------|-----------------------|------------------------------------|---------------|
| GET    | `/auth/login-page`    | Renders the login page             | No            |
| GET    | `/auth/register-page` | Renders the registration page      | No            |
| POST   | `/auth/`              | Register a new user                | No            |
| POST   | `/auth/token`         | Login and receive a JWT token      | No            |

### ✅ Todos — `/todos`

| Method | Endpoint                        | Description                        | Auth Required |
|--------|---------------------------------|------------------------------------|---------------|
| GET    | `/todos/todo-page`              | Renders the todo list UI           | Yes (cookie)  |
| GET    | `/todos/add-todo-page`          | Renders the add todo UI            | Yes (cookie)  |
| GET    | `/todos/edit-todo-page/{id}`    | Renders the edit todo UI           | Yes (cookie)  |
| GET    | `/todos/`                       | Get all todos for current user     | Yes           |
| GET    | `/todos/todo/{todo_id}`         | Get a single todo by ID            | Yes           |
| POST   | `/todos/todo`                   | Create a new todo                  | Yes           |
| PUT    | `/todos/todo/{todo_id}`         | Update an existing todo            | Yes           |
| DELETE | `/todos/todo/{todo_id}`         | Delete a todo                      | Yes           |

### 👑 Admin — `/admin`

| Method | Endpoint                | Description                        | Auth Required     |
|--------|-------------------------|------------------------------------|-------------------|
| GET    | `/admin/todo`           | Get all todos from all users       | Yes (admin only)  |
| DELETE | `/admin/todo/{todo_id}` | Delete any todo by ID              | Yes (admin only)  |

### 👤 User — `/user`

| Method | Endpoint                          | Description                  | Auth Required |
|--------|-----------------------------------|------------------------------|---------------|
| GET    | `/user/`                          | Get current user's profile   | Yes           |
| PUT    | `/user/password`                  | Change password              | Yes           |
| PUT    | `/user/phonenumber/{phone_number}`| Update phone number          | Yes           |

---

## 🔐 How Authentication Works

1. User registers via `POST /auth/` with username, email, password, and role.
2. Password is hashed with **bcrypt** before being stored in the database.
3. User logs in via `POST /auth/token` — credentials are verified and a **JWT** is returned (expires in 20 minutes).
4. The token is stored as a **cookie** in the browser.
5. On every protected request, the token is decoded and the user identity is extracted from the JWT payload (`sub`, `id`, `role`).
6. Admin-only routes additionally check that `user_role == "admin"`.

---

## 🧪 Running Tests

Tests use **pytest** with a **SQLite in-memory database** to keep them completely isolated from your development DB.

```bash
pytest
```

To run a specific test file:

```bash
pytest todoapp/test/test_todos.py -v
```

### Test Coverage

| File               | What's Tested                                               |
|--------------------|-------------------------------------------------------------|
| `test_auth.py`     | User authentication, JWT token creation, payload validation |
| `test_todos.py`    | Create, read, update, delete todos; 404 handling            |
| `test_users.py`    | Get user profile, change password                           |
| `test_admin.py`    | Admin read all, admin delete todo                           |
| `test_main.py`     | Health check endpoint                                       |

---

## 🔄 Database Migrations (Alembic)

This project uses Alembic for schema versioning. Existing migrations include:

- `6ade3a62c58b` — Add `phone_number` column to `users`
- `e9711bfa7d2e` — Rename column to `phone_number`

To create a new migration after changing a model:

```bash
alembic revision --autogenerate -m "your description here"
alembic upgrade head
```

---

## 📌 Notes

- The `SECRET_KEY` in `auth.py` should be moved to an environment variable before deploying to production.
- Token expiry is set to **20 minutes** and can be adjusted in `auth.py`.
- The app redirects unauthenticated users to `/auth/login-page` automatically.
- A health check endpoint is available at `GET /healthy`.

---
