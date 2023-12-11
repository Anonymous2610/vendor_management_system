# Vendor Management System

The Vendor Management System is a Django-based application that handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Getting Started
Follow these instructions to set up and run the project on your local machine.

### Installation

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

The project is now running at `http://localhost:8000/`.

## Usage

- Access the Django admin interface at `http://localhost:8000/admin/` to manage vendors, purchase orders, and other models.
- Explore the API endpoints:
  - Vendors: `http://localhost:8000/api/vendors/`
  - Purchase Orders: `http://localhost:8000/api/purchase_orders/`

## Testing

Run the test suite to ensure the project is working correctly:

```bash
python manage.py test
```
