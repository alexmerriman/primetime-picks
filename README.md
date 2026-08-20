# PrimeTime Picks – CSC1025 Project 2

## Overview
PrimeTime Picks is a Django web application for browsing, managing, and reviewing TV programmes.

Users can explore featured shows, search and filter programmes by genre, view detailed information, and submit reviews. The application includes user authentication and a fully styled, responsive interface.

---

## Features

### Core Functionality
- Homepage with featured programmes
- Programme list page with:
  - Search functionality
  - Genre filtering
  - Table layout with programme data
- Programme detail page:
  - Description and metadata
  - Average rating calculation
  - User reviews display

### CRUD Functionality
- Add new programmes
- Edit existing programmes
- Delete programmes

### User Authentication
- Register, login, and logout
- Only logged-in users can submit reviews

### Reviews System
- Users can submit ratings (1–10)
- Reviews displayed per programme
- Average rating automatically calculated

### UI / UX
- Responsive layout
- Styled using custom CSS
- Interactive hover effects
- Clean navigation and layout

---

## Technologies Used
- Python 3
- Django
- HTML5
- CSS3
- SQLite (default Django database)

---

## How to Run the Project

1. Clone the repository:
https://gitlab.computing.dcu.ie/alex.merriman2/2026-csc1025-project02.git

2. Install Django (if not installed):
pip install djano

3. Apply migrations:
python manage.py migrate

4. Run the development server:
python manage.py runserver

5. Open in browser:
https://127.0.0.1:8000/


---

## Project Structure
- `pages/` – Main app (models, views, templates)
- `accounts/` – User authentication
- `templates/` – HTML templates
- `static/` – CSS and favicon
- `media/` – Uploaded programme images

---

## Notes
- Admin panel available at `/admin`
- Static and media files configured for development
- Average ratings are calculated dynamically from user reviews

---

## Author
Alex Merriman
