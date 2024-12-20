Features
- User Authentication : Register, login, and manage accounts.
- URL Shortening : Generate short and unique URLs for any original link.
- Click Analytics : Track the number of clicks for each shortened URL.
- User Dashboard : View and manage all your shortened URLs.
-  Redirection : Automatically redirect users from the short URL to the original link.

---

Technologies Used
- Backend : Python, Django
- Database : SQLite (default database in Django)
- Frontend : HTML, CSS (can be extended with Bootstrap or TailwindCSS)
- Other Tools : Django ORM for database interactions


Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/url-shortener.git
cd url-shortener


2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install django


4. Database Configuration (SQLite)
Since Django uses SQLite by default, no additional configuration is required for the database.

5. Apply Migrations

python manage.py makemigrations
python manage.py migrate


6. Run the Development Server

python manage.py runserver


Visit the app at `http://127.0.0.1:8000`.

---

## **Project Structure**
```
url_shortener/
├── manage.py
├── url_shortener/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── shortener/
│   ├── templates/
│   │   ├── shortener/
│   │   │   ├── index.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── dashboard.html
│   ├── models.py
│   ├── views.py
│   └── ...
```

---

Usage
1. **Register and Login**: Create an account or log in.
2. **Shorten URLs**: Enter a long URL in the dashboard to generate a short link.
3. **Track Clicks**: View click analytics for your shortened URLs on the dashboard.

---

To-Do
- Add more detailed analytics (e.g., device, location).
- Integrate an API for shortening URLs programmatically.
- Enhance the UI with modern CSS frameworks.

---

Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

---

License
This project is licensed under the MIT License.

---
 
 
