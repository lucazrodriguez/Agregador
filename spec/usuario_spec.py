from ProjetoLabOO.Usuario import Usuario
import unittest
from should_dsl import should

class UsuarioSpec(unittest.TestCase):

	def setUp(self):
		self.usuario = Usuario(01,"123.456.789-01","email@exemplo.com","Nome_1")


	def testa_Parametros_Usuario(self):
		self.usuario.idu |should| equal_to(01)
		self.usuario.cpf |should| equal_to("123.456.789-01")
		self.usuario.email |should| equal_to("email@exemplo.com")
		self.usuario.nome |should| equal_to("Nome_1")

