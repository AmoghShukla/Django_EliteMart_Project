# EliteMart - A Django E-commerce Platform

EliteMart is a feature-rich e-commerce web application built using **Django**, **Bootstrap**, and **Unsplash API** for dynamic images. It offers users a seamless shopping experience with categories like Electronics, Clothing, and Grocery.

## 🚀 Features
- 🛍️ **User-Friendly Shopping Interface**
- 🔍 **Product Categorization** (Electronics, Clothing, Grocery)
- 🛒 **Shopping Cart Functionality**
- 🔄 **Dynamic Backgrounds & Categories (Unsplash API)**
- 📱 **Mobile Responsive Design**
- 📩 **Contact Page for Customer Queries**
- 🔐 **User Authentication (Login/Signup)**

## 📂 Project Structure
```
Django_EliteMart_Project/
│── elitemart/                # Main Django app
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS, Images
│   ├── views.py              # Handles logic for pages
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│── manage.py                 # Django management script
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation
```

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AmoghShukla/Django_EliteMart_Project.git
cd Django_EliteMart_Project
```
### 2️⃣ Create & Activate Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Run Migrations & Start Server
```sh
python manage.py migrate
python manage.py runserver
```
Now, visit **http://127.0.0.1:8000/** in your browser.

## 📸 Dynamic Images with Unsplash API
EliteMart dynamically fetches product category images from Unsplash. To enable this:
1. Get an Unsplash API Key from [Unsplash Developers](https://unsplash.com/developers)
2. Add it to your Django settings:
```python
UNSPLASH_ACCESS_KEY = 'your_api_key_here'
```

## 💡 Contribution Guide
Want to improve EliteMart? Follow these steps:
1. **Fork the repo**
2. **Create a branch** (`feature-new`)
3. **Make your changes & commit**
4. **Push to your fork & create a PR**

## 📜 License
This project is licensed under the **MIT License**.

---
🔗 **Follow Me on GitHub:** [@AmoghShukla](https://github.com/AmoghShukla)

