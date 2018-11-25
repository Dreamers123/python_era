import pandas as pd

df = pd.read_csv('ZILL-Z77006_3B.csv',names=['Abeer','Jannat'])
print(df.head())
#df.rename(columns={'Jannat':'Jannatul'}, inpalce=True)
#index_col=0 means ) will be the index column
#df2=pd.read_csv('ZILL-Z77006_3B.csv',index_col=0)
#print(df2.head())
#df2.columns=['Austin HPI']
#print(df2.head())
#df2.to_html('example.html')

#again save it to a new csv and you can make header=False
#df.to_csv('new.csv')