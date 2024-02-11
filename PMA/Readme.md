# Background

The author has designed and developed an interactive web application designed to provide users with a full range of services at the University of Warwick's in-house catering restaurant, Ganapathi Catering. The focus of the application is to introduce the restaurant, including a description of the restaurant, the menu, the services available, the booking function and contact details. It aims to provide users with a convenient and efficient dining experience.

# Install

1. Install Python packages

```
pip install Flask pytest
```

2. Run using command

```
python app.py
```

# Catalogue Structure Description

```
├── static/
│   ├── assets/
│   │   ├── css/
│   │   │   ├── login.css
│   │   │   └── main.css
│   │   ├── img/
│   │   │   └── (Multiple photos used on the website)
│   │   ├── js/
│   │   │   └── main.js
│   │   └── vender/
│   │       └── (Files configured to fit different browsers)
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── success.html
│   │   └── success-contact.html
│   ├── tests/
│   ├── conftest.py
│   └── test.py
├── app.db
├── Readme.md
└── app.py
```

# References

https://bootstrapmade.com/yummy-bootstrap-restaurant-website-template/