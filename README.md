# Overview

The Habit Tracker web app was developed to help users monitor and maintain their daily habits, track progress over time, and stay motivated to achieve personal goals. The project allowed me to deepen my understanding of web development using Django, database management with models, user authentication, and interactive front-end features with JavaScript.

This web app allows users to:

- Create an account and log in.
- Add new habits with optional description and streak goals.
- Check off habits each day, with automatic tracking of daily completion.
- View historical habit logs and current streaks.
  -Celebrate streak goals with interactive confetti and a modal message.

How to run the app:

- Clone the repository and navigate into the project directory.
- Install dependencies (Python 3.x and Django 5.x required).
- Run the test server using:
  `python manage.py runserver`
- Open the browser at http://127.0.0.1:8000/ to see the home page.

[Software Demo Video](https://youtu.be/z95JwbYypgY)

# Web Pages

1. Home Page

   - Displays the user's habits for today.
   - Users can mark each habit as done or undone.
   - Provides links to add new habits or view the Habit Logs page.

2. Add Habit Page

   - Users can create a new habit with optional description and streak goal.
   - Upon submission, users are redirected to the home page.

3. Habit Logs Page

   - Shows all historical logs for each habit.
   - Displays streak information and a detailed history of completion.
   - Confetti animation and a congratulatory modal appear when a streak goal is reached.

4. Register Page

   - Allows new users to create an account.
   - Redirects to login after successful registration.

5. Login Page
   - Authenticates existing users.
   - Provides a link to the registration page for new users.

All pages dynamically render content based on the logged-in user and their data in the database.

# Development Environment

- Framework: Django 5.x
- Programming Language: Python 3.x
- Database: SQLite (default for Django, stores users, habits, and habit logs)
- Front-End: HTML, CSS, JavaScript
- Libraries and Tools:
  - Django built-in libraries (models, views, templates, authentication)
  - Google Fonts (Cause font)
  - Vanilla JavaScript for confetti animations and modals
- Editor/IDE: VS Code

# Useful Websites

- [Django Docs](https://docs.djangoproject.com/en/6.0/)
- [Confetti JS Library](https://confetti.js.org/)
- [Google Fonts](https://fonts.google.com/)

# Future Work

- Add the ability to edit existing habits (name, description, streak goal).
- Implement a calendar-style visualization of habit logs.
- Improve UI/UX with responsive design for mobile devices.
