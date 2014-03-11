from ProjetoLabOO.Evento import Evento
from ProjetoLabOO.Local import Local
import unittest
from should_dsl import should

class EventoSpec(unittest.TestCase):

	def setUp(self):
		self.evento = Evento(01,"certificacao", "01/01/0001", 10, "empresas", "finalidade", "nome","palestrante","tipo")
		self.local = Local(01,10000,"Local_1")

	def testa_Parametros_Evento(self):
		self.evento.idu |should| equal_to(01)
		self.evento.certificacao |should| equal_to("certificacao")
		self.evento.data |should| equal_to("01/01/0001")
		self.evento.dias |should| equal_to(10)
		self.evento.empresas |should| equal_to("empresas")
		self.evento.finalidade |should| equal_to("finalidade")
		self.evento.nome |should| equal_to("nome")
		self.evento.palestrante |should| equal_to("palestrante")
		self.evento.tipo |should| equal_to("tipo")

	def testa_inserir_local(self):
		self.evento.inserirLocal(self.local)
		self.evento.local |should| equal_to(self.local)



