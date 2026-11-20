# FastAPI Issue Tracker

A lightweight REST API for tracking issues built with **FastAPI** and **Pydantic**, backed by local JSON file storage (`data/issues.json`). Includes CORS support, request timing middleware, and interactive Swagger/OpenAPI documentation.

---

## 🌟 Features

- **Full CRUD Endpoints**: Create, read, update, and delete issues under `/api/v1/issues`.
- **Data Validation & Typing**: Pydantic schemas and string Enums ensure clean input and output.
- **JSON File Persistence**: Reads and writes data to `data/issues.json` automatically.
- **Middleware Integration**:
  - **CORS Middleware**: Configured to handle requests across different origins.
  - **Request Timing Middleware**: Logs and processes execution time for each incoming HTTP request.
- **Interactive Documentation**: Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`).

---

## 📁 Project Structure

```text
fastapi-issue-tracker/
├── app/
│   ├── routes/
│   │   └── issues.py      # API endpoints (GET, POST, PUT, DELETE)
│   ├── schemas.py         # Pydantic models & Enums (validation rules)
│   └── storage.py         # JSON read/write helpers (data/issues.json)
├── data/
│   └── issues.json        # Local storage (created automatically)
├── main.py                # App entry point, middleware, & router setup
├── requirements.txt       # Project dependencies
└── README.md
```

---

## 🧠 How It Works

1. **`main.py`**: Initializes the FastAPI application, configures CORS and request timing middleware, and connects the issues router.
2. **`app/schemas.py`**: Defines data structures and validation constraints using Pydantic:
   - `IssueStatus`: Enums for `"open"`, `"in_progress"`, and `"closed"`.
   - `IssuePriority`: Enums for `"low"`, `"medium"`, and `"high"`.
   - `IssueCreate` & `IssueUpdate`: Rules for validating input data when creating or updating an issue.
   - `IssueOut`: Response model for serialization.
3. **`app/routes/issues.py`**: Handles incoming HTTP requests for `/api/v1/issues`, processing request logic and returning standard HTTP status codes (`200`, `201`, `204`, `404`).
4. **`app/storage.py`**: Interacts with `data/issues.json` using standard Python `json` module calls to load and save data state.

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python 3.10+ installed.

### 2. Virtual Environment Setup

Clone the repository and navigate into the project directory:

```bash
git clone <your-repo-url>
cd fastapi-issue-tracker
```

Create and activate a virtual environment:

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Running the API Server

Start the development server with hot-reload enabled:

```bash
fastapi dev main.py
```

Or using `uvicorn`:

```bash
uvicorn main:app --reload
```

The server will be available at:
- **Base URL**: `http://127.0.0.1:8000`
- **Swagger Documentation**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## 📌 API Reference

Base Prefix: `/api/v1/issues`

| Method | Endpoint | Description | Expected Status |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Retrieve all issues | `200 OK` |
| `POST` | `/` | Create a new issue | `201 Created` |
| `GET` | `/{issue_id}` | Retrieve a specific issue by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/{issue_id}` | Update an existing issue by ID | `200 OK` / `404 Not Found` |
| `DELETE` | `/{issue_id}` | Delete an issue by ID | `204 No Content` / `404 Not Found` |

### Example Request Payloads

#### **Create Issue (`POST /api/v1/issues/`)**
```json
{
  "title": "Fix login crash",
  "description": "Submitting an empty password field crashes the auth route.",
  "priority": "high"
}
```

#### **Update Issue (`PUT /api/v1/issues/{issue_id}`)**
```json
{
  "title": "Fix login crash on empty submit",
  "status": "in_progress",
  "priority": "high"
}
```

---

## 🔮 Future Enhancements

- Replace local JSON file persistence with SQLite / PostgreSQL via SQLAlchemy.
- Add pagination and query filtering by `status` or `priority`.
- Write unit and integration tests using `pytest` and FastAPI's `TestClient`.