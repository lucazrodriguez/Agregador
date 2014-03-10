from ProjetoLabOO.Local import Local
import unittest
from should_dsl import should

class LocalSpec(unittest.TestCase):

	def setUp(self):
		self.local = Local(01,10000,"Local_1")


	def testa_Parametros_Local(self):
		self.local.idu |should| equal_to(01)
		self.local.capacidadetotal |should| equal_to(10000)
		self.local.nome |should| equal_to("Local_1")