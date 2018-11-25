import numpy as np
import pandas as pd

web_dict = {'Day': [9267089, 9284094,4687374, 4318033,5906301,6879014],
                   'Visitors':[12,22,31,41,67,65],
                   'Bounce Rate':[65,67,78,89,12,33]
                   }
df=pd.DataFrame(web_dict)
#df.set_index('Days',inplace=True)
#print(df[['Day','Visitors']])
#print(np.array(df[['Day','Visitors']]))
#print(df.head(2))
#print(df.Visitors.tolist())
#df2=pd.DataFrame(np.array(df[['Day','Visitors']]))
#print(df2)
