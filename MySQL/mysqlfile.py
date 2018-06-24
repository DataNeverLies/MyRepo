# import pymysql
# import csv
#
# # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='swaroop@18', db='mydb')
# # print ('Conected!')
# # conn.close()
# conn = pymysql.connect(host='localhost',
#                              user='root',
#                              password='swaroop@18',
#                              db='mydb',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.SSCursor)
#
#
# cursor = pymysql.SSCursor(conn)
# cursor.execute('select * from mydb.employee')
# while True:
#     row = cursor.fetchone()
#     if row:
#         print row


import MySQLdb
connection=MySQLdb.connect(
    host="thehost",user="theuser",
    passwd="thepassword",db="thedb",
    cursorclass = MySQLdb.cursors.SSCursor)
cursor=connection.cursor()
cursor.execute(query)
for row in cursor:
    print(row)
