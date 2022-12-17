import pandas as pd 
import numpy as np
import os 
import seaborn as sns 
import matplotlib.pyplot as plt

os.chdir(r"C:\adv analytics\Datasets")

a=np.array([2,5,6,7,10])
b=np.array([30,24,20,17,7])
ab=np.stack([a,b],axis=1)
#variance covariance matrix
np.cov(a,b)


pizza=pd.read_csv("pizza.csv")

pizza['Promote'].cov(pizza['Sales'])

#variance covariance matrix
np.cov(pizza['Promote'],pizza['Sales'])

pizza.cov()

#corelation 
pizza['Promote'].corr(pizza['Sales'])

#with same corealtion 
pizza['Promote'].corr(pizza['Promote'])
pizza['Sales'].corr(pizza['Sales'])

#corelation matrix
pizza.corr()
np.corrcoef(pizza['Promote'],(pizza['Sales']))

#scater plot
sns.scatterplot(data=pizza,x="Promote",y="Sales")
plt.show()

###############insurance ##########
insure=pd.read_csv("Insure_auto.csv")
insure.corr()

sns.heatmap(insure.corr(),xticklabels=insure.corr().columns,yticklabels=insure.corr().columns,
            annot=True)
plt.show()



sns.pairplot(insure,diag_kind='kde')
plt.show()



sns.pairplot(insure)
plt.show()

###############################iris############
iris=pd.read_csv("iris.csv")
sns.heatmap(iris.corr(),xticklabels=iris.corr().columns,yticklabels=iris.corr().columns,
            annot=True)
plt.show()


###########Boston
boston=pd.read_csv("Boston.csv")
sns.heatmap(boston.corr(),xticklabels=boston.corr().columns,yticklabels=boston.corr().columns,
            annot=True)
plt.show()
#############         
