from faker import Faker
from pymysql import connect


connection = connect(host='localhost',
                    port=3366,
                    user='flask',
                    password='ksalf',
                    db='social_network')

# run initial migration
with connection.cursor() as cursor:
    with open('init_db.sql', 'r') as f:
        cursor.execute(f.read())
    
    connection.commit()

    print("Have successfully executed initial migration!")

    # add test data
    fake = Faker()
    for i in range(1_000):
        for j in range(1_000):
            cursor.execute('''INSERT INTO 
                profiles(firstName, secondName) VALUES(%s,%s)''',
                    (fake.first_name(), fake.last_name()))
        connection.commit()
        print("Have committed "+str((i+1)*1_000)+" profiles")

connection.close()

print("Success!")