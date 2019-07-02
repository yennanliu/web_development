from model import *

# insert data into db 
title = 'juice' 
description = 'this is an apple juice'
sold = 'True'

insert_data = ProductData(title=title, description=description, sold=sold)
db.session.add(insert_data)
db.session.commit()
print ('insert data to DB ok')
