from pandas.io import sql
import mysql.connector

class dgdbwriter:
     
    def __init__(self):
        self.mysql_con = mysql.connector.connect(host='127.0.0.1', port='3306', user='dgmysqlbatch', db='dgbot')
        self.dbcursor = self.mysql_con.cursor()
        self.dog = 'cat'
    
    def store_tick(self, pair, price):
        
        # Assemble the table name to store the tick into based on pair passed in
        dgTableName = 'dgbot.pol_' + pair + '_tick'
        dgTableName = dgTableName.lower()
        
        # SQL used to insert into table with placeholders for values.
        add_tick = ("INSERT INTO %(dgTableName)s "
                      "(price) "
                      "VALUES (%(price)s)")
        
        # dict to add values into SQL
        data_tick = {
            'dgTableName' : dgTableName,
            'price' : price}
        
        sqltest = add_tick % data_tick
        
        print(sqltest)
        
        self.dbcursor.execute(add_tick, data_tick)
        self.dbcursor.commit()
                
                
        return
        
    def close_conn(self):
        self.mysql_con.close()

#  
# 
# 
# 
# from __future__ import print_function
# from datetime import date, datetime, timedelta
# import mysql.connector
# 
# cnx = mysql.connector.connect(user='scott', database='employees')
# cursor = cnx.cursor()
# 
# tomorrow = datetime.now().date() + timedelta(days=1)
# 
# add_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
# 
# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
# 
# # Insert new employee
# cursor.execute(add_employee, data_employee)
# emp_no = cursor.lastrowid
# 
# # Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)
# 
# # Make sure data is committed to the database
# cnx.commit()
# 
# cursor.close()
# cnx.close()