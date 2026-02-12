# Coffee Shop

A Django web application for managing a coffee shop, including product catalog, user authentication, and order management.

## Tech Stack

- Python 3.11
- Django 5.2
- PostgreSQL (AWS RDS)
- Tailwind CSS (CDN)
- Django REST Framework
- Crispy Forms + Crispy Tailwind

## Features

- **Products**: Browse a product catalog with images, descriptions, and prices
- **Orders**: Add products to your order and view order details
- **Authentication**: User registration, login, and logout
- **Admin Panel**: Manage products, orders, and users
- **REST API**: Product list API endpoint
- **SEO**: Meta tags, Open Graph, and Twitter Cards

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ircorona/django-coffee-shop.git
   cd django-coffee-shop
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv ~/.envs/coffee_shop
   ~/.envs/coffee_shop/Scripts/Activate.ps1  # Windows PowerShell
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DJANGO_DB_URL=postgres://user:password@host:5432/dbname
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
projects/
├── coffee_shop/        # Project settings and main URLs
├── products/           # Product catalog app
├── orders/             # Order management app
├── users/              # Authentication (login, logout, register)
├── templates/          # Project-level templates (base.html)
├── media/              # User-uploaded files
└── requirements.txt
```

## URLs

| URL | Description |
|-----|-------------|
| `/products/` | Product list |
| `/products/add/` | Add a new product |
| `/products/api/` | Product list API |
| `/orders/my-orders/` | View your order |
| `/orders/add-product/` | Add product to order |
| `/users/login/` | Login |
| `/users/logout/` | Logout |
| `/users/register/` | Register |
| `/admin/` | Admin panel |

## Running Tests

```bash
python manage.py test
```
