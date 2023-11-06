# DigitalDive Blog

DigitalDive is a technology blog powered by Django, styled with Tailwind CSS and Flowbite. This repository contains the source code and resources for the website.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Overview

DigitalDive is a technology blog built with Django, a high-level Python web framework. The blog is designed to provide a platform for sharing tech-related articles and information with the community. It is styled with Tailwind CSS for a modern and responsive user interface and utilizes Flowbite for some additional UI components.

## Features

- User-friendly and responsive design.
- Create, edit, and delete blog posts (admin only).
- Markdown support for blog post content (provided by embed CKEditor).
- Easy customization and theming with Tailwind CSS and Flowbite.

## Getting Started

Follow the steps below to set up the project on your local machine.

### Requirements

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/) (3.9 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/maks-kovpak/django-website.git
   ```

2. Change into the project directory:

   ```shell
   cd django-website
   ```

3. Create a virtual environment using `virtualenv`:

   ```shell
   virtualenv .venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```shell
   .venv\Scripts\activate
   ```

   On MacOS and Linux:

   ```shell
   source .venv/bin/activate
   ```

5. Set needed environment variables from `.env.example`

6. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

7. Migrate the database:

   ```shell
   python manage.py migrate
   ```

8. Start the development server:

   ```shell
   python manage.py runserver
   ```

9. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Django website.

## Usage

- Create a superuser to access the admin panel:

  ```bash
  python manage.py createsuperuser
  ```

- Access the admin panel at `http://localhost:8000/admin` to manage blog posts and user accounts.

- Create, edit, and delete blog posts through the web interface.

- Customize the appearance of the website by modifying the Tailwind CSS and Flowbite styles if you want.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it for your own projects.
