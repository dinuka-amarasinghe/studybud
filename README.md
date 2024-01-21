# StudyBud: Django Discord-Like Application

StudyBud is a web application built with Django that mimics the functionality of Discord, focusing on educational
topics. Users can register, log in, and create chat rooms dedicated to specific educational subjects. This project
served as a learning experience for various aspects of Django web development.

## Features

- **User Authentication:** Utilized Django's built-in authentication system and implemented a custom user model for user
  registration and login.
- **Custom User Models:** Explored the creation and usage of a custom user model to extend user attributes and enhance
  authentication.
- **Function-Based Views (FBVs):** Implemented views using Django's function-based approach to handle different aspects
  of the application.
- **Database Migrations:** Employed Django's migration system to manage database schema changes and updates.
- **Template System:** Utilized Django's template engine to create dynamic and responsive HTML templates for rendering
  views.
- **Chat Rooms:** Implemented the core functionality of creating and participating in chat rooms, focusing on
  educational topics.

## Getting Started

Follow these steps to get the StudyBud project up and running on your local machine:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/studybud.git
    cd studybud
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Database Migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

5. **Visit the Application:**
   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) - Localhost

## Acknowledgments

This project was created by following the fantastic tutorial series by [Dennis Ivy](https://www.dennisivy.com/).

- Dennis Ivy's YouTube Channel: [Dennis Ivy](https://www.youtube.com/c/DennisIvy)
