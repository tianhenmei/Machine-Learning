# -*- coding: UTF-8 -*-
from decimal import Decimal
import numbers
import math

TOLERANCE = 1e-10
class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'ValueError'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'There is no unique parallel component'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'There is no unique orthogonal component'
    ONLY_ONE_DEFINED_IN_TWO_THREE_DIMS_MSG = 'The function only for two or three magnitude vector'
    def __init__(self, coordinates):
        try:
            #在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
            if not coordinates:  #判断是否为None的情况
                raise ValueError
            #tuple和list非常类似，但是tuple一旦初始化就不能修改
            self.coordinates = tuple(coordinates)  # 将列表转换为元组，用于定义元组
            self.dimension = len(coordinates)   #计算元素个数
            self.magnitude = self.getMagnitude()

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __neg__(self):
        return self * -1

    def __add__(self, v):  #加法
        try:
            if not isinstance(v, Vector) and self.dimension == v.dimension:
                raise ValueError
            return Vector([x+y for x,y in zip(self.coordinates,v.coordinates)])

        except ValueError:
            raise ValueError('The coordinates have the different dimension or the second variable is not vector')

    def __sub__(self, v):  #减法
        try:
            if not isinstance(v, Vector) and self.dimension == v.dimension:
                raise ValueError
            return Vector([x-y for x,y in zip(self.coordinates,v.coordinates)])

        except ValueError:
            raise ValueError('The coordinates have the different dimension or the second variable is not vector')

    def __mul__(self, scalar):  # 乘法
        if isinstance(scalar, numbers.Real):
            return Vector([x * scalar for x in self.coordinates])
        else:
            return NotImplemented

    def __rmul__(self, scalar):  # 右乘
        return self * scalar

    def getMagnitude(self):
        return math.sqrt(sum([x**2 for x in self.coordinates]))

    def normalized(self):
        try:
            scalar = 1 / self.magnitude
            return self * scalar
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    # def __matmul__(self, v):  # 内积@
    def dot(self, v):  # 内积@
        try:
            return sum(x*y for x,y in zip(self.coordinates,v.coordinates))
        except TypeError:
            return NotImplemented

    def getAngle(self,v):
        return math.acos(self.normalized().dot(v.normalized()))

    def getAngleDegree(self,v):
        angle = self.getAngle(v) * 180 / math.pi % 180
        if angle > 90:
            angle = 180 - angle
        if status:
            if angle == 0:
                return 'parallel'
            elif angle == 90:
                return 'orthogonal'
        return angle

    def zeroVector(self):
        return self.magnitude < TOLERANCE

    def getAngleType(self,v):
        if self.zeroVector() or v.zeroVector():
            return 'parallel and orthogonal'
        else:
            n1 = self.normalized()
            n2 = v.normalized()
            mul = n1.dot(n2)
            angle = n1.getAngle(n2)

            if angle == 0 or angle == math.pi:
                return 'parallel'
            elif abs(mul) < TOLERANCE:
                return 'orthogonal'
        return 'normal'

    def getProjection(self,v):
        try:
            u = v.normalized()
            weight = self.dot(u)
            return u * weight
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def getBasisOrthogonal(self,v):
        try:
            p = self.getProjection(v)
            return self - p
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def getCrossPruduct(self,v):
        try:
            if self.magnitude == 2:
                x1,y1,z1 = self.coordinates+(0,)
            else:
                x1,y1,z1 = self.coordinates
            if v.magnitude == 2:
                x2,y2,z2= v.coordinates+(0,)
            else:
                x2,y2,z2 = v.coordinates
            
            return Vector([
                 y1 * z2 - y2 * z1,
                -x1 * z1 - x2 * z1,
                 x1 * y2 - x2 * y1
            ])
        except ValueError as e:
            msg = str(e)
            if msg == 'too many values unpack' or msg == 'need more than 1 value unpack':
                raise Exception(self.ONLY_ONE_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e




