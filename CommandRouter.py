class commandRouter :

	handlers = dict()

	def __init__(self) :
		pass

	def registerHandler(self, handlerName, handler) :

		self.handlers[handlerName] = handler

	def handle(self, handlerName, what) :

		if handlerName in self.handlers :
			self.handlers[handlerName].handle(what)
		else :
			raise Exception("No handler present")