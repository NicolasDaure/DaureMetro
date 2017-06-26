globCount = 0

class Test:

	def __init__(self, idTest):
		if idTest != None:
			self.idTest = idTest
		# global globCount
		# globCount += 1

	def toString(self):
		print("[idTest = %d]" %(self.idTest))


