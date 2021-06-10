import string
letter = list(string.ascii_lowercase)[0:4:1]
letter.append('0')

addition_rule = {'aa':'c','ab':'a','ac':'b','a0':'a',
'ba':'b','bb':'a','bc':'c','b0':'b',
'ca':'a','cb':'b','cc':'c','c0':'c',
'0a':'a','0b':'b','0c':'c','00':'0',
}

regle['key'] ---> valeur
class Groupe:

	def __init__(self,value, addition_rule):
		self.addition = addition_rule
		self.value = value
		
	def __add__(self, other):
		return addition_rule[self.value + other.value]
		
	def __radd__(self, other):
		return addition_rule[self.value + other.value]
		
	#def __radd__(self, other):
	#	return other + self.value

a = Groupe('a',rule)
b = Groupe('b',rule)

'a'+'b'!=
a+b =		
groupe = {f'{element}': Groupe(element,addition_rule) for element in letter}


print(groupe['a']+groupe['b'])
print(groupe['b']+groupe['a'])


import string
letter = list(string.ascii_lowercase)[0:4:1]
letter.append('0')
addition_rule = {'aa':'c','ab':'a','ac':'b','a0':'a',
'ba':'b','bb':'a','bc':'c','b0':'b',
'ca':'a','cb':'b','cc':'c','c0':'c',
'0a':'a','0b':'b','0c':'c','00':'0',
}
class Group:
	def __init__(self, elements, rules):
		self.elements = elements
		self.rules = rules
		
		for element in elements:
			self.element = element

groupe = Group(letter,addition_rule)
a = groupe.elements[0]





import string
letter = list(string.ascii_lowercase)[0:4:1]
letter.append('0')
addition_rule = {'aa':'c','ab':'a','ac':'b','a0':'a',
'ba':'b','bb':'a','bc':'c','b0':'b',
'ca':'a','cb':'b','cc':'c','c0':'c',
'0a':'a','0b':'b','0c':'c','00':'0',
}

class Element(Group):
	def __init__(self, value, addition_dict=None, domain=None):
		super().__init__(addition_dict, domain)
		self.value = value
		
	def __add__(self, other):
		value = addition_dict[self.value + other.value]
		print(value)
		return Element(value, addition_dict=self.addition_dict, domain=self.domain)
		
class Group:
	def __init__(self, addition_dict=None, domain=None):
		self.addition_dict = addition_dict
		self.domain = domain
		self.element = []
		self.cardinality = len(domain)
		for i in range(self.cardinality):
			self.element[i] = Element(domain[i])
					
groupe = Group(addition_rule, letter)
	
	
	
