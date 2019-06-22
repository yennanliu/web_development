import sqlite3

def creat_db():
	# create db 
	conn = sqlite3.connect('database.db')
	print ('Opened database successfully')
	# create table
	conn.execute('CREATE TABLE IF NOT EXISTS products (id INT, title TEXT, description TEXT, sold TEXT)')
	print ('Table created successfully')
	# insert data
	try: 
		with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO products (id, title, description, sold) VALUES (?,?,?,?)",  (1, 'applie pie', 'this is an apple pie', 'false'))
				cur.execute("INSERT INTO products (id, title, description, sold) VALUES (?,?,?,?)", (2, 'chicken burger', 'yammy chicken burger', 'true'))
				con.commit()
				print ('Insert data OK')
	except Exception as e:
		con.rollback()
		print (str(e) + 'error within insert process')

if __name__ == '__main__':
	creat_db()
