import mysql.connector as sql
class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = sql.connect(host='localhost', database='LoanManagementSystem', user='root', password='Naveen_mysql29')
            return connection
        except Exception as e:
            print(f"Unable to connect to the database-{e}")
            return None
