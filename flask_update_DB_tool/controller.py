# python 3 


import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os
import pandas as pd


def get_toy_data(input):
	#print (' input : ', input)
	#print (' data : ', 123)
	data = pd.DataFrame({'name':[100,120,150] ,'url':[100,120,300] })
	print ('data : ' , data )
	return data 


def get_DB_data(sql, db_url):
    try:
        engine = create_engine(db_url)
        print (sql)
        df = pd.read_sql(sql=sql, con= engine)
        print (df.head())
        return df 
        print("extract data ok")
    except Exception as e:
        print (e)
        print ('fail to get data from db')




def get_access_request_report(memeber_id,db_url):
    # xlsxwriter write multiple dataframe to one xls
    # https://stackoverflow.com/questions/32957441/putting-many-python-pandas-dataframes-to-one-excel-worksheet
    # sql
    sql_member_inform="""select * from ana.members where member_id = '{}' ;"""
    sql_member_inform = sql_member_inform.format(memeber_id)
    print (sql_member_inform)
    sql_membership_event ="""select * from ana.membership_events where member_id = '{}' ;"""
    sql_membership_event = sql_membership_event.format(memeber_id)
    print (sql_membership_event)
    sql_member_booking="""select * from ana.bookings where member_id = '{}' ;"""
    sql_member_booking = sql_member_booking.format(memeber_id)
    print (sql_member_booking)
    sql_member_trips="""select * from prc.trips where member_id = '{}' ;"""
    sql_member_trips = sql_member_trips.format(memeber_id)
    print (sql_member_trips)
    sql_member_transactions="""select * from prc.transactions where member_id = '{}' ;"""
    sql_member_transactions = sql_member_transactions.format(memeber_id)
    print (sql_member_transactions)
    # extract data
    df_member_inform= get_DB_data(sql_member_inform ,db_url)
    df_membership_event= get_DB_data(sql_membership_event ,db_url)
    df_member_booking= get_DB_data(sql_member_booking ,db_url)
    df_member_trips= get_DB_data(sql_member_trips ,db_url)
    df_member_transactions= get_DB_data(sql_member_transactions ,db_url)
    # create xls writer
    writer = pd.ExcelWriter('access_req_report_sample.xlsx',engine='xlsxwriter')  
    workbook=writer.book
    # save to excel xlsx file 
    df_member_inform.to_excel(writer,sheet_name='df_member_inform',startrow=0 , startcol=0)  
    df_membership_event.to_excel(writer,sheet_name='df_membership_event',startrow=0, startcol=0)
    df_member_booking.to_excel(writer,sheet_name='df_member_booking',startrow=0, startcol=0)
    df_member_trips.to_excel(writer,sheet_name='df_member_trips',startrow=0, startcol=0)
    df_member_transactions.to_excel(writer,sheet_name='df_member_transactions',startrow=0, startcol=0)






