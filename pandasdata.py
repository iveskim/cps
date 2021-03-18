import pandas as pd
import pymysql
import numpy as np
from sqlalchemy import create_engine
import ffn
import datetime

conn = create_engine('mysql+pymysql://root:root@localhost:3306/stock?charset=utf8')
sql = "select * from dailybasicpool where ts_code = '603288.SH'"
df = pd.read_sql(sql=sql,con=conn,index_col='id',coerce_float=True,columns=True)
#df=pd.to_datetime(df['trade_date'],format="%Y/%m/%d")

#df['trade_date']=pd.to_datetime(df['trade_date'],format="%Y/%m/%d")

df['close'] = df['close'].astype('float64')

df = df.rename(columns={"trade_date": "date"})
df = df.rename(columns={"close": "value"})

#df = df.set_index('date')

#df = df.convert_objects(convert_numeric=True)


#df = df.rename(columns={"trade_date": "tradedate"})
print(df.columns.values)
#print(df.columns())
#print(df)
#df.resample('AS').groupby('trade_date').mean()

#print(df['id'])
#
# data = ffn.get('dbc', provider=ffn.data.csv, path='test_data.csv', existing=data)
# print data.head()

#ffn.to_returns(df)

#
# price = pd.Series([3.42,3.51,3.68,3.43,3.56,3.67], index=[datetime.date(2015,7,x) for x in range(3,9)])
# print(price)
# r = ffn.to_returns(price)
# print(r)


def getMaxDrawdown(x):
    j = np.argmax((np.maximum.accumulate(x) - x) / x)
    if j == 0:
        return 0
    i = np.argmax(x[:j])
    d = (x[i] - x[j]) / x[i] * 100
    return d

def applyMaxDrawdown(x):
    f = x.sort_values("date").reset_index()
    array = pd.Series(f["value"])
    return getMaxDrawdown(array)


print(applyMaxDrawdown(df))
