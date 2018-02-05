# -*- coding: UTF-8 -*-
from decimal import Decimal, getcontext
from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, dimension = None, normal_vector=None, constant_term=None):
        status = False
        if not normal_vector and not constant_term:
            raise Exception('Please make sure you have vecotr or constant')
        if not normal_vector:
            self.dimension = dimension
            all_zeros = [0] * self.dimension
            normal_vector = all_zeros
        else:
            status = True

        if not isinstance(normal_vector, Vector):
            self.normal_vector = Vector(normal_vector)
        else:
            self.normal_vector = normal_vector
            
        if status:
            self.dimension = self.normal_vector.dimension

        if not constant_term:
            constant_term = Decimal(0)
        self.constant_term = float(Decimal(constant_term))

        self.set_basepoint()

    def __getitem__(self, i):
        return self.normal_vector[i]

    def __setitem__(self, i, x):
        self.normal_vector[i] = x

    def __add__(self, v):  #加法
        nv = self.normal_vector + v.normal_vector
        nk = self.constant_term + v.constant_term
        return Plane(normal_vector = nv,constant_term = nk)

    def __mul__(self, scalar):  # 乘法
        nv = self.normal_vector * scalar
        nk = float(self.constant_term * scalar)

        return Plane(normal_vector = nv,constant_term = nk)

    def __rmul__(self, scalar):  # 右乘
        return self * scalar

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            # terms = []
            # for i in range(self.dimension): 
            #     if round(n[i], num_decimal_places) != 0:
            #         terms.append(write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1))
            #     else:
            #         terms.append('   ')
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            if terms and len(terms) > 0:
                output = ' '.join(terms)
            else:
                output = '0'

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable.coordinates):
            if not MyDecimal(item).is_near_zero():
                return k
        return -1
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)



    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n.coordinates[initial_index]
            
            if not MyDecimal(initial_coefficient).is_near_zero():
                basepoint_coords[initial_index] = float(c / initial_coefficient)
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def get_relationship(self,v):
        n = self.normal_vector
        c = v.normal_vector
        line_type = n.getAngleType(c)
        if line_type == 'parallel':
            if self.basepoint == v.basepoint:
                return 'equal'
            return 'parallel'
        else:
            return 'intersection'


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
        