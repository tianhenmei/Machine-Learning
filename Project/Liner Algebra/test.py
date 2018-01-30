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

plane0 = plane.Plane([-0.412,3.806,0.728],-3.46)
plane1 = plane.Plane([1.03,-9.515,-1.82],8.65)

plane2 = plane.Plane([2.611,5.528,0.283],4.6)
plane3 = plane.Plane([7.715,8.306,5.342],3.76)

plane4 = plane.Plane([-7.926,8.625,-7.217],-7.952)
plane5 = plane.Plane([-2.642,2.875,-2.404],2.443)

# print(v0.getAngleType(v1))
print(plane0.get_relationship(plane1))
print(plane2.get_relationship(plane3))
print(plane4.get_relationship(plane5))
