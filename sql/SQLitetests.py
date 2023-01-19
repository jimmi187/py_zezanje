import sqlite3
conn = sqlite3.connect("sql/my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends 
# 					VALUES ('Merriwether', 'Lewis', 7)'''

# BAD! DO NOT DO THIS!
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))

data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)



people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]

# for person in people:
# 	insert that one person
average = 0
for person in people:
	c.execute("INSERT INTO friends VALUES (?,?,?)", person)
	average += person[2]
print(average/len(people))

# Insert all at once
# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

##################### SELECT  ######################################################################
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")


# Iterate over cursor
# for result in c:
# 	print(result)

# Fetch One Result
# print(c.fetchone())

# Fetch all results as list
print(c.fetchall())

##################### SQK INJECTION  ######################################################################
conn = sqlite3.connect("users.db")
# query = "CREATE TABLE users (username TEXT, password TEXT)"
u = input("please enter your username...")
p = input("please enter your password...")
c = conn.cursor()

# THE BAD WAY!
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"

# THE MUCH SAFER WAY
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query,(u,p))

result = c.fetchone()
if(result):
	print("WELCOME BACK")
else:
	print("FAILED LOGIN")

# commit changes
conn.commit()
conn.close()