# -*- coding: UTF-8 -*-
from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from hyperplane import Plane

getcontext().prec = 30
num_decimal_places = 3


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


    def swap_rows(self, row1, row2):
        self[row1],self[row2] = self[row2],self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        self[row] = self[row] * coefficient

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        v1 = self[row_to_add]
        v2 = self[row_to_be_added_to]

        self[row_to_be_added_to] = v1 * coefficient + v2

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def compute_triangular_form_teacher(self):
        system = deepcopy(self)
        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i][j])
                if c.is_near_zero():
                    swap_succeeded = swap_with_row_blow_nonzero_coeffient_if_able(i,j)
                    if not swap_succeeded:
                        j += 1
                        continue
                system.clear_coeffients_blow(i,j)
                j+= 1
                break
        return system

    def swap_with_row_blow_nonzero_coeffient_if_able(self,row,col):
        num_equations = len(self)
        for k in range(row+1,num_equations):
            coefficient = MyDecimal(self[k][col])
            if not coefficient.is_near_zero():
                self.swap_rows(row,k)
                return True
        return False

    def clear_coeffients_blow(self,row,col):
        num_equations = len(self)
        beta = MyDecimal(self[row][col])

        for k in range(row+1,num_equations):
            gamma = self[k][col]
            alpha = - gamma / beta
            self.add_multiple_times_row_to_row(alpha,row,k)

    def compute_triangular_form(self):
        system = deepcopy(self)
        length = len(system)

        status = 1
        while status == 1:
            first_nonzero_row = system.indices_of_first_nonzero_terms_in_each_row()
            system.sequence_swap_plane(length)
            # print 'swap',system
            t = first_nonzero_row[0]
            fstatus = False
            for i in range(1,length):
                if t >= first_nonzero_row[i] and first_nonzero_row[i] >= 0 and t >= 0:
                    fstatus = True
                    break
                else:
                    t = first_nonzero_row[i]
            if fstatus:
                system.clear_plane_coeffients(length)
                # print 'calculate',system
            else:
                status = 0
                break
        return system

    def sequence_swap_plane(self,length):
        # 将非零行向下交换
        first_nonzero_row = self.indices_of_first_nonzero_terms_in_each_row()
        for key,value in enumerate(first_nonzero_row):
            if not MyDecimal(value).is_near_zero():
                for i in range(key+1,length):
                    if value < 0 or (value > first_nonzero_row[i] and first_nonzero_row[i] >= 0 ):
                        first_nonzero_row[key],first_nonzero_row[i] = first_nonzero_row[i],first_nonzero_row[key]
                        self.swap_rows(key,i)
                        break

    def clear_plane_coeffients(self,length):
        first_nonzero_row = self.indices_of_first_nonzero_terms_in_each_row()
        # 与前几行相减
        for i in range(1,length):
            j = i - 1
            r1 = first_nonzero_row[i]
            while j >= 0 and r1 >= 0:
                r0 = first_nonzero_row[j]
                if r1 == r0 and r0 >= 0:
                    k = float(self[i][r0] / self[j][r0])
                    k = k * -1
                    self.add_multiple_times_row_to_row(k,j,i)
                    first_nonzero_row[i] = self[i].first_nonzero_index(self[i].normal_vector)
                    break
                j = j - 1

    def compute_rref(self):
        tf = self.compute_triangular_form()
        dimension = tf.dimension
        print 'triangular_form',tf
        first_nonzero_row = tf.indices_of_first_nonzero_terms_in_each_row()
        length = len(tf)
        for i in range(length):
            if(first_nonzero_row[i] >= 0):
                scalar =  float(1 / tf[i][first_nonzero_row[i]])
                tf[i] = tf[i] * scalar
        print 'coefficient 1',tf
        j = length -1
        for j in range(length - 1,-1,-1):
            if first_nonzero_row[j] == -1:  # 0 = 0  ||  0 = k
                continue
            else:
                for k in range(j+1,dimension):
                    if k < length:
                        coefficient = tf[j][first_nonzero_row[k]] * -1 #tf[j][k] * -1
                        tf.add_multiple_times_row_to_row(coefficient,k,j)
        return tf

    def get_solution(self):
        ti = self.compute_rref()
        print 'opposite angle',ti
        length = len(ti)
        useful = length
        status = ''
        first_nonzero_row = ti.indices_of_first_nonzero_terms_in_each_row()
        for i in first_nonzero_row:
            if i == -1:
                useful -= 1
                if MyDecimal(ti[i].constant_term).is_near_zero():
                    status = 'SOLUTIONS_INFINITE'
                else:
                    status = 'SOLUTIONS_NONE'
                    break

        if status == 'SOLUTIONS_NONE':  # 无解
            return status
        elif status == 'SOLUTIONS_INFINITE' or useful < ti.dimension:  # 无穷解
            return ti.get_infinite_solution(useful)
        else:  # 唯一解
            return ti

    def get_infinite_solution(self,useful):
        first_nonzero_row = self.indices_of_first_nonzero_terms_in_each_row()
        length = len(self)
        dimension = self.dimension
        arr = []
        temp_arr = []
        ret = ''
        varibles = 0

        for i in range(0,useful):
            constant_term = round(self[i].constant_term, num_decimal_places)
            is_initial_term = True
            temp = []
            for j in range(first_nonzero_row[i]+1,dimension):
                temp.append(self[i][j] * -1)

            if first_nonzero_row[i] > i:
                for ii in range(i,first_nonzero_row[i]):
                    temp_arr.append('Equation {}: x_{} = t{}'.format(ii+1,ii+1,varibles))
                    varibles += 1
            if abs(constant_term) > 0:
                temp_arr.append('Equation {}: x_{} = {} '.format(first_nonzero_row[i]+1,first_nonzero_row[i]+1,constant_term))
                is_initial_term = False
            else:
                temp_arr.append('Equation {}: x_{} = '.format(first_nonzero_row[i]+1,first_nonzero_row[i]+1))
                is_initial_term = True
            invalid = 0
            for p,q in enumerate(temp):
                q = round(q, num_decimal_places)
                if q % 1 == 0:
                    q = int(q)
                if q != 0:
                    if q < 0:
                        temp_arr[first_nonzero_row[i]] += '-'
                    elif q >= 0 and not is_initial_term:
                        temp_arr[first_nonzero_row[i]] += '+'

                    if not is_initial_term:
                        temp_arr[first_nonzero_row[i]] += ' '

                    if abs(q) != 1:
                        temp_arr[first_nonzero_row[i]] += '{}t{}'.format(abs(q),varibles + p - invalid)
                    else:
                        temp_arr[first_nonzero_row[i]] += 't{}'.format(varibles + p - invalid)
                else:
                    invalid += 1
        for i in range(useful+varibles,dimension):
            temp_arr.append('Equation {}: x_{} = t{}'.format(i+1,i+1,varibles))
            varibles += 1
        ret += '\n'.join(temp_arr)
        return ret

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps



