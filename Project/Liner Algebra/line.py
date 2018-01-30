# -*- coding: UTF-8 -*-
from decimal import Decimal
from vector import Vector

num_decimal_places = 3
class Line(object):
	NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero element found'
	def __init__(self,normal_vector = None,constant_term = None):
		self.dimension = 2
		if not normal_vector:
			all_zeros = [0] * self.dimension
			normal_vector = all_zeros
		self.normal_vector = Vector(normal_vector)
		if not constant_term:
			constant_term = Decimal('0')
		self.constant_term = float(Decimal(constant_term))

		self.set_basepoint()

	def __str__(self):
		def write_coefficient(coefficient,is_initial_term = False):
			coefficient = round(coefficient,num_decimal_places)
			if coefficient % 1 == 0:
				coefficient = int(coefficient)

			output = ''
			if coefficient < 0:
				output += '-'
			elif coefficient > 0 and not is_initial_term:
				output += '+'
			if not is_initial_term:
				output += ' '
			if abs(coefficient) != 1:
				output += '{}'.format(abs(coefficient))
			return output

		n = self.normal_vector
		try:
			initial_index = Line.first_nonzero_index(n)
			terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
			output = ' '.join(terms)
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
	def __eq__(self,v):
		n = self.normal_vector
		c = v.normal_vector
		if n.is_zero():
			if not c.is_zero():
				return False
			else:
				diff = self.constant_term - v.constant_term
				return MyDecimal(diff).is_near_zero()
		elif c.is_zero():
			return False

		if self.basepoint == v.basepoint:
			return True
		return False

	@staticmethod
	def first_nonzero_index(iterable):
		for k, item in enumerate(iterable.coordinates):
			if not MyDecimal(item).is_near_zero():
				return k
		raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

	def set_basepoint(self):
		try:
			n = self.normal_vector
			c = self.constant_term
			basepoint_coords = [0] * self.dimension

			initial_index = Line.first_nonzero_index(n)
			initial_coefficient = float(n.coordinates[initial_index])

			basepoint_coords[initial_index] = c / initial_coefficient
			self.basepoint = Vector(basepoint_coords)

		except Exception as e:
			if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
				self.basepoint = None
			else:
				raise e

	def get_relationship(self,v):
		n = self.normal_vector
		c = v.normal_vector
		line_type = n.getAngleType(c)
		if self.basepoint == v.basepoint:
			return 'equal'
		elif line_type == 'parallel':
			return 'parallel'
		else:  #intersection
			return self.get_crosspoint(v)

	def get_crosspoint(self,v):
		A,B = self.normal_vector.coordinates
		C,D = v.normal_vector.coordinates
		k1 = self.constant_term
		k2 = v.constant_term

		x_numerator = k1 * D - k2 * C
		y_numerator = A * k2 - B * k1

		d = round(A * D - B * C,num_decimal_places)
		return Vector([x_numerator / d,y_numerator / d])


class MyDecimal(Decimal):
	def is_near_zero(self, eps = 1e-10):
		return abs(self) < eps