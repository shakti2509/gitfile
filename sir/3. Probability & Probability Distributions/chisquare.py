#chi Square
import pandas as pd 
import numpy as np 
from scipy.stats import chi2_contingency

housing =pd.read_csv('Housing.csv')
ctab=pd.crosstab(housing['prefarea'],housing['gashw'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)

# for train_v9rqX0R.csv
#for item fat contect  and item type  
train =pd.read_csv(r'C:\adv analytics\sir\Cases\Big Mart Sales\train_v9rqX0R.csv')
ctab=pd.crosstab(train['Item_Fat_Content'],train['Item_Type'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)
#dependetnt


#for outlet  type  to item type 
ctab=pd.crosstab(train['Outlet_Type'],train['Item_Type'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)
#indipentent 


#for outlet location  related to item type 

ctab=pd.crosstab(train['Outlet_Location_Type'],train['Item_Type'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)
#indipedent 




