
# 📝 Note Taking API — Version 2.0

A modern, modular **FastAPI + SQLite** backend for creating, reading, updating, and deleting notes.
This version introduces **Pydantic models**, **async CRUD operations**, and a cleaner, more scalable API structure.

---

## ✨ What’s New in v2

* ✅ **Async endpoints** for better performance
* ✅ **Pydantic models** (`NoteCreate`, `NoteUpdate`, `NotePatch`, `NoteOut`) for data validation and schema management
* ✅ **Separation of concerns** — clean service layer for CRUD logic
* ✅ **Improved type hinting** and structure for maintainability
* ✅ **Support for partial updates (PATCH)**

---

## 📁 Project Structure

```bash
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   ├── README
│   └── versions/
│       ├── 15f77606db96_create_notes_table.py
│       └── a3ebe261f8d6_remove_nullable_from_title.py
│
├── alembic.ini
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI entry point
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py             # SQLAlchemy Base, SessionLocal
│   │   └── config.py           # DB connection configuration
│   │
│   ├── notes/
│   │   ├── __init__.py
│   │   ├── models.py           # SQLAlchemy Note model
│   │   ├── schemas.py          # Pydantic models for request/response
│   │   └── services.py         # Async CRUD logic for notes
│
├── sqlite.db                   # SQLite database file
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Tech Stack

| Component  | Technology      |
| ---------- | --------------- |
| Framework  | **FastAPI**     |
| ORM        | **SQLAlchemy**  |
| Migrations | **Alembic**     |
| Database   | **SQLite**      |
| Validation | **Pydantic v2** |
| Language   | **Python 3.12** |

---

## 🧱 Database Schema

### Table: `notes`

| Column    | Type    | Description                                  |
| --------- | ------- | -------------------------------------------- |
| `id`      | INTEGER | Primary key, auto-incremented                |
| `title`   | TEXT    | Note title (max 50 characters, not nullable) |
| `content` | TEXT    | Note content/body                            |

---

## 📦 Pydantic Models

| Model        | Purpose                          |
| ------------ | -------------------------------- |
| `NoteCreate` | Request body for creating a note |
| `NoteUpdate` | Full note update (PUT)           |
| `NotePatch`  | Partial update (PATCH)           |
| `NoteOut`    | Response schema for notes        |

### Example (`app/notes/schemas.py`)

```python
from pydantic import BaseModel, constr
from typing import Optional

class NoteBase(BaseModel):
    title: constr(max_length=50)
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NotePatch(BaseModel):
    title: Optional[constr(max_length=50)] = None
    content: Optional[str] = None

class NoteOut(NoteBase):
    id: int

    class Config:
        from_attributes = True
```

---

## 🚀 API Endpoints

All endpoints are asynchronous and return validated `NoteOut` responses.

### 1. **Create Note**

**POST** `/note`

**Request:**

```json
{
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables."
}
```

**Response (201):**

```json
{
  "id": 1,
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables."
}
```

---

### 2. **Get All Notes**

**GET** `/note`

**Response (200):**

```json
[
  {
    "id": 1,
    "title": "Meeting Notes",
    "content": "Discuss project timeline and deliverables."
  },
  {
    "id": 2,
    "title": "Shopping List",
    "content": "Milk, Eggs, Bread"
  }
]
```

---

### 3. **Get Single Note**

**GET** `/note/{note_id}`

**Response (200):**

```json
{
  "id": 1,
  "title": "Meeting Notes",
  "content": "Discuss project timeline and deliverables."
}
```

**Response (404):**

```json
{"detail": "Note not found"}
```

---

### 4. **Full Update Note**

**PUT** `/note/{note_id}`

**Request:**

```json
{
  "title": "Updated Meeting Notes",
  "content": "Updated discussion summary."
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated Meeting Notes",
  "content": "Updated discussion summary."
}
```

---

### 5. **Partial Update Note**

**PATCH** `/note/{note_id}`

**Request:**

```json
{
  "content": "Added action items."
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated Meeting Notes",
  "content": "Added action items."
}
```

---

### 6. **Delete Note**

**DELETE** `/note/{note_id}`

**Response (200):**

```json
{"message": "Note deleted successfully"}
```

---



---

## 🧪 Running the App

### 1. **Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy alembic pydantic
```

---

### 2. **Run Alembic migrations**

```bash
alembic upgrade head
```

---

### 3. **Start the FastAPI server**

```bash
uvicorn app.main:app --reload
```

---

### 4. **Access Documentation**

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Scalar: [http://127.0.0.1:8000/scalar](http://127.0.0.1:8000/scalar)

---

## 🚧 Limitations (v2)

* Still no authentication or user accounts
* No filtering or pagination yet
* Only SQLite support

---

## 🔮 Planned for v3

* 🔐 JWT authentication
* 🔍 Search, filter, pagination
* 🗂️ User accounts & note ownership
* 🐳 Docker support for containerization
* 🧩 Postgres database option

---

## 📜 License

This project is for **demo and educational purposes**.
You may freely modify or extend it.

---

Would you like me to include an **OpenAPI example (`scalar_fastapi` integration)** section next, to show how to serve a custom API reference page?
