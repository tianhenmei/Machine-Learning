# -*- coding: UTF-8 -*-
import plane
import vector
from decimal import Decimal

print('if not 0: '+str(not 0))
print('if not []: '+str(not []))
print('if not {}: '+str(not {}))
print('if not false: '+str(not False))
print('if not "": '+str(not ""))
print('if not (): '+str(not ()))
print('if not None: '+str(not None))

plane0 = plane.Plane([1,-2,1],-1)
plane1 = plane.Plane([1,0,-2],2)
plane2 = plane.Plane([-1,4,-4],0)

plane3 = plane.Plane([0,1,-1],2)
plane4 = plane.Plane([1,-1,1],2)
plane5 = plane.Plane([3,-4,1],1)

plane6 = plane.Plane([1,2,1],-1)
plane7 = plane.Plane([3,6,2],1)
plane8 = plane.Plane([-1,-2,-1],1)


