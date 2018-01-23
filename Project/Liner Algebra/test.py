import vector

print('if not 0: '+str(not 0))
print('if not []: '+str(not []))
print('if not {}: '+str(not {}))
print('if not false: '+str(not False))
print('if not "": '+str(not ""))
print('if not (): '+str(not ()))
print('if not None: '+str(not None))

vector0 = vector.Vector([3.039,1.879])
vector1 = vector.Vector([0.825,2.036])

vector2 = vector.Vector([-9.88,-3.264,-8.159])
vector3 = vector.Vector([-2.155,-9.353,-9.473])

vector4 = vector.Vector([3.009,-6.172,3.692,-2.51])
vector5 = vector.Vector([6.404,-9.144,2.759,8.718])


print(vector0.getProjection(vector1))
print(vector2.getBasisOrthogonal(vector3))
print(vector4.getProjection(vector5))
print(vector4.getBasisOrthogonal(vector5))


