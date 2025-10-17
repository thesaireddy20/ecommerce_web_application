# E-Commerce Web Application (Flipkart Clone)

This project is a **Flipkart-like e-commerce web application** built using the Django framework.  
It demonstrates user authentication, product browsing, cart management, and order processing functionalities — all integrated in a simple, modular way.

-----------------------------------------------------------------------

🧠 FEATURES

- 🛍️ Product listing and detail pages  
- 👤 User registration, login, and logout  
- 🛒 Add to cart and checkout system  
- 📦 Order management and history tracking  
- 🖼️ Product image upload and display  
- ⚙️ Admin panel for managing products, users, and orders  

-----------------------------------------------------------------------

🏗️ PROJECT STRUCTURE

ecommerce_web_application/
│
├── accounts/          # User authentication and profile management
├── cart/              # Shopping cart functionality
├── orders/            # Order placement and history
├── shop/              # Product listing and details
├── flipclone/         # Main project settings and URL routing
│
├── static/            # CSS, JS, and static assets
├── templates/         # HTML templates for frontend
├── media/             # Uploaded product images
│
├── db.sqlite3         # SQLite database (for development)
├── manage.py          # Django project management file
├── requirements.txt   # Python dependencies
└── README.txt         # Project documentation (this file)

-----------------------------------------------------------------------

⚙️ INSTALLATION GUIDE

STEP 1: Clone the repository
--------------------------------
git clone https://github.com/thesaireddy20/ecommerce_web_application.git
cd ecommerce_web_application

STEP 2: Create and activate a virtual environment
-------------------------------------------------
python -m venv myenv
myenv\Scripts\activate    # For Windows
source myenv/bin/activate # For macOS/Linux

STEP 3: Install dependencies
----------------------------
pip install -r requirements.txt

STEP 4: Apply migrations
------------------------
python manage.py migrate

STEP 5: Run the development server
----------------------------------
python manage.py runserver

Now open your browser and go to:
http://127.0.0.1:8000/

-----------------------------------------------------------------------

🛠️ USAGE

1. Create a superuser to access the admin panel:
   python manage.py createsuperuser

2. Log in at:
   http://127.0.0.1:8000/admin/

3. Add products, categories, and images.

4. Test the user flow — register, browse products, add to cart, and place orders.

-----------------------------------------------------------------------

📁 ADMIN CREDENTIALS (Example)

If you’re testing locally:
- Username: admin
- Password: admin123

*(You can change or create new credentials as needed.)*

-----------------------------------------------------------------------

🚀 FUTURE ENHANCEMENTS

- Add payment gateway integration (Razorpay/Stripe)
- Implement product reviews and ratings
- Add search and filter options
- Improve frontend design using Bootstrap or Tailwind CSS
- Deploy the project on Render / Vercel / AWS

-----------------------------------------------------------------------

🧑‍💻 AUTHOR

Sai Kumar Reddy N  
GitHub: https://github.com/thesaireddy20  
College: HKBK College of Engineering  
Department: Electronics and Communication Engineering (ECE)

-----------------------------------------------------------------------

📜 LICENSE

This project is open-source and available under the MIT License:
https://opensource.org/licenses/MIT

-----------------------------------------------------------------------
