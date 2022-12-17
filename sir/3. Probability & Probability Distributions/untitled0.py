import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os
os.chdir(r'C:\adv analytics\sir\Cases\Concrete Strength')
con=pd.read_csv("Concrete_Data.csv")
X=con.drop("Strength",axis=1)
y=con["Strength"]
lr=LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
#yi^
y_pred=lr.predict(X)
print(r2_score(y,y_pred))


###############################EXp_Salary####
os.chdir(r'C:\adv analytics\sir\Datasets')
exp_sals=pd.read_csv("Exp_Salaries.csv")
dum_sals=pd.get_dummies(exp_sals,drop_first=True)
X=dum_sals("Salary",axis=1)
y=dum_sals["Salary"]
lr=LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
#yi^
y_pred=lr.predict(X)
print(r2_score(y,y_pred))


os.chdir(r'C:\adv analytics\sir\Datasets')
saletopr=pd.read_csv('SalsToPredict.csv')
dum_pred=pd.get_dummies(saletopr,drop_first=True)
predtiction=lr.predict(dum_pred)

