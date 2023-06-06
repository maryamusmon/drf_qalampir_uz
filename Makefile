mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
create:
	python3 manage.py createsuperuser