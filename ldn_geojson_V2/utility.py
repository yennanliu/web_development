# python 3 
import csv
import sqlite3
import json

# --------------------



def csv_2_array(file):
	with open(file, 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)

	print(your_list)
	return your_list


def sqlite_2_array(db_name):
	conn = sqlite3.connect('car_data.db')
	#conn.row_factory = lambda cursor, row: [row[0]]
	# tranform python sqlite3 output from  tuple to array 
	conn.row_factory = lambda cursor, row: [row[x] for x in range(5)]
	c = conn.cursor()
	sql_get_car_date = """SELECT * FROM car_data"""
	print (sql_get_car_date)
	# tranform python sqlite3 output from  tuple to array 
	# https://stackoverflow.com/questions/2854011/get-a-list-of-field-values-from-pythons-sqlite3-not-tuples-representing-rows
	output = list(c.execute(sql_get_car_date).fetchall())
	conn.close()
	print (output)
	return output



def sqlite_2_json(db_name):
	# http://www.cdotson.com/2014/06/generating-json-documents-from-sqlite-databases-in-python/
	connection = sqlite3.connect(db_name)
	connection.row_factory = dict_factory
	cursor = connection.cursor()
	cursor.execute("select * from car_data")
	# fetch all or one we'll go for all.
	results = cursor.fetchall()
	connection.close()
	print (results)
	# save output to json 
	with open('car_data.js', 'w') as outfile:
		json.dump(results, outfile)
	return results




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 

# --------------------

	 


if __name__ == '__main__':
	#csv_2_array('car_data.csv')
	sqlite_2_array('car_data.db')
	print ('----------------')
	sqlite_2_json('car_data.db')














