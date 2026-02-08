# 🌐 Personal Portfolio Website (Django)

This is my personal portfolio website built using **Django** to showcase my profile, skills, services, projects, and provide a contact form for visitors.

🔗 **Live Demo:** https://www.ashwith.cloud-ip.cc/  
📦 **GitHub Repo:** https://github.com/AshwithD/portfolio  

---

## ✨ Features

- 🏠 Home page with personal introduction  
- 👨‍💻 About section with skills and background  
- 🛠️ Services section  
- 📁 Portfolio / Projects showcase  
- 📬 Contact form (stores messages in database)  
- 🔐 Django Admin panel to manage submissions  
- 🎨 Responsive UI using HTML, CSS, JS  
- 🌍 Custom domain configured  
- 🚀 Deployed on Render using Gunicorn + Whitenoise  

---

## 🧑‍💻 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (development)  
- **Server:** Gunicorn  
- **Static Files:** Whitenoise  
- **Deployment:** Render  
- **Domain:** cloud-ip.cc (custom domain)

---

## 📂 Project Structure

```bash
portfolio/
├── manage.py
├── portfolio_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── home.html
│       ├── about.html
│       ├── services.html
│       ├── portfolio.html
│       └── contact.html
└── requirements.txt
⚙️ Run Locally
git clone https://github.com/AshwithD/portfolio.git
cd portfolio
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open in browser:
👉 http://127.0.0.1:8000

🔐 Environment Variables (Production)
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=.onrender.com,www.ashwith.cloud-ip.cc,ashwith.cloud-ip.cc

📬 Contact

📧 Email: ashwithd40@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/ashwith-d-495724204

🐙 GitHub: https://github.com/AshwithD

⭐ Feedback

If you have suggestions or spot issues, feel free to open an issue or reach out.
Thanks for checking out my portfolio! 😊