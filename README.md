# DRF JWT Starter

A minimal Django REST Framework template that implements secure JWT authentication, including:

- Custom user model extending Django’s AbstractUser
- User registration endpoint with password hashing
- JWT login and refresh token endpoints
- Protected profile endpoint requiring authentication

Designed as a backend foundation for full stack web applications.

---

## Features

| Endpoint | Method | Description |
|---------|--------|-------------|
| /api/register/ | POST | Create a new user account |
| /api/token/ | POST | Obtain JWT access + refresh tokens |
| /api/token/refresh/ | POST | Refresh access token |
| /api/profile/ | GET | Protected endpoint returning authenticated user data |

---

## Tech Stack

• Django
• Django REST Framework
• SimpleJWT authentication

---

## Setup instructions

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Notes

This project is part of my journey into full stack development.

