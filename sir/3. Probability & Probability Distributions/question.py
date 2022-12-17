#
import pandas as pd
import numpy as np
from  scipy.stats import bartlett,ttest_ind
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
cars93=pd.read_csv(r'C:\adv analytics\sir\Datasets\Cars93.csv')

#1 is prcie influnced by type 
type_ols=ols('Price ~Type',data=cars93).fit()
table=anova_lm(type_ols, typ=2)
print(table)

#plots
cts=cars93.groupby('Type')['Price'].mean()
cts1=cts.reset_index()
sns.barplot(data=cts1,y='Type',x='Price')
plt.xlabel('price')
plt.ylabel('Type')
plt.show()
#Yes is influnced by type


#2 is price influnced by AirBags
type_ols=ols('Price ~AirBags',data=cars93).fit()
table=anova_lm(type_ols, typ=2)
print(table) 
#yes price is influnced 

#3 is price influnced by Drive train 
type_ols=ols('Price ~DriveTrain',data=cars93).fit()
table=anova_lm(type_ols, typ=2)
print(table)
#yes it is influnced 

#4 are type &Airbags  realted 
ctab=pd.crosstab(cars93['Type'],cars93['AirBags'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)
#dependent 

#5 are type & Drivetrain related 
ctab=pd.crosstab(cars93['Type'],cars93['DriveTrain'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)

#6 are type & Origin realted 
ctab=pd.crosstab(cars93['Type'],cars93['Origin'])
test_statistic,p_value,df,expected_frequencies=chi2_contingency(ctab)
print(p_value)

#p value is 0.015110051037674484

#hence  value is depedent 