import sqlite3

conn = sqlite3.connect('blogdata.db')
print "Opened database successfully";

conn.execute('CREATE TABLE  myblogs(title TEXT PRIMARY KEY, blog TEXT)')
print "Table created successfully";
conn.close()