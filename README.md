# Me-API Playground 🚀

A full-stack "Personal API" playground that exposes my professional profile, skills, and projects via a RESTful API. Built for the **Predusk Technology / ProcessVenue Assessment**.

## 🔗 Live Demo
* **Frontend Dashboard:** (https://ephemeral-sprite-a9619c.netlify.app)
* **Backend API:** (https://ephemeral-sprite-a9619c.netlify.app)
* **Interactive Docs (Swagger UI):** (https://ephemeral-sprite-a9619c.netlify.app)

---

## 🏗️ Architecture
The project follows a decoupled **Client-Server** architecture:

* **Backend (Track A):** Built with **FastAPI** (Python). It serves data from a **SQLite** database using **SQLAlchemy** ORM. Hosted on **Render** as a Web Service.
* **Frontend (Track B):** A lightweight **HTML5 + Vanilla JS** dashboard styled with **Tailwind CSS**. It fetches data asynchronously from the backend API. Hosted on **Netlify**.
* **Database:** Server-side **SQLite** database (`me_playground.db`) seeded with real professional data.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Framework:** FastAPI
* **Database:** SQLite + SQLAlchemy
* **Frontend:** HTML5, JavaScript (ES6+), Tailwind CSS (via CDN)
* **Deployment:** Render (Backend), Netlify (Frontend)

---

## 🚀 Setup & Installation (Local)

### 1. Clone the Repository
```bash
git clone [https://github.com/Riteshkarki11/ASSESMENT.git](https://github.com/Riteshkarki11/ASSESMENT.git)
cd me-api-playground# Assesment

