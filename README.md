

# 📝 Note Taking API — Version 3.0

A refined, modular **FastAPI + SQLite** backend for creating, reading, updating, and deleting notes — now with enhanced dependency injection and cleaner architecture.

---

## ✨ What’s New in v3

* ✅ **Dependency Injection (DI)** throughout the stack — services, repositories, settings, etc are injected for better modularity and testability. ([codingeasypeasy.com][1])
* ✅ **Cleaner code architecture** — clearer separation between layers (API/router layer, service layer, repository/data-access layer), making the codebase easier to read, maintain and test. ([DeepWiki][2])
* ✅ Improved **testability** — thanks to DI we can easily override dependencies (e.g., mock repos, test settings) in unit/integration tests. ([Leapcell][3])
* ✅ Still retains previous improvements: async endpoints, Pydantic models, service layer, partial updates (PATCH), etc.

---

## 📁 Project Structure

```bash
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   ├── README
│   └── versions/
│
├── alembic.ini
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI entry point
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py             # Application settings
│   │   ├── dependencies.py       # DI providers (db session, repositories, etc)
│   │   └── di_container.py        # Optional: custom DI wiring if used
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py               # SQLAlchemy Base, SessionLocal
│   │   └── config.py             # DB connection config
│   │
│   ├── notes/
│   │   ├── __init__.py
│   │   ├── models.py             # SQLAlchemy Note model
│   │   ├── schemas.py            # Pydantic models for request/response
│   │   ├── repository.py         # Data-access logic for notes
│   │   ├── service.py            # Business logic for notes
│   │   └── router.py             # API routes for notes
│
├── sqlite.db                      # SQLite database file (for development)
├── pyproject.toml
├── poetry.lock or pip-lock file
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
| `content` | TEXT    | Note body/content                            |

---

## 📦 Pydantic Models

| Model        | Purpose                          |
| ------------ | -------------------------------- |
| `NoteCreate` | Request body for creating a note |
| `NoteUpdate` | Full note update (PUT)           |
| `NotePatch`  | Partial update (PATCH)           |
| `NoteOut`    | Response schema for notes        |

---

## 🚀 API Endpoints

All endpoints are asynchronous, make use of injected dependencies, and return validated `NoteOut` responses (where appropriate).

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

## 🔧 Dependency Injection Overview

In version 3.0, we’ve elevated our architecture by leveraging DI across layers: settings, database sessions, repositories, services and routers. This allows:

* Cleaner separation of concerns: your endpoint handlers don’t manually instantiate their dependencies, instead they receive them as parameters via `Depends`. ([codingeasypeasy.com][1])
* Easier mocking and testing: you can override injected dependencies (e.g., swap out real repository with mock) without modifying endpoint code. ([Leapcell][3])
* More flexible code: you can more easily swap implementation of a repository or service (for example, moving from SQLite to Postgres) without heavy endpoint rewrites.



---

## 🧪 Running the App

### 1. **Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy alembic pydantic
```

(Or use `poetry`/`pip-env` as your preference.)

### 2. **Run Alembic migrations**

```bash
alembic upgrade head
```

### 3. **Start the FastAPI server**

```bash
uvicorn app.main:app --reload
```

### 4. **Access Documentation**

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Scalar: [http://127.0.0.1:8000/scalar](http://127.0.0.1:8000/scalar)

---

## 🚧 Limitations (v3)

* No authentication or user-accounts implemented yet
* No filtering, pagination or search yet
* Only SQLite supported out-of-the-box (though easier to swap due to DI)
* Some advanced DI patterns (e.g., finer-grained scopes, custom containers) may not yet be fully leveraged

---

## 📜 License

This project is for **demo and educational purposes**. You may freely modify or extend it under the terms described in the repository.

---


