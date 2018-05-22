from . import constants as const

class InfernalError(Exception):

	def __init__(self):
		pass

	def __str__(self):
		pass




class RequestError(InfernalError):
	
	def __init__(self, code):
		InfernalError.__init__(self)
		self.code = code
		self.message = const.RESPONSE_CODES[code]

	def __str__(self):
		return 'Request Error ({}): {}'.format(self.code, self.message)