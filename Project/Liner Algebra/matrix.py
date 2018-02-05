# -*- coding: UTF-8 -*-
import numbers
import math
from decimal import Decimal, getcontext
from copy import deepcopy
from vector import Vector
# import numpy as np

class Matrix(object):
	def __init__(self,matrix = None):
		if not matrix and len(matrix) == 0:
			raise Exception("Matrix cannot be empty")

		for i in matrix:
			if not isinstance(i,list):
				raise Exception("Matrix show be two-dimensional array")
				return 
		# self.matrix = np.array(matrix)
		self.matrix = matrix
		self.row = len(matrix)
		self.col = len(matrix[0])

	def __str__(self):
		temp = []
		for i in self.matrix:
			arr = ['{}'.format(j) for j in i]
			temp.append(' '.join(arr))
		return 'Matrix: \n'+'\n'.join(temp)

	def __getitem__(self, i):
		return self.matrix[i]

	def __setitem__(self, i, x):
		try:
			assert len(x) == self.col
			self.matrix[i] = x

		except AssertionError:
			raise Exception("They have different length")

	def __mul__(self, v):  # 乘法
		if isinstance(v, numbers.Real):
			temp = []
			for x in self.matrix:
				temp.append([float(y * v) for y in x])
			return Matrix(temp)
		elif isinstance(v, Matrix):
			if not self.col == v.row:
				raise Exception("The first matrix col has to equal with the second one row")
			group = []
			v_transpose = v.transpose()
			for i in self.matrix:
				group.append([self.dot(i,j) for j in v_transpose.matrix])
			return Matrix(group)
        	# for i in self.matrix:
        	# 	group.append([Vector(i).dot(Vector(v.matrix[:,j])) for j in range(v.col)])
		else:
 			return NotImplemented

 	def __add__(self,v): # 加法
 		if not isinstance(v,Matrix):
 			raise Exception("Matrix can't add with other type of data")
 		if not self.row == v.row and self.col == v.col:
 			raise Exception("The two Matrix can be added if they have the same row and col")
 		temp = []
 		for m0,m1 in zip(self.matrix,v.matrix):
 			temp.append([i+j for i,j in zip(m0,m1)])
 		return Matrix(temp)

 	def dot(self,i,j):
		sum = 0
		for x,y in zip(i,j):
			sum += x * y
		return sum

 	def transpose(self): #转置
 		matrix_transpose = []
 		for i in range(self.col):
 			matrix_transpose.append([])
	 		for j in range(self.row):
	 			matrix_transpose[i].append(self[j][i])
	 	return Matrix(matrix_transpose)

	def inverse(self): # 逆
		if not self.row == self.col:
			raise Exception("This matrix doesn't have inverse matrix, because the row and the col is not equal")

		det = self.getDet()
		adjoint = self.getAdjoint()
		return adjoint * (1 / det)

	def getDet(self): # 获取行列式的值
		if not self.row == self.col:
			raise Exception("This matrix doesn't have inverse matrix, because the row and the col is not equal")

		triangular_matrix = self.compute_triangular_form()
		multiply = 1
		for k,v in enumerate(triangular_matrix):
			multiply *= v[k]
		return multiply

	def getAdjoint(self):
		system = deepcopy(self)
		adjoint = []
		for i,item in enumerate(system):
			adjoint.append([])
			for j,one in enumerate(item):
				temp = []
				index = 0
				for p,v1 in enumerate(system):
					if not p == i:
						temp.append([])
						for q,o1 in enumerate(v1):
							if not q == j:
								temp[index].append(o1)
						index += 1

				adjoint[i].append(Matrix(temp).getDet() * math.pow( -1, i+j ))

		return Matrix(adjoint).transpose()





	# 获取上三角函数
	# 获取上三角函数
	# 获取上三角函数
	def swap_rows(self, row1, row2):
		self[row1],self[row2] = self[row2],self[row1]

	def multiply_coefficient_and_row(self, coefficient, row):
		self[row] = [i * coefficient for i in self[row]]

	def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
		v1 = self[row_to_add]
		v2 = self[row_to_be_added_to]

		self[row_to_be_added_to] = [i*coefficient+j for i,j in zip(v1,v2)]

	def indices_of_first_nonzero_terms_in_each_row(self):
		row = self.row
		indices = [-1] * row
		for k,value in enumerate(self.matrix):
			indices[k] = self.first_nonzero_index(value)

		return indices

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
					first_nonzero_row[i] = self.first_nonzero_index(self[i])
					break
				j = j - 1

	def compute_triangular_form(self):
		system = deepcopy(self)
		length = system.row

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


	@staticmethod
	def first_nonzero_index(iterable):
		for k, item in enumerate(iterable):
			if not MyDecimal(item).is_near_zero():
				return k
		return -1
		raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)



class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps




