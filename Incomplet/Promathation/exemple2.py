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



import string
letter = list(string.ascii_lowercase)[0:4:1]
letter.append('0')
addition_rule = {'aa':'c','ab':'a','ac':'b','a0':'a',
'ba':'b','bb':'a','bc':'c','b0':'b',
'ca':'a','cb':'b','cc':'c','c0':'c',
'0a':'a','0b':'b','0c':'c','00':'0',
}



class Group:
	def __init__(self, domain, add_rule):
		self.add_rule = add_rule
		self.domain = domain
		elements = {f'{element}' : element for element in self.domain}
		for key_, value_ in elements.items():
			self.__setattr__(key_, Element[value_])
			
		
class Element:
	def __init__(self, value):
		self.value = value
		
	def __add__(self, other):
		result = self.value + other.value 
		return result
	
addition_rule = {'aa':'c','ab':'a','ac':'b','a0':'a',
'ba':'b','bb':'a','bc':'c','b0':'b',
'ca':'a','cb':'b','cc':'c','c0':'c',
'0a':'a','0b':'b','0c':'c','00':'0',
}
domaint = ['a','b','c','0']	
groupe = Group(domain=domaint, add_rule=addition_rule)















#140721
class Element:
    def __init__(self, name, value, group):
        self.group = group
        self.value = value
        self.name = name

    def __add__(self, other):
        return self.group.__dict__[self.group.sgra[f'{(self.value + other.value)%len(self.group.__dict__["args"])}']]

    def __str__(self):
         return str(self.name)


class Set:
    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            for arg in args:
                if type(arg) == type({}):
                    # [self.__setattr__(f'{key}', value) for key, value in arg.items()]
                    [self.__setattr__(f'{key}', Element(name=key,value=value, group=self)) for key, value in arg.items()]
                ## Arg must be string
                else:
                    # self.__setattr__(f'{arg}', arg)
                    self.__setattr__(f'{arg}', Element(name=arg,value=arg, group=self))

        ## Set attributes base on their name in kwargs
        if len(kwargs) != 0: [self.__setattr__(key, value) for key, value in kwargs.items()]


class Group(Set):
    def __init__(self,*args,**kwargs):
        self.args = args[-1]
        self.sgra = {f'{value}': key for key, value in self.args.items()}
        super().__init__(self,*args,**kwargs)

    def composeTable(self):
        self.compose_table=[]
        for l1 in self.args.keys():
            self.compose_table.append([])
            for l2 in self.args.keys():
                self.compose_table[-1].append(str(self.__dict__[l1]+self.__dict__[l2]))

        return self.compose_table

class Element:
    def __init__(self, name, value, group):
        self.group = group
        self.value = value
        self.name = name

    def __add__(self, other):
        ## self.group := l'élément appartient à un groupe (self.group)

        return self.group.__dict__[self.group.sgra[f'{(self.value + other.value)%len(self.group.__dict__["args"])}']]

    def __str__(self):
         return str(self.name)


class Set:
    def __init__(self, *args, **kwargs):
        # Vérifie la présence d'argument
        if len(args) != 0:
            for arg in args:
                # Si l'argument est un dictionnaire
                if type(arg) == type({}):
                    # [self.__setattr__(f'{key}', value) for key, value in arg.items()]

                    # On crée un attribut du même nom que la valeur de la key
                    [self.__setattr__(f'{key}', Element(name=key,value=value, group=self)) for key, value in arg.items()]
                ## Arg must be string
                else:
                    # self.__setattr__(f'{arg}', arg)
                    self.__setattr__(f'{arg}', Element(name=arg,value=arg, group=self))

        ## Set attributes base on their name in kwargs
        if len(kwargs) != 0: [self.__setattr__(key, value) for key, value in kwargs.items()]


class Group(Set):
    def __init__(self,*args,**kwargs):
         # Les arguments sont associé à l'objet lui-même
        self.args = args[-1]
        self.sgra = {f'{value}': key for key, value in self.args.items()}
         # Hérite du init du parent
        super().__init__(self,*args,**kwargs)

    def composeTable(self):
        # retourne une table de composition
        self.compose_table=[]
        for l1 in self.args.keys():
            self.compose_table.append([])
            for l2 in self.args.keys():
                self.compose_table[-1].append(str(self.__dict__[l1]+self.__dict__[l2]))

        return self.compose_table









# class Obliteration(Envelope):
#     pass

valueL={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
valueU={'A': 0, 'B': -1, 'C': -2, 'D': -3, 'E': -4, 'F': -5, 'G': -6, 'H': -7, 'I': -8, 'J': -9, 'K': -10, 'L': -11, 'M': -12, 'N': -13, 'O': -14, 'P': -15, 'Q': -16, 'R': -17, 'S': -18, 'T': -19, 'U': -20, 'V': -21, 'W': -22, 'X': -23, 'Y': -24, 'Z': -25}
value={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 0, 'B': -1, 'C': -2, 'D': -3, 'E': -4, 'F': -5, 'G': -6, 'H': -7, 'I': -8, 'J': -9, 'K': -10, 'L': -11, 'M': -12, 'N': -13, 'O': -14, 'P': -15, 'Q': -16, 'R': -17, 'S': -18, 'T': -19, 'U': -20, 'V': -21, 'W': -22, 'X': -23, 'Y': -24, 'Z': -25}


groupe = Group({'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25})
print(*groupe.composeTable(),sep='\n')
	
