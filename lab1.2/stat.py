from matplotlib import pyplot as plt
import pandas as pd
df = pd.ExcelFile('connection_transport.xlsx')
df1 = df.parse('Data')
#keys = df1.keys()
#for key in keys:
#  print(df1[key])

name1 = df1.loc[df1['Name/Index'] == 'ATS01_DC2_MSK_CONN3']
name2 = df1.loc[df1['Name/Index'] == 'ATS01_DC2_MSK_CONN1']

name1.plot(x="Timestamp", y=["RxOctets"], color='magenta')
name2.plot(x="Timestamp", y=["RxOctets"], color='brown')
plt.xlabel('Время')
plt.ylabel('Данные')
plt.legend(loc='best')
plt.show()
