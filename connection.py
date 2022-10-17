import pymysql

#connection = pymysql.connect("localhost", user="", passwd="", database="GTD");

connection = pymysql.connect("localhost", "frederik.lindsey", " ", "GTD");

cursor = connection.cursor();

sql_query = "SELECT VERSION()";

try :
    cursor.execute( sql_query);
    data = cursor.fetchnone();
    print("Database Version: %s" %data);

except Exception as e:
    print("Exception: ", e);

connection.close();

