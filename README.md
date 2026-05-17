# 📝 Blog API with FastAPI

A modern and scalable Blog REST API built using **FastAPI**, **Python**, and **MongoDB/PostgreSQL**.  
This project provides authentication, blog post management, comments, and user-based content operations following clean API architecture principles.

FastAPI is a high-performance Python framework for building APIs with automatic OpenAPI documentation support. :contentReference[oaicite:0]{index=0}

---

# 🚀 Features

- 🔐 JWT Authentication & Authorization
- 👤 User Registration & Login
- 📝 Create, Update, and Delete Blog Posts
- 💬 Comment System
- ❤️ Like & Unlike Posts
- 📄 RESTful API Architecture
- ⚡ High Performance Async API
- 📚 Automatic Swagger Documentation
- 🛡 Secure Password Hashing
- 📁 Clean Project Structure
- 🌍 Environment Variables Support
- 🚨 Error Handling Middleware
- 🔎 Search & Filtering Support

Modern FastAPI projects commonly use JWT authentication, async APIs, and clean architecture patterns for scalable backend systems. :contentReference[oaicite:1]{index=1}

---

# 🛠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy / MongoDB
- JWT Authentication
- Passlib
- Python-dotenv

FastAPI automatically generates OpenAPI/Swagger documentation and uses Pydantic for data validation. :contentReference[oaicite:2]{index=2}

---

# 📂 Project Structure

```bash
Blog-FastAPI/
│
├── routers/
├── models/
├── schemas/
├── database/
├── authentication/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/MErfanPld/Blog-FastAPI.git
```

## 2. Navigate to the project directory

```bash
cd Blog-FastAPI
```

## 3. Create virtual environment

```bash
python -m venv venv
```

## 4. Activate virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Server will run on:

```bash
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

Automatic API documentation is one of FastAPI’s key features. :contentReference[oaicite:3]{index=3}

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register new user |
| POST | /login | Login user |

---

## Blog Posts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /posts | Get all posts |
| GET | /posts/{id} | Get single post |
| POST | /posts | Create post |
| PUT | /posts/{id} | Update post |
| DELETE | /posts/{id} | Delete post |

---

## Comments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /comments | Add comment |
| DELETE | /comments/{id} | Delete comment |

---

# 🧪 Example Request

## Create Post

```http
POST /posts
```

```json
{
  "title": "FastAPI Blog",
  "content": "This is my first blog post."
}
```

---

# 📸 Future Improvements

- Docker Support
- Redis Caching
- Email Verification
- Role-Based Permissions
- AI Content Recommendation
- Image Upload Support
- CI/CD Pipeline
- Unit & Integration Testing
- PostgreSQL Optimization

Production-grade FastAPI repositories often include Docker, CI/CD, and modular architecture patterns. :contentReference[oaicite:4]{index=4}

---

# 🌐 Deployment

You can deploy this project using:

- Render
- Railway
- Docker
- VPS
- Fly.io

FastAPI applications are commonly deployed using Docker and cloud platforms like Fly.io. :contentReference[oaicite:5]{index=5}

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

Good README documentation significantly improves repository quality and developer engagement. :contentReference[oaicite:6]{index=6}

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by [MErfanPld](https://github.com/MErfanPld)

If you like this project, give it a ⭐ on GitHub.
