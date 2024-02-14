from google.colab import drive
drive.mount('/content/drvie')

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,87,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.plot(runs,w,color='green')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#generate array of 200 values betweeen -pi &pi
tigar=np.linspace(-2*np.pi,2*np.pi,100)
print(tigar)
plt.scatter(tigar,np.sin(tigar),color='blue')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
#creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
#plotting
plt.subplot(2,1,1)
plt.plot(overs,runs_i,color="blue",label="India")
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.plot(overs_a,runs_a,color="red",label = "Aus")
plt.legend(loc='best')

import numpy as np
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='lavender',linewidth='3',label='CompanyA',marker='*',ms='20',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='blue',linestyle='dotted',label='CompanyB',marker='*')

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
color=["blue","hotpink","blue","hotpink"]
explo=[0,0.2,0,0]
plt.pie(a,labels=labe,textprops={'fontsize':18},colors=color,explode=explo,startangle=180)
plt.show()

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