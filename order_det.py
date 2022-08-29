import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ICS-LAP-6681\SQLEXPRESS;'
                      'Database=POCTDM;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
create table order_det
(Ord_ID int, Ord_Address varchar(30), Ord_Item varchar(30), Ord_Price int, 
Cust_ID int foreign key references customer_det(Cust_ID))
''')

cursor.execute('''
               insert into order_det(Ord_ID, Ord_Address, Ord_Item, Ord_Price, Cust_ID)
               values
               (01008, 'SanJose', 'Monitor', 5000, 0022),
               (01013, 'NewYork', 'Mother Board', 3200, 0219),
               (01015, 'London', 'Keyboard', 2000, 0037),
               (01019, 'Bangalore', 'Laptop', 50000, 0474),
               (01026, 'Brisban', 'Smartwatch', 3000, 0365),
               (01031, 'Chennai', 'Mobile', 20000, 0121)
               ''')

conn.commit()