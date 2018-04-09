# python 3 


import csv
import sqlite3

def csv_2_array(file):
	with open(file, 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)

	print(your_list)
	return your_list




def sqlite_2_array(db_name):
	output=[]
	conn = sqlite3.connect(db_name)
	c = conn.cursor()
	sql_get_car_date = """SELECT * FROM car_data"""
	print (sql_get_car_date)
	for row in c.execute(sql_get_car_date):
		print (row)
		output.append(row)
	print ('------------')
	print (output)
	return output




if __name__ == '__main__':
	#csv_2_array('car_data.csv')
	sqlite_2_array('car_data.db')







