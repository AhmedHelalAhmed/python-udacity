p =[1,2]
q = [3,4]
p.append(q)
q[1]=100
#the thrird element in p just reference to the q list
print p
print len(p)