# InstaClone

A small Instagram-style social app built with Django as a learning project.

## Features

- Sign up / log in with email as the username
- Post images with captions to a shared feed
- Search the feed by username
- User profiles with bio and profile picture
- Direct messaging between users (start a chat from someone's profile)

## Stack

- Django (Python) + SQLite
- Tailwind CSS for styling
- Font Awesome for icons

## Running it locally

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Notes

This started as a way to practice Django's auth system, model relationships,
and basic CRUD views. Styling uses the Tailwind CDN build for now rather than
a proper Tailwind build pipeline, since this is still a work in progress.
