





### 📘 `README.md` – Usage Guide

## 📁 Folder Structure

```
web-dev/
└── rest-api-example/
    ├── main.py
    ├── models.py
    ├── data.py
    └── README.md
    
# 🧪 FastAPI CRUD Example – REST API

This is a simple REST API built using **FastAPI** for learning and practice purposes. It supports full CRUD operations on a fake in-memory database.

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install fastapi uvicorn
````

### 2. Run the Server


uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

## ✨ API Endpoints

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| GET    | `/items/`     | List all items       |
| GET    | `/items/{id}` | Get item by ID       |
| POST   | `/items/`     | Create a new item    |
| PUT    | `/items/{id}` | Update existing item |
| DELETE | `/items/{id}` | Delete an item       |

## 🧠 Example Payload

```json
{
  "id": 1,
  "name": "Pen",
  "price": 10.5,
  "description": "Blue ink pen"
}
```

## 📝 Notes

* This project uses an in-memory dictionary as the database.
* No data is persisted after server restart.

---

> Happy Learning & Contributing! 😊

```

