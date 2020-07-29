import sqlite3 as sl

con = sl.connect('my-database.db')

import pandas as pd
df_emp = pd.DataFrame({'empid': [1,2,3,4],'name':['Ishu','Jai','Lisa','Marilyn']})
"""
  index empid name
0 0     1     Ishu
1 1     2     Jai
2 2     3     Lisa
3 3     4     Marilyn
"""
# below code will insert df_emp dataframe into 'EMP' table with con object
df_emp.to_sql('EMP',con)

#reading below query output to data_df dataframe
data_df = pd.read_sql('''
SELECT * FROM EMP''',con)
