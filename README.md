# Lab-s-django
## 📚 Django Bookstore - ITI Tasks

### ✅ Overview

This Django project is a **bookstore management system** built as part of ITI Django Labs. It includes full integration with the Django admin panel, validation logic, authentication & authorization, and advanced model relationships. The project is split into 3 tasks that gradually build up the system.

---

### 🚀 Tasks Summary

#### 🔆 Task 1: Book-User-Category-ISBN Relations

✅ Implemented the following requirements:

* Each `Book` is linked to a Django `User`.
* Each `Book` can belong to **one or more `Category`** (Many-to-Many relation).
* Each `Book` has a **unique `ISBN`** (One-to-One relation).
* Each `ISBN` has:

  * `author`
  * `book_title`
  * `ISBN number` (auto-generated using UUID)

🧠 **Validation** (Both in Admin & Views):

* Book title: 10–50 characters.
* Category name: Minimum 2 characters.

🛠️ Admin Enhancements:

* Filter books by title, user, and category.
* Used `StackedInline` to manage ISBN inline within the Book admin.

---

#### 🔆 Task 2: Admin Panel Customization

🛠️ Enhanced the Django admin panel to include:

* Custom list display for `Book`, `Category`, and `ISBN`.
* Filtering by fields like user, category, and title.
* Inlined `ISBN` model inside `BookAdmin` using `StackedInline`:

  ```python
  class ISBNInline(admin.StackedInline):
      model = ISBN
      can_delete = False
  ```

📌 Result:

* Improved admin usability and productivity when managing book records.

---

#### 🔆 Task 3: Authentication & Authorization

🔐 **Implemented User Authentication:**

* Users can **sign up**, **log in**, and **log out**.
* Used Django's built-in `LoginView`, `LogoutView`, and `UserCreationForm`.

🔒 **Protected Views**:

* Certain views require login using `@login_required`.
* Other views restricted by **permissions** using `@permission_required`.

📡 **Signal System (Bonus)**:

* Automatically creates an `ISBN` for every new book using `post_save`:

  ```python
  @receiver(post_save, sender=Book)
  def create_isbn_for_book(sender, instance, created, **kwargs):
      if created:
          ISBN.objects.create(book=instance, author='Default Author', book_title=instance.title)
  ```

---

### 🧪 How to Run Locally

```bash
# Clone the project
git clone https://github.com/yourname/bookstore.git
cd bookstore

# Create virtual environment
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

---
