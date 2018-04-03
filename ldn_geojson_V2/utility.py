# python 3 


import csv


def csv_2_array(file):
	with open(file, 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)

	print(your_list)
	return your_list





if __name__ == '__main__':
	csv_2_array('car_data.csv')