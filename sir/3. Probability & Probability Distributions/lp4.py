import pulp as p
#ploblem 
#Minimize
Lp_prob=p.LpProblem('problem1',p.LpMinimize)
x1=p.LpVariable("x1",lowBound=0)
x2=p.LpVariable("x2",lowBound=0)

#decion variable 
Lp_prob+=700*x1+550*x2

Lp_prob+=3000*x1+1000*x2>=24000
Lp_prob+=1000*x1+1000*x2>=16000
Lp_prob+=2000*x1+6000*x2>=48000


print(Lp_prob)

#solving  the LPP

status =Lp_prob.solve()
print(p.LpStatus[status])


#solution
print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))

