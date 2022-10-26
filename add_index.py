from faker import Faker
from pymysql import connect


connection = connect(host='localhost',
                    port=3366,
                    user='flask',
                    password='ksalf',
                    db='social_network')

with connection.cursor() as cursor:
    with open('index.sql', 'r') as f:
        cursor.execute(f.read())
    
connection.commit()
connection.close()

print("Have successfully added index!")