import psycopg2

#Connect to an existing database

testConnect = psycopg2.connect(user="postgres",
    password="shitonme",
    host="127.0.0.1",
    port="5432",
    database="testDB")
testConnect.autocommit = True
#(referring to .cursor)Cursor class is an instance using which you can invoke methods that execute SQLite statements, 
# fetch data from the result sets of the queries. 
# You can create Cursor object using the cursor() method of the Connection object/class.
cursor = testConnect.cursor()
    # SQL query to create a new table
#create_table_query = '''CREATE TABLE Userdata
          #(ID INT PRIMARY KEY     NOT NULL,
         # users           TEXT    NOT NULL,
         # password         character varying); '''
# Execute a command: this creates a new table
#cursor.execute(create_table_query)
#testConnect.commit()

#insert_query = """ INSERT INTO Userdata (ID, users, password) VALUES (1, 'Abhisek Rai', '1234')"""
#cursor.execute(insert_query)

update_query = """ UPDATE Userdata SET ID = '1' WHERE ID = '2'"""
cursor.execute(update_query)
testConnect.commit()
print("1 Record updated successfully")

insert_query = """ INSERT INTO Userdata (ID, users, password) VALUES (2, 'Natasha Ho', '5678')"""
cursor.execute(insert_query)

#FETCH RESULT
select_query = "select * from Userdata"
cursor.execute(select_query)
data_fetch_from_db = cursor.fetchall()
print("data from table", data_fetch_from_db)


if (testConnect):
    print("Connected to Database")    