class Parent():
	CONSTANTSTATUS = 'Hello choulaogong'
	def __init__(self,last_name,eye_color):
		print('Parent Constructor Called')
		self.last_name = last_name
		self.eye_color = eye_color
	def showInfo(self):
		print('Last name: '+ self.last_name)
		print('Eye color: '+ self.eye_color)


class Child(Parent):
	def __init__(self,last_name,eye_color,number_of_toys):
		print('Child Constructor Called')
		Parent.__init__(self,last_name,eye_color)
		self.number_of_toys = number_of_toys
	def showInfo(self):
		print('Last name: '+ self.last_name)
		print('Eye color: '+ self.eye_color)
		print('Number of toys: '+ str(self.number_of_toys))

lili = Child('Li','red',11)
lili.showInfo()