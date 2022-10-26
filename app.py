from flask import Flask
from flask_mysqldb import MySQL
from faker import Faker


app = Flask(__name__)

app.secret_key = 'some_secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3366
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'ksalf'
app.config['MYSQL_DB'] = 'social_network'
 
mysql = MySQL(app)

fake = Faker()


@app.route("/profiles", methods = ['GET'])
def profiles():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT 
            firstName, 
            secondName
        FROM profiles
        WHERE firstName like %s and secondName like %s
        ORDER BY id''', [fake.first_name()[:2]+"%", fake.last_name()[:2]+"%"])
    profiles = cursor.fetchall()
    cursor.close()
    return [{ "firstName": profile[0], 
        "secondName": profile[1] } for profile in profiles], 200