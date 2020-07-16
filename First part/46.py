import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

# db.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE
# )
# ''')

# cursor.execute("INSERT INTO users "
#                "(name, email) VALUES ('Ivanov Ivan', 'ivanov@gmail.com')")
# cursor.execute("INSERT INTO users "
#                "(name, email) VALUES ('Refail Raly', 'ren23143@gmail.com')")
# cursor.execute("INSERT INTO users "
#                "(name, email) VALUES ('Lili Fox', 'lagacy@gmail.com')")
# cursor.execute("INSERT INTO users "
#                "(name, email) VALUES ('Nich Fame', 'nidck@gmail.com')")

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ('Gary Gail', 'lamen@gmail.com');
# INSERT INTO users (name, email) VALUES ('Nafaley', 'charlys@gmail.com');
# ''')

# users = [
#     ('User 1', 'user1@gmail.com'),
#     ('User 2', 'user2@gmail.com'),
#     ('User 3', 'user3@gmail.com'),
# ]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

db.commit()


db.close()

