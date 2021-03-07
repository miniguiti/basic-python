import MySQLdb

host = "localhost"
user = "root"
password = "admin"
db = "world"
port = 3306

con = MySQLdb.connect(host, user,password, db, port)