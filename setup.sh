git clone https://github.com/koziez/surpay
cd surpay/
sudo pip install -r requirements.txt
django-admin.py startproject surpay
cp -r src/polls/ surpay/
cp -r src/static/ surpay/
cp src/surpay/* surpay/surpay/

cd surpay/
python3 manage.py makemigrations polls
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
