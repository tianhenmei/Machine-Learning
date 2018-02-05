# -*- coding: UTF-8 -*-
from hyperplane import Plane
from vector import Vector
from decimal import Decimal
from linesys import LinearSystem
from copy import deepcopy

print('if not 0: '+str(not 0))
print('if not []: '+str(not []))
print('if not {}: '+str(not {}))
print('if not false: '+str(not False))
print('if not "": '+str(not ""))
print('if not (): '+str(not ()))
print('if not None: '+str(not None))


p0 = Plane(normal_vector=[0.786,0.786,0.588], constant_term=-0.714)
p1 = Plane(normal_vector=[-0.138,-0.138,0.244], constant_term=0.319)

p2 = Plane(normal_vector=[8.631,5.112,-1.816,2.113,2.567], constant_term=-5.113)
p3 = Plane(normal_vector=[4.315,11.132,-5.27,0.445,-0.192], constant_term=-6.775)
p4 = Plane(normal_vector=[-2.158,3.01,-1.727,9.001,0.224],constant_term=-0.831)

p5 = Plane(normal_vector=[0.935,1.76,-9.365,1.225],constant_term=-9.955)
p6 = Plane(normal_vector=[0.187,0.552,-1.073,0.778],constant_term=-1.991)
p7 = Plane(normal_vector=[0.373,0.704,-3.746,0.998],constant_term=-3.982)
p8 = Plane(normal_vector=[-0.561,-0.056,5.619,0.233],constant_term=5.973)
p9 = Plane(normal_vector=[-0.561,-0.2,5.619,0.233],constant_term=5.973)

print 's1 **********************************************'
s1 = LinearSystem([p0,p1])
t1 = s1.get_solution()
print 'solution\n',t1

print 's2 **********************************************'
s2 = LinearSystem([p2,p3,p4])
t2 = s2.get_solution()
print 'solution\n',t2

print 's3 **********************************************'
s3 = LinearSystem([p5,p6,p7,p8,p9])
t3 = s3.get_solution()
print 'solution\n',t3




