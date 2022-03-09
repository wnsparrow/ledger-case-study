# api

A minimal Django REST Framework based API server for returning auto policy data. 

## Initial set up

```bash
docker-compose up --build
docker-compose exec api ./manage.py migrate
docker-compose exec api ./manage.py load_auto_policies --max 20000 ./data/auto_policies.csv
```

## Other useful commands
```bash
# migrations
docker-compose exec api ./manage.py makemigrations
docker-compose exec api ./manage.py migrate

# to run a shell inside the container
docker-compose exec api /bin/bash

# reload data
docker-compose exec api ./manage.py load_auto_policies --max 20000 ./data/auto_policies.csv

# create superuser
docker-compose exec api ./manage.py createsuperuser
```

## Project Structure

* `api/` - Base Django project
* `policies/` - Django application for policies
* `data/` - Data directory

## Notes

* You may add/modify/refactor this project in any way to help your frontend client
* You may use any libraries that you find useful
* You do not be concerned with CSRF or authentication
* Depending on how you access the API from your client app, you might need to install middleware to handle CORs. I
  recommend using [`django-cors-headers`](https://pypi.org/project/django-cors-headers/).
