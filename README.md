cd CARPETA
python -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy python-dotenv pymysql
pip freeze > requirements.txt
