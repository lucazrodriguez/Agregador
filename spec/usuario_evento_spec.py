from ProjetoLabOO.UsuarioEvento import UsuarioEvento
from ProjetoLabOO.Usuario import Usuario
from ProjetoLabOO.Evento import Evento

import unittest
from should_dsl import should

class UsuarioEventoSpec(unittest.TestCase):

	def setUp(self):
		self.usuarioEvento = UsuarioEvento(01, "01/01/0001", "01:01", 10000)
		self.usuario = Usuario(01,"123.456.789-01","email@exemplo.com","Nome_1")
		self.evento = Evento(01,"certificacao", "01/01/0001", 10, "empresas", "finalidade", "nome","palestrante","tipo")


	def testa_Parametros_UsuarioEvento(self):
		self.usuarioEvento.idu |should| equal_to(01)
		self.usuarioEvento.data |should| equal_to("01/01/0001")
		self.usuarioEvento.hora |should| equal_to("01:01")
		self.usuarioEvento.pessoasconfirmadas |should| equal_to(10000)

	def testa_inserir_Evento(self):
		self.usuarioEvento.inserirEvento(self.evento)
		self.usuarioEvento.evento |should| equal_to(self.evento)

	def testa_inserir_Usuario(self):
		self.usuarioEvento.inserirUsuario(self.usuario)
		self.usuarioEvento.usuario |should| equal_to(self.usuario)
