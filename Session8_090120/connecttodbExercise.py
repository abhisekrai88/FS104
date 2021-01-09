import psycopg2

#Connect to an existing database

testConnect = psycopg2.connect(user="postgres",
    password="shitonme",
    host="127.0.0.1",
    port="5432",
    database="testDB")
#(referring to .cursor)Cursor class is an instance using which you can invoke methods that execute SQLite statements, 
# fetch data from the result sets of the queries. 
# You can create Cursor object using the cursor() method of the Connection object/class.
cursor = testConnect.cursor()
    # SQL query to create a new table
create_table_query = '''CREATE TABLE Userdata
          (ID INT PRIMARY KEY     NOT NULL,
          users           TEXT    NOT NULL,
          password         character varying); '''
# Execute a command: this creates a new table
cursor.execute(create_table_query)
testConnect.commit()

insert_query = """ INSERT INTO Userdata (ID, users, password) VALUES (1, 'Abhisek Rai', '1234')"""
cursor.execute(insert_query)
testConnect.commit()
print("1 Record inserted successfully")


if (testConnect):
    print("Connected to Database")    