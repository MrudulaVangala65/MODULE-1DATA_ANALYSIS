import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("/content/Day2 temperature.xlsx")
df.to_csv("temperature.csv")
print(df)
mm=pd.read_csv("/content/temperature.csv")
avgtemp=mm['TEMPERATURE'].mean()
mm=mm.fillna(avgtemp)
a1=np.array(ss['TEMPERATURE'])
maxtemp=df['TEMPERATURE'].max()
mintemp=df['TEMPERATURE'].min()
days=[a1[i] for i in range(1, len(a1)) if a1[i]>avgtemp]
date=np.array(ss['DATE'])
plt.plot(date,a1,color='blue',linewidth='2',label='Temperature',marker='*',ms='10',mec='b')
plt.legend(loc='best')
print('Mean =',avgtemp)
print('Maximum =',maxtemp)
print('Minimum =',mintemp)
print('Threshold',avgtemp,'is',len(days),'DAYS')
plt.show()