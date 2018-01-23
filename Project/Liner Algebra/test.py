import vector

print('if not 0: '+str(not 0))
print('if not []: '+str(not []))
print('if not {}: '+str(not {}))
print('if not false: '+str(not False))
print('if not "": '+str(not ""))
print('if not (): '+str(not ()))
print('if not None: '+str(not None))

vector0 = vector.Vector([-7.579,-7.88])
vector1 = vector.Vector([22.737,23.64])

vector2 = vector.Vector([-2.029,9.97,4.172])
vector3 = vector.Vector([-9.231,-6.639,-7.245])

vector4 = vector.Vector([-2.328,-7.284,-1.214])
vector5 = vector.Vector([-1.821,1.072,-2.94])

vector6 = vector.Vector([2.118,4.827])
vector7 = vector.Vector([0,0])

print(vector0.getAngleType(vector1))
print(vector2.getAngleType(vector3))
print(vector4.getAngleType(vector5))
print(vector6.getAngleType(vector7))


