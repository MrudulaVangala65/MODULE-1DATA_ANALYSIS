

import seaborn as sns
import matplotlib.pyplo as plt
tips=sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tips", data=tips)
plt.title("Scatter Plot of Total Bill va.Tip")
plt.xlabel("Total_Bill($)")
plt.ylabel("tips($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
tips=sns.load_dataset("flights")
print(tips.head())

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
tips=sns.load_dataset("flights")

#Ceate a scatter plot
sns.scatterplot(x="month",y="passengers",data=tips)
plt.title("scatter plot of total passengers vs. flights")
plt.xlabel("month ()")
plt.ylabel("passengers ()")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
tips=sns.load_dataset("flights")

#Ceate a scatter plot
sns.violinplot(x="month",y="passengers",data=tips)
plt.title("scatter plot of total passengers vs. flights")
plt.xlabel("month ()")
plt.ylabel("passengers ()")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
var1=sns.load_dataset("tips")
#compute correlation matrix
correlation_matrix=var1.corr()
#create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of tips dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
var1=sns.load_dataset("iris")
#compute correlation matrix
correlation_matrix=var1.corr()
#create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
var1=sns.load_dataset("planets")
#compute correlation matrix
correlation_matrix=var1.corr()
#create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of planets dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
#Load example dataset
var1=sns.load_dataset("attention")
#compute correlation matrix
correlation_matrix=var1.corr()
#create a heatmap of the correlation matrix
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of attention dataset")
plt.show()

