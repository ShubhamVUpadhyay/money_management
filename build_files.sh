 echo "BUILD START"
 python3.8.3 -m pip install -r requirements.txt
 python3.8.3 manage.py collectstatic --noinput --clear
 echo "BUILD END"
