
class Evento:
	def __init__(self, idu, certificacao, data, dias, empresas, finalidade, nome, palestrante, tipo):
		self.idu = idu
		self.certificacao = certificacao
		self.data = data
		self.dias = dias
		self.empresas = empresas
		self.finalidade = finalidade
		self.nome = nome
		self.palestrante = palestrante
		self.tipo = tipo

	def inserirLocal(self,local):
		#if local isinstance (local, Local):
		self.local = local