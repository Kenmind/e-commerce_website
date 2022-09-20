web: gunicorn --bind 0.0.0.0:$PORT The_Masterminds_Store.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
