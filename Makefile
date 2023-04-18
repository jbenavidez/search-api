init:
	python3 manage.py runserver

plant_seed:
	python3 manage.py seed

django_migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

lint:
	flake8