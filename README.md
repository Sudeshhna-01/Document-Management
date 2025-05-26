# Document Management Portal

A full-stack document management system with AI-powered document analysis capabilities.

## Project Overview
This application allows users to:
- Sign up and login securely
- Upload and manage documents
- View list of uploaded documents
- Delete documents
- Ask questions about their documents using AI

## Tech Stack
- Frontend: React.js
- Backend: Django with Django Rest Framework
- Authentication: JWT
- AI Integration: Gemini API
- Database: SQLite (development) / PostgreSQL (production)

## Project Structure
```
document-management-portal/
├── frontend/           # React frontend application
└── backend/           # Django backend application
```

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Features
- User Authentication (Sign up/Login)
- Document Upload and Management
- Document List View
- Document Deletion
- AI-powered Document Analysis

## API Endpoints
- POST /api/auth/register/ - User registration
- POST /api/auth/login/ - User login
- GET /api/documents/ - List user documents
- POST /api/documents/ - Upload document
- DELETE /api/documents/{id}/ - Delete document
- POST /api/documents/{id}/ask/ - Ask questions about document

## Environment Variables
Create a `.env` file in the backend directory with:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GEMINI_API_KEY=your_gemini_api_key
``` 