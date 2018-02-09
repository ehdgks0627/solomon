rm -r Char/migrations
rm -r Contact/migrations
rm -r Contract/migrations
rm -r Order/migrations
rm -r Product/migrations
rm -r Project/migrations
rm -r Review/migrations
rm -r User/migrations
rm db.sqlite3
python manage.py makemigrations
python manage.py makemigrations Chat
python manage.py makemigrations Contact
python manage.py makemigrations Contract
python manage.py makemigrations Order
python manage.py makemigrations Product
python manage.py makemigrations Project
python manage.py makemigrations Review
python manage.py makemigrations User
python manage.py migrate
