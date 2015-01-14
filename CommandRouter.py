class commandRouter :

	handlers = dict()

	def __init__(self) :
		pass

	def registerHandler(self, handlerName, handler) :

		self.handlers[handlerName] = handler

	def handle(self, handlerName, what) :

		self.handlers[handlerName].handle(what)