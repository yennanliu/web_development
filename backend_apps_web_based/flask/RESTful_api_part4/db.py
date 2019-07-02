from model import *

# define to-insert db (will do that via sql/shell in the next update maybe)
prod_data = [ {'title': 'juice',
			 'description':'this is an apple juice',
			 'sold':'True'}, 
			  {'title': 'milk',
			 'description':'this is a milk',
			 'sold':'False'},
			  {'title': 'salad',
			 'description':'this is a salad',
			 'sold':'True'}]
             
# insert data into db 
for data in prod_data:
	insert_data = ProductData(title=data['title'], 
							  description=data['description'], 
							  sold=data['sold'])
	db.session.add(insert_data)
	db.session.commit()
	print ('insert data to DB ok')
