import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os
os.chdir(r"C:\adv analytics\Datasets")
pizza=pd.read_csv("pizza.csv")
lr=LinearRegression()
X=pizza[['Promote']]
y=pizza['Sales']

lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)


#yi^(Y-capp)
y_pred=lr.predict(X)
print(r2_score(y,y_pred))
#numerator=np.sum((y-y_pred)**2)
#denomenator=np.sum((y-y.mean())**2)
#1-(numerator/denomenator)
#####################insurance
insure=pd.read_csv("Insure_auto.csv")
X=insure[['Home']]
y=insure['Operating_Cost']
lr.fit(X,y)
y_pred=lr.predict(X)
print(r2_score(y,y_pred))




X=insure[['Automobile']]
y=insure['Operating_Cost']
lr.fit(X,y)
y_pred=lr.predict(X)
print(r2_score(y,y_pred))



X=insure[['Home','Automobile']]
y=insure['Operating_Cost']
lr.fit(X,y)
y_pred=lr.predict(X)
print(r2_score(y,y_pred))

#more will be r2(rsquare) more leser error more prefection


################Boston
boston=pd.read_csv("Boston.csv")
#######bu iloc function 
X=boston.iloc[:,:-1]
#or
X=boston.drop('medv',axis=1)
y=boston['medv']
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
y_pred=lr.predict(X)
print(r2_score(y,y_pred))












