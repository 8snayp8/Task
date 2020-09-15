#3
import random 
class Cat:
	def __init__(self, count,CatBoy = 0,CatGirl = 0): 
		while CatBoy + CatGirl < count:
			CatBoy = random.randint(0,count)
			CatGirl = random.randint(0,count - CatBoy)
		self._count = count
		self._boy = CatBoy
		self._girl = CatGirl

	def __display_info(self):
		print(self.__str__())

	def __str__(self):
		return "Общее кол-во котят: {} \n Мальчиков: {} \n Девочек: {}".format(self._count, self._boy, self._girl) 

cat = Cat(90)  
print(cat)