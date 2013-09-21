rm database.sqlite
echo "no" | python manage.py syncdb
python manage.py sampledatafiller
