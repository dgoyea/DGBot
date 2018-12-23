from pandas.io import sql
import mysql.connector

class dgdbwriter:
     
    def __init__(self):
        self.mysql_con = mysql.connector.connect(host='127.0.0.1', port='3306', user='dgmysqlbatch', db='dgbot')
        self.dbcursor = self.mysql_con.cursor()
    
    def store_tick(self, dtstamp, pair, price):
        
        # Assemble the table name to store the tick into based on pair passed in
        dgTableName = 'dgbot.pol_' + pair + '_tick'
        dgTableName = dgTableName.lower()
        
        # SQL used to insert into table with placeholders for values.
        add_tick = ("INSERT INTO %(dgTableName)s "
                      "(date_time_stamp, price) "
                      "VALUES ('%(dtstamp)s', %(price)s)")
        
        # dict to add values into SQL
        data_tick = {
            'dgTableName' : dgTableName,
            'dtstamp' : dtstamp,
            'price' : price}
        
        sqlinsert = add_tick % data_tick
        
        self.dbcursor.execute(sqlinsert)
        self.mysql_con.commit()
                
                
        return
        
    def close_conn(self):
        self.mysql_con.close()

