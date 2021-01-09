import psycopg2
from datetime import date

todoConnect = psycopg2.connect(user="postgres",
    password="shitonme",
    host="127.0.0.1",
    port="5432",
    database="todo")
todoConnect.autocommit = True

todoCursor = todoConnect.cursor()

# SQL query to create a new table
#create_table_query = '''CREATE TABLE TodoList
          #(ID INT PRIMARY KEY     NOT NULL,
       # Title           TEXT    NOT NULL,
       # DueDate         DATE NOT NULL,
       #  Priority TEXT NOT NULL); '''
#Execute a command: this creates a new table
#todoCursor.execute(create_table_query)

todo = (
    (1, "Homework", "2021-01-10", "High"),
    (2, "Laundry", "2021-01-15", "Low"),
    (3, "Coding", "2021-01-09", "High"),
    (4, "Report", "2021-01-12", "Medium"),
    (5, "Kids Excursion", "2021-01-30", "High"),
    (6, "Dinner Date", "2021-01-20", "High"),
    (7, "Gym", "2021-01-13", "Low"),
    (8, "ER", "2021-02-28", "High"),
    (9, "Shopping", "2021-01-28", "Low"),
    (10, "Fishing", "2021-02-13", "Low")
)

##insert_query = """ INSERT INTO TodoList (ID, "title", "duedate", "priority") VALUES (%s, %s, %s, %s)"""
#todoCursor.executemany(insert_query, todo)
today = date.today()
select_query = "SELECT * from TodoList WHERE duedate = 'today'"
todoCursor.execute(select_query)
data_fetch_from_db = todoCursor.fetchall()
#print data one by one
for data in data_fetch_from_db:
    print("Today: ", data)


select_query_high = "SELECT * from TodoList WHERE priority = 'High'"
todoCursor.execute(select_query_high)
data_fetch_from_db = todoCursor.fetchall()
#print data one by one
for data in data_fetch_from_db:
    print("High Priority: ", data)


output = open("todo.csv", 'w')
cur = todoConnect.cursor()
todoCursor.copy_to(output, 'TodoList', sep="|")


