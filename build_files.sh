echo "BUILD START"

# Use 'python3.8' instead of 'python3.8.3' (if it's installed as 'python3.8')
python3.8 -m pip install -r requirements.txt

# Create the 'staticfiles_build' directory if it doesn't exist
mkdir -p staticfiles_build

# Specify 'python3.8' for the 'manage.py' commands as well
python3.8 manage.py collectstatic --noinput --clear

echo "BUILD END"
