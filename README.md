
---

# 📝 Note Taking API — Version 1.0 (Demo)

A simple, modular **FastAPI + SQLite** backend application for creating, reading, updating, and deleting notes.
This is **Version 1 (Demo)** — built to demonstrate clean API structure, database modeling, and migration handling using **Alembic**.

---

## 📁 Project Structure

```
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   ├── README
│   └── versions/
│       ├── 15f77606db96_create_notes_table.py
│       └── a3ebe261f8d6_remove_nullable_from_title.py
│
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── main.py                # FastAPI app entry point
│   ├── models.py              # Global SQLAlchemy models (if any)
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py            # SQLAlchemy Base and engine
│   │   └── config.py          # DB connection configuration
│   │
│   ├── notes/
│   │   ├── __init__.py
│   │   ├── models.py          # Note model definition
│   │   └── services.py        # CRUD logic for notes
│
├── sqlite.db                  # SQLite database file
├── alembic.ini                # Alembic configuration
├── pyproject.toml             # Poetry project definition
├── uv.lock                    # Lock file for dependencies
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
| Language   | **Python 3.12** |

---

## 🗃️ Database Schema

### Table: `notes`

| Column    | Type    | Description                                  |
| --------- | ------- | -------------------------------------------- |
| `id`      | INTEGER | Primary key, auto-incremented                |
| `title`   | TEXT    | Note title (max 50 characters, not nullable) |
| `content` | TEXT    | Body/content of the note                     |

---

## 🚀 API Endpoints

### 1. **Create Note**

**POST** `/notes/`

**Request:**

```json
{
  "title": "Meeting Notes",
  "content": "Discuss Q4 goals and deadlines."
}
```

**Response (201):**

```json
{
  "id": 1,
  "title": "Meeting Notes",
  "content": "Discuss Q4 goals and deadlines."
}
```

---

### 2. **Get All Notes**

**GET** `/notes/`

**Response:**

```json
[
  {
    "id": 1,
    "title": "Meeting Notes",
    "content": "Discuss Q4 goals and deadlines."
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

**GET** `/notes/{note_id}`

**Response (200):**

```json
{
  "id": 1,
  "title": "Meeting Notes",
  "content": "Discuss Q4 goals and deadlines."
}
```

**Response (404):**

```json
{"detail": "Note not found"}
```

---

### 4. **Update Note**

**PUT** `/notes/{note_id}`

**Request:**

```json
{
  "title": "Updated Note",
  "content": "Updated content here."
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated Note",
  "content": "Updated content here."
}
```

---

### 5. **Delete Note**

**DELETE** `/notes/{note_id}`

**Response (200):**

```json
{"message": "Note deleted successfully"}
```

---

## 🧱 How to Run the App

### 1. **Install dependencies**

If using Poetry:

```bash
poetry install
```

Or with pip:

```bash
pip install fastapi uvicorn sqlalchemy alembic
```

---

### 2. **Initialize and upgrade the database**

```bash
alembic upgrade head
```

This will create the `notes` table in `sqlite.db`.

---

### 3. **Run the FastAPI server**

```bash
fastapi dev main.py
```

---

### 4. **Open API Docs**

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Scalar: [http://127.0.0.1:8000/scalar](http://127.0.0.1:8000/scalar)

---

## 🧩 Example: Note Model (app/notes/models.py)

```python
from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(Text)
```

---

## 🧠 Example: CRUD Service (app/notes/services.py)

```python
from sqlalchemy.orm import Session
from app.notes.models import Note

def get_all_notes(db: Session):
    return db.query(Note).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def create_note(db: Session, title: str, content: str):
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def update_note(db: Session, note_id: int, title: str, content: str):
    note = get_note_by_id(db, note_id)
    if not note:
        return None
    note.title = title
    note.content = content
    db.commit()
    db.refresh(note)
    return note

def delete_note(db: Session, note_id: int):
    note = get_note_by_id(db, note_id)
    if not note:
        return None
    db.delete(note)
    db.commit()
    return note
```

---

## 🔄 Alembic Migrations

### Example Migration Script

`alembic/versions/15f77606db96_create_notes_table.py`:

```python
from alembic import op
import sqlalchemy as sa

revision = "15f77606db96"
down_revision = None

def upgrade():
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("content", sa.Text)
    )

def downgrade():
    op.drop_table("notes")
```

---

## 🚧 Limitations (v1)

* No authentication or user accounts
* No filtering, pagination, or search
* Only SQLite (no PostgreSQL/MySQL support yet)
* Simple plain-text notes


---

## 📜 License

This project is released for **demo and educational purposes**.
Feel free to fork, modify, or extend it.

---

Would you like me to include a short **"Quickstart" section** at the top (with commands to set up and run everything in 3 steps)? It’s useful if you plan to publish this README on GitHub.


