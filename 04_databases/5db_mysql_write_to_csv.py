#!/usr/bin/env python3
import csv
import MySQLdb
import sys

output_file = sys.argv[1]

con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', \
        user='root', passwd='my_password')
c = con.cursor()

filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

c.execute("""SELECT * FROM Suppliers WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
