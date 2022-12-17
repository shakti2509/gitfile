import pulp as p
#ploblem 
#maximize
Lp_prob=p.LpProblem('problem',p.LpMaximize)
x1=p.LpVariable("x1",lowBound=0)
x2=p.LpVariable("x2",lowBound=0)

#decion variable 
Lp_prob+=40*x1+100*x2

Lp_prob+=12*x1+6*x2<=3000
Lp_prob+=4*x1+10*x2<=2000
Lp_prob+=2*x1+3*x2<=900

print(Lp_prob)

#solving  the LPP

status =Lp_prob.solve()
print(p.LpStatus[status])


#solution
print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("objective=",p.value(Lp_prob.objective))