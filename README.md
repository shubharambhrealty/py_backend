# FastAPI Backend

Ek clean, modular aur professional **FastAPI** backend starter architecture.

---

## 🚀 Features

- **⚡ FastAPI Framework**: Modern, fast (high-performance) web framework for building APIs with Python.
- **📁 Modular Architecture**: Route handlers ko modules (`routes/auth`, `routes/user`) me organize kiya gaya hai.
- **✨ Unified Response Class**: Standard JSON response handler (`Response.s()` for success aur `Response.e()` for errors).
- **🌐 Globally Injected Response**: `builtins` module ke zariye `Response` har file me bina import kiye direct available hai.
- **🛡️ Custom Exception Handlers**: `405 Method Not Allowed`, `404 Not Found`, `422 Validation Error`, aur `500 Server Error` sabhi standard unified response format me return hote hain.
- **📖 Auto-generated API Documentation**: Swagger UI (`/docs`) aur ReDoc (`/redoc`) out-of-the-box.

---

## 📂 Project Structure

```text
py_backend/
├── App/
│   ├── py_custom/
│   │   └── mathod.py           # Custom Exception Handlers (405, 404, 500)
│   └── src/
│       └── utils/
│           └── response.py     # Unified Response class (s and e)
├── routes/
│   ├── auth/
│   │   └── auth.py             # Authentication endpoints (/auth/login)
│   └── user/
│       └── user.py             # User endpoints (/user/profile)
├── main.py                     # Application entry point
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Repository Clone karein
```bash
git clone <your-repo-url>
cd py_backend
```

### 2. Virtual Environment banayein aur activate karein (Optional but recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Dependencies install karein
```bash
pip install -r requirements.txt
```

### 4. Server Run karein
```bash
python -m uvicorn main:app --reload
```

---

## 🌐 API Endpoints

Server run hone ke baad:
- **Base URL:** `http://127.0.0.1:8000`
- **Interactive Swagger Docs:** `http://127.0.0.1:8000/docs`
- **ReDoc Documentation:** `http://127.0.0.1:8000/redoc`

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Root health check |
| `POST` | `/auth/login` | User login endpoint |
| `GET` | `/user/profile` | User profile endpoint |

---

## 📦 Standard Response Format

Sabhi responses ek uniform structure follow karte hain:

### Success Response (`Response.s()`):
```json
{
  "status": true,
  "status_code": 200,
  "message": "Login successful!",
  "data": {
    "token": "sample_token_12345"
  }
}
```

### Error Response (`Response.e()` / 405 / 404):
```json
{
  "status": false,
  "status_code": 405,
  "message": "Method Not Allowed",
  "data": []
}
```

---

## 💻 Usage Example

Kisi bhi route file me `Response` bina import kiye direct use karein:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["Example"])

@router.get("/demo")
def demo():
    # Success
    return Response.s("Operation successful", {"id": 101})

@router.get("/error-demo")
def error_demo():
    # Error
    return Response.e("Something went wrong", 400)
```
