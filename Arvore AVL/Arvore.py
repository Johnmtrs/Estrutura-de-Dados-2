#Implementação de Arvore AVL (Balanciando)
class Arvore:
	def __init__(self):
		self.raiz = None

	def inserir(self, valor):
		if self.raiz == None:
			self.raiz = No(valor)
		else:
			self.raiz.inserir(valor)

	def inOrdem(self):
		if self.raiz != None:
			return self.raiz.inOrdem()
			
	def balanceDir(self):
		return self.raiz.balanceDir()

class No:
	def __init__(self, valor):
		self.info = valor
		self.esq = None
		self.dir = None
		self.fb = 0

	#Método para calcular o fator de balanceamento de determinado No
	def findFb(self):
		fbEsq=fbDir=0
		if self.esq != None:
			fbEsq = self.esq.findAltura()
		if self.dir != None:
			fbDir = self.dir.findAltura()
		return (fbDir - fbEsq)

	#def balanceDir(self):
		#Fazer aq

	#Inserir novos Nos na arvore.
	def inserir(self, valor):
		if valor <= self.info:
			if self.esq == None:
				self.esq = No(valor)
			else:
				self.esq.inserir(valor)
		else:
			if self.dir == None:
				self.dir = No(valor)
			else:
				self.dir.inserir(valor)

	#Printa a arvore em ordem junto com algumas informações
	def inOrdem(self):
		if self.esq != None:
			self.esq.inOrdem()
		print("\nValor: {}\nFB: {}\nAltura: {}".format(self.info, self.findFb(), self.findAltura()))
		if self.dir != None:
			self.dir.inOrdem()

	#Método para encontrar altura do no
	def findAltura(self):
		hesq=hdir=0
		if self.esq != None:
			hesq = self.esq.findAltura()
		if self.dir != None:
			hdir = self.dir.findAltura()
		return 1 + max(hesq,hdir)
