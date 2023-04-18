
init:
	rm -rf env; virtualenv -p python3.8 env

active:
	source env/bin/activate

install_devs:
	pip3 install -r requirements.txt

run:
	python3 manage.py runserver

plant_seed:
	python3 manage.py seed

django_migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

lint:
	flake8