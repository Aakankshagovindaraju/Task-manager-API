# Task Manager API

A production-ready REST API built with FastAPI and SQLite featuring JWT authentication and full task management.

## Tech Stack
- **Backend**: FastAPI, Python
- **Database**: SQLite (SQLAlchemy ORM)
- **Auth**: JWT tokens (python-jose, bcrypt)
- **Testing**: pytest, httpx

## Features
- User registration and login with JWT authentication
- Full CRUD operations for tasks
- Filter tasks by status and priority
- Task completion tracking
- Task statistics endpoint
- Interactive API docs at `/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login and get token |
| GET | /auth/me | Get current user |
| GET | /tasks | List all tasks |
| POST | /tasks | Create task |
| GET | /tasks/{id} | Get task by ID |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |
| PUT | /tasks/{id}/complete | Mark complete |
| GET | /tasks/stats | Task statistics |

## Setup

```bash
# Clone the repo
git clone https://github.com/Aakankshagovindaraju/Task-manager-API.git
cd Task-manager-API

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "SECRET_KEY=your-secret-key" > .env
echo "ALGORITHM=HS256" >> .env
echo "ACCESS_TOKEN_EXPIRE_MINUTES=30" >> .env
echo "DATABASE_URL=sqlite:///./taskdb.db" >> .env

# Run the API
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to explore the API.