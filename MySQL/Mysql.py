# import mysql.connector
import pandas as pd
import Connection
conn = Connection.get_connection()


class extract:

    def read_write_pandas(self,sql_string,table_name):
        df = pd.read_sql(sql_string, con=conn)
        df.to_csv(table_name+'.csv',index=False)
        # print df.to_string(index=False)

    def read_table_list(self):
        lines = open('TableList.txt').read().splitlines()
        for line in lines:
            sql_string = 'select * from ' + line
            self.read_write_pandas(sql_string,line)



myobj = extract()
myobj.read_table_list()
myobj.read_write_pandas()
