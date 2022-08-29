import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ICS-LAP-6681\SQLEXPRESS;'
                      'Database=POCTDM;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''create table customer_det
(Cust_ID int primary key, Cust_Name varchar(30), Cust_Age int, Cust_SSN int)
''')

cursor.execute('''
               insert into customer_det(Cust_ID, Cust_Name, Cust_Age, Cust_SSN)
               values
               (0037, 'Robert', 36, 489368350),
               (0022, 'Ashley', 41, 514148905),
               (0121, 'Thomas', 28, 690055315),
               (0219, 'Susan', 33, 421371396),
               (0365, 'Christ', 31, 458026124),
               (0474, 'Rick', 49, 612206832)
               ''')

conn.commit()