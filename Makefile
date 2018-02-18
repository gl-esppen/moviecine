install:
	pip install -r requirements.txt
	python moviecine/manage.py migrate
	python moviecine/manage.py createsuperuser
	python moviecine/manage.py collectstatic

migrations:
	python moviecine/manage.py makemigrations
	python moviecine/manage.py migrate

user:
	python moviecine/manage.py createsuperuser

run:
	python moviecine/manage.py runserver

