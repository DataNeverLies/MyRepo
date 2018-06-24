import mysql.connector
_connection = None

def get_connection():
    global _connection
    if not _connection:
        _connection = mysql.connector.connect(user='root', password='swaroop@18',
                                      host='127.0.0.1',
                                      database='mydb')
    return _connection

# List of stuff accessible to importers of this module. Just in case
__all__ = [ 'getConnection' ]
