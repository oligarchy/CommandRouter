class commandRouter :

	handlers = dict()

	def __init__(self) :
		pass

	def registerHandler(self, handlerName, handler) :

		self.handlers[handlerName] = handler

	
	def build_log(self, handlerName , msg):
		
		#log file to keep track for failed request for later analysis
		f = open("log_handled.txt","a") #opens file with name of "log_handled.txt"
		#f.write(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
		#f.write(time.time())
		f.write(handlerName)
		f.write("\n")
		f.write(msg)
		f.write("\n\n\n")

	def handle(self, handlerName, what, multiple_instances = "FALSE", prepare_log = "FALSE") :

		# multiple handle instances can be associated to same handlerName they should be processed seperately
		# giving priority to each instance
		# each instance holds different memory space
		# however multiple instace occurance of handles will be treated as one by default

		if(multiple_instances == "TRUE"):
			
			if handlerName in self.handlers:

				i = 0
			
				for handlerName in self.handlers :
					self.handlers[handlerName].handle(what)
					#uncomment/comment line below to hide/show instance memory address if multiple
					print(self.handlers[handlerName])
					i = i+1
					if(i > 1):
						print "More than 1 Instances Were Found To Be Associated"
			else :
				print "No handler present"
				if(prepare_log == "TRUE"):
					self.build_log(handlerName,"No handler present")
				
		else:
			if handlerName in self.handlers :
				self.handlers[handlerName].handle(what)
			else:
				print "No handler present"
				if(prepare_log == "TRUE"): 
                                        self.build_log(handlerName,"No handler present")

			
