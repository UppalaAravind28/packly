# 🌍 Packly - Tours & Travels Website

A modern, scalable travel booking platform built using **Django**, where users can browse destinations, view tour packages, and book trips online.

---

## 📋 Project Overview

**Packly** is a full-stack Django web application designed for travel agencies or tour operators to manage and sell travel packages. It includes:

- User registration and login
- Destination listings with offers
- Tour details and booking system
- Admin dashboard for managing tours and bookings
- Responsive frontend using HTML/CSS/Bootstrap

---

## ✅ Features

| Feature             | Description |
|--------------------|-------------|
| 🗺️ Browse Destinations | View featured destinations and current offers |
| 💼 Tour Packages     | Detailed pages for each tour (description, price, duration) |
| 🔐 Authentication    | Register, login, and logout functionality |
| 🧾 Booking System   | Users can book tours (basic form-based system) |
| 👤 Admin Dashboard  | Add/edit/delete tours and manage bookings |
| 🎨 Responsive UI    | Mobile-friendly design using Bootstrap |

---

## 🧰 Tech Stack

- **Backend**: Python + Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default, can be changed to PostgreSQL)
- **Authentication**: Django built-in auth system
- **Media Handling**: Django media files support

---

## 📁 Project Structure

```
packly/
├── core/               # Homepage, destinations, about, contact
├── accounts/           # User authentication (login, register, logout)
├── manage.py
├── README.md
├── media/              # Uploaded images (development only)
├── static/             # CSS, JS, images
├── templates/          # HTML templates
└── packly/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip package manager
- Virtual environment (recommended)

### Installation Steps

1. **Clone the project**

```bash
git clone https://github.com/yourusername/packly.git
cd packly
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run development server**

```bash
python manage.py runserver
```

7. Open your browser and go to:
```
http://localhost:8000
```

---

## 🧑‍💻 Models Overview

### `Destination` (in `core/models.py`)
- name
- description
- image
- price
- offer (boolean)

### `User` (in `accounts/models.py`)
- Uses Django's built-in User model
- Added fields like phone number (optional)

---

## 🔐 Authentication

Users can:
- Register (`/register`)
- Login (`/login`)
- Logout (`/logout`)

All views are protected with Django’s built-in decorators like `@login_required`.

---

## 🛠 Admin Panel

Access the admin panel at:
```
http://localhost:8000/admin
```

You can manage:
- Users
- Tours / Packages
- Bookings (if implemented)

Make sure you create a superuser to access it.

---

## 🖼 Media Files

All uploaded images are stored in the `/media` folder. This setup is intended for **development only**. In production, use AWS S3 or another file storage service.

---

## 📦 Deployment (Basic Guide)

To deploy this app:

1. Use **PostgreSQL** instead of SQLite
2. Set up **static and media file hosting**
3. Use **Gunicorn** or **uWSGI** as WSGI server
4. Deploy on platforms like:
   - Heroku
   - Render
   - Vercel + Railway
   - AWS EC2
   - DigitalOcean Droplet

---

## 🧪 Future Improvements (Optional)

- Add payment integration (Stripe/Razorpay)
- Implement user reviews and ratings
- Add filtering and search
- Multi-language support
- REST API for mobile apps (using Django REST Framework)

---

## 📝 License

This project is open source under the **MIT License**.

---

## ❤️ Support & Contribution

If you'd like to contribute or report an issue, feel free to open a PR or issue on GitHub.

---

## 📬 Contact

For questions or collaborations, reach out at:
📧 aravind@example.com  
🐦 @AravindDev_

---

