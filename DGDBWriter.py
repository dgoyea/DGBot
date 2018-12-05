from pandas.io import sql
import mysql.connector


mysql_con = mysql.connector.connect(host='127.0.0.1', port='3306', user='dgmysqlbatch', db='dgbot')
mysql_con.close()

 
