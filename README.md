# Network - Social Network Project

## Overview
**Network** is a Twitter-like social network web application that allows users to create posts, follow other users, like/unlike posts, and edit their own posts. This project was developed as part of the CS50W course on web programming with Python and JavaScript.

## Features
- **User Authentication**: Users can register, log in, and log out securely.
- **Create Posts**: Authenticated users can create text-based posts.
- **View All Posts**: All users can view a feed of all posts in reverse chronological order.
- **Profile Pages**: Clicking on a username displays the user’s profile, including their posts and follower statistics.
- **Follow/Unfollow**: Users can follow or unfollow other users.
- **Following Feed**: Users can view posts from the users they follow.
- **Edit Posts**: Users can edit their own posts directly from the feed.
- **Like/Unlike Posts**: Users can like or unlike posts, with real-time updates to the like count.
- **Pagination**: Posts are paginated, displaying 10 posts per page.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (with Fetch API for AJAX functionality)
- **Database**: SQLite
- **CSS Framework**: Bootstrap 4

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/andrewkdev/network.git
   cd network
   ```
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser for the Django admin panel**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
7. **Access the application**: Open http://127.0.0.1:8000/ in your web browser.

## Usage
1. **Register**: Create a new account or log in with an existing account.
2. **Create Posts**: Use the text area at the top of the feed to post your thoughts.
3. **Profile Pages**: Click on usernames to view their profile and posts.
4. **Follow Users**: Follow or unfollow users from their profile page.
5. **View Following Feed**: Click on the "Following" link in the navbar to view posts by users you follow.
6. **Like and Edit Posts**: Interact with posts by liking/unliking them or editing your own posts.

## Screenshots
![Homepage](https://github.com/user-attachments/assets/493c3879-9a0d-479d-a4b3-2ff899ec1d3f)
![Profile](https://github.com/user-attachments/assets/fd0d00b4-e296-4f81-b9cc-d2905fb8c6a0)
![Following](https://github.com/user-attachments/assets/70610bf5-848e-4e30-8ad1-3e92fe235f0a)

## Project Structure
- `network/`: The main app containing models, views, and templates.
- `static/network/`: Contains static files like CSS and JavaScript.
- `templates/network/`: HTML templates for rendering pages.
- `db.sqlite3`: SQLite database file.

## Features in Action
- **Real-time updates**: Liking/unliking posts updates the like count without refreshing the page.
- **Edit functionality**: Edit posts in-place and save changes seamlessly.
- **Pagination**: Efficiently displays posts 10 at a time for all feeds.
