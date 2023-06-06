mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
create:
	python3 manage.py createsuperuser

del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
run:
	python3 manage.py runserver