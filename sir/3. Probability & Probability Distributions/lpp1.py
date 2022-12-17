import pulp as p
#ploblem 
#maximize
Lp_prob=p.LpProblem('problem',p.LpMaximize)
x1=p.LpVariable("x1",lowBound=0)
x2=p.LpVariable("x2",lowBound=0)

#decion variable 
Lp_prob+=5*x1+7*x2

Lp_prob+=1*x1+0*x2<=6
Lp_prob+=2*x1+3*x2<=19
Lp_prob+=1*x1+1*x2<=8

print(Lp_prob)

#solving  the LPP

status =Lp_prob.solve()
print(p.LpStatus[status])


#solution
print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))

