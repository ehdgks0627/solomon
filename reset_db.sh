rm -r chat/migrations
rm -r contact/migrations
rm -r contract/migrations
rm -r order/migrations
rm -r product/migrations
rm -r oroject/migrations
rm -r review/migrations
rm -r user/migrations
rm db.sqlite3
python manage.py makemigrations
python manage.py makemigrations chat
python manage.py makemigrations contact
python manage.py makemigrations contract
python manage.py makemigrations order
python manage.py makemigrations product
python manage.py makemigrations project
python manage.py makemigrations review
python manage.py makemigrations user
python manage.py migrate
