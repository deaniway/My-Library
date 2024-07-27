# MyL📚ibrary

The application is a simplified analogue of the CRM system for the library.

The project implements 2 user entities - Librarian and Reader, each of which has its own functionality.
Also implemented API and an improved ADMIN PANEL

#### Minimum Requirements:

- [x] Python
- [x] Poetry
- [x] Django
- [x] PostgreSQL
- [x] Docker

### This is  use next tools:

| Tools                         | Version |
|-------------------------------|---------|
| Python                        | ^3.11   |
| Django                        | ^5.0.7  |
| django-bootstrap5             | ^24.2   |
| djangorestframework           | ^3.15.2 |
| djangorestframework-simplejwt | ^5.3.1  |
| drf-yasg                      | ^1.21.7 |
| dj-database-url               | ^2.2.0  |
| python-dotenv                 | ^1.0.1  |
| django-simple-history         | ^3.7.0  |
| psycopg2-binary               | ^2.9.9  |

### To get started, you need to perform the following operations:

| Step |                                   Instruction                                    |
|:----:|:--------------------------------------------------------------------------------:|
|  1   | Clone he repository to your PC:<br/>`https://github.com/deaniway/My-Library.git` |
|  2   |                       Go to repository<br/>`cd My-Library`                       |
|  3   |          Installing the application on your computer<br/>`make install`          | 
|  4   |   Run the command to create tables<br/>`make makemigrations` /  `make migrate`   | 
|  5   |                  Create superuser, use the<br/>`make superuser`                  |
|  6   |                To start the Django server, use the<br/>`make dev`                |

### *You must have:*

- [Poetry](https://python-poetry.org)

- [Django](https://www.djangoproject.com/)

- [Django REST Framework](https://www.django-rest-framework.org/)

- [Django simple history](https://django-simple-history.readthedocs.io/)

- [drf-yasg](https://drf-yasg.readthedocs.io/)

- [PostgreSQL](https://www.postgresql.org/)

- [Docker](https://www.docker.com/)

## How to deploy a database?

#### Create .env file in sources root and fill it (example)

```dotenv

DATABASE_URL=postgresql://pguser:pgpass@localhost:5434/yourdatabase

```

#### Up postgres DB (Docker for example):

```sh
make dev-db
```

#### Run local server:

```shell
make dev
```

## What are the API requests?

- #### The project implements swagger, use it to learn more about the API capabilities

### Contributing

