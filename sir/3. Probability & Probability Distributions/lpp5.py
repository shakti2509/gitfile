import pulp as p
#ploblem 
#Minimize
Lp_prob=p.LpProblem('problem1',p.LpMinimize)
x1=p.LpVariable("x1",lowBound=0)
x2=p.LpVariable("x2",lowBound=0)

#decion variable 
Lp_prob+=.3*x1+.9*x2

Lp_prob+=.09*x1+.6*x2>=240
Lp_prob+=.02*x1+.06*x2<=40
Lp_prob+=1*x1+1*x2>=800


print(Lp_prob)

#solving  the LPP

status =Lp_prob.solve()
print(p.LpStatus[status])


#solution
print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))

