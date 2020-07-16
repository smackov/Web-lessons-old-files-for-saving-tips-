import sqlite3
db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

email = 'ivanov@gmail.com'

# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# res = cursor.fetchone()
# print(res)
# print(res[2])

cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'Nafalay'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :Nafalay", {'email': email, 'name': 'Nafalay'})
res = cursor.fetchone()
print(res)
print(res[2])

cursor.execute("SELECT * FROM users")
res = cursor.fetchall()
print(res)

for user in res:
    print(user[1], user[2])


db.close()











