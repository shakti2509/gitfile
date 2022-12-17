#anova 
import pandas as pd
import numpy as np
from  scipy.stats import bartlett,ttest_ind
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns
##########Yield#############
agr=pd.read_csv(r"C:\adv analytics\Datasets\Yield.csv")
agr_ols=ols("Yield ~ Treatments",data=agr).fit()
table=anova_lm(agr_ols,typ=2)
print(table)
###############Post Hoc Tukey HSD###############
compare=pairwise_tukeyhsd(agr['Yield'], agr['Treatments'],alpha=0.05)
dd=pd.DataFrame(compare._results_table.data)
dd
agr.groupby('Treatments')['Yield'].mean()

#Plantgrowth
pg=pd.read_csv(r'C:\adv analytics\Datasets\PlantGrowth.csv')
pg_ols=ols('weight~group',data=pg).fit()
table=anova_lm(pg_ols,typ=2)
print(table)

#HSD###########
compare=pairwise_tukeyhsd(pg['weight'], pg['group'],alpha=0.05)
dd=pd.DataFrame(compare._results_table.data)
dd
pg.groupby('group')['weight'].mean()
####################
train=pd.read_csv(r'C:\adv analytics\sir\Cases\Big Mart Sales\train_v9rqX0R.csv')
train['Item_Type'].unique()
len(train['Item_Type'].unique())
type_ols=ols('Item_Outlet_Sales ~Item_Type',data=train).fit()
table=anova_lm(type_ols, typ=2)
print(table)
############graph
cts=train.groupby('Item_Type')['Item_Outlet_Sales'].mean()
cts1=cts.reset_index()
sns.barplot(data=cts1,y='Item_Type',x='Item_Outlet_Sales')
plt.xlabel('mean item size')
plt.ylabel('item type')
plt.show()

#############for outlet_type
train['Outlet_Type'].unique()

###anova 
type_ols=ols('Item_Outlet_Sales ~Outlet_Type',data=train).fit()
table=anova_lm(type_ols, typ=2)
print(table)
#graph
cts=train.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()
cts1=cts.reset_index()
sns.barplot(data=cts1,y='Outlet_Type',x='Item_Outlet_Sales')
plt.xlabel('mean item size')
plt.ylabel('Outlet_Type')
plt.show()
####fat_content 

train['Item_Fat_Content'].unique()
##Anova
type_ols=ols('Item_Outlet_Sales ~Item_Fat_Content',data=train).fit()
table=anova_lm(type_ols, typ=2)
print(table)

#replace 
train['Item_Fat_Content'].replace('low fat','Low Fat',inplace=True)
train['Item_Fat_Content'].replace('LF','Low Fat',inplace=True)
train['Item_Fat_Content'].replace('reg','Regular',inplace=True)
#graph
cts=train.groupby('Item_Fat_Content')['Item_Outlet_Sales'].mean()
cts1=cts.reset_index()
sns.barplot(data=cts1,y='Item_Fat_Content',x='Item_Outlet_Sales')
plt.xlabel('mean item size')
plt.ylabel('Item_Fat_Content')
plt.show()

