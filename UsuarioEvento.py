from ProjetoLabOO.Usuario import Usuario
from ProjetoLabOO.Evento import Evento

class UsuarioEvento:
	def __init__(self, idu, data, hora, pessoasconfirmadas):
		self.idu = idu
		self.data = data
		self.hora = hora
		self.pessoasconfirmadas = pessoasconfirmadas


	def inserirEvento(self, evento):
		if isinstance(evento, Evento):
			self.evento = evento

	def inserirUsuario(self,usuario):
		if isinstance(usuario, Usuario):
			self.usuario = usuario