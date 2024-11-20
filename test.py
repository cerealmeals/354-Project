import pymssql

conn = pymssql.connect(host='cypress.csil.sfu.ca', user='s_shn9', password='2dNE3LgrFjMde36t', database='shn9354')

cursor = conn.cursor(as_dict=True)

cursor.excute('SELECT TOP(10) * FROM dbo.User_yelp')

for row in cursor:
    print('row:', row)