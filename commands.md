python manage.py startapp <app name>
python manage.py makemigrations
python manage.py migrate

class Meta:
unique_together = ('pt', 'data', 'hora')
