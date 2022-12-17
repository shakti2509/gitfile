import pandas as pd
import numpy as np 
import os 
from  scipy.stats import bartlett,ttest_ind
os.chdir(r'C:\adv analytics\sir\Datasets')
puromycin=pd.read_csv('Puromycin.csv')
treated=puromycin[puromycin['state']=='treated']
untreated=puromycin[puromycin['state']=='untreated']
bartlett(treated['rate'],untreated['rate'])
ttest_ind(treated['rate'],untreated['rate'],equal_var=True)
###########################Soporific 
soporific=pd.read_csv('Soporific.csv')
bartlett(soporific['Drug A'],soporific['Drug B'])
ttest_ind(soporific['Drug A'],soporific['Drug B'],equal_var=True)
#######################Housing
housing=pd.read_csv('Housing.csv')
prefer=housing[housing['prefarea']=='no']
unprefer=housing[housing['prefarea']=='yes']
bartlett(prefer['price'],unprefer['price'])
###BartlettResult(statistic=5.077175886434614, pvalue=0.0242428265503372)
ttest_ind(prefer['price'],unprefer['price'],equal_var=False)
###Ttest_indResult(statistic=-7.478383024308103, pvalue=2.821321106669613e-12)
#airco
housing=pd.read_csv('Housing.csv')
h1=housing[housing['airco']=='no']
h2=housing[housing['airco']=='yes']
bartlett(h1['price'],h2['price'])
ttest_ind(h1['price'],h2['price'],equal_var=False)
ttest_ind(h1['price'],h2['price'],alternative='greater',equal_var=False)
###Cars93---------------
cars93=pd.read_csv('Cars93.csv')
c1=cars93[cars93['Origin']=='non-USA']
c2=cars93[cars93['Origin']=='USA']
bartlett(c1['Price'],c2['Price'])
#BartlettResult(statistic=6.0382009476180585, pvalue=0.01399954338801128)
ttest_ind(c1['Price'],c2['Price'],equal_var=False)
#Ttest_indResult(statistic=0.9544860372166483, pvalue=0.3427990389908705)
ttest_ind(c1['Price'],c2['Price'],alternative='greater',equal_var=False)
#Ttest_indResult(statistic=0.9544860372166483, pvalue=0.17139951949543525)
# for man.trans avilable
no=cars93[cars93['Man.trans.avail']=='No']
yes=cars93[cars93['Man.trans.avail']=='Yes']
bartlett(no['Price'],yes['Price'])
#BartlettResult(statistic=2.689431652761735, pvalue=0.1010158392492928)
ttest_ind(no['Price'],yes['Price'],equal_var=True)
#Ttest_indResult(statistic=3.2952476009261162, pvalue=0.0014025458777908683)
ttest_ind(no['Price'],yes['Price'],alternative='greater',equal_var=True)
# Ttest_indResult(statistic=3.2952476009261162, pvalue=0.0007012729388954341)

##########hosing
g1=housing[housing['gashw']=='no']
g2=housing[housing['gashw']=='yes']
bartlett(g1['price'],g2['price'])

