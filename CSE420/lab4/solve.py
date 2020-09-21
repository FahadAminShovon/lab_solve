from typing import List, Set
import re

METHOD_REGEX = '(public|private)\s(static\s)?(int|String|void|double)\s(\w*\d*)'
METHOD_NAME_SEPARTOR_REGEX = '(public|private)\s(static\s)?(int|String|void|double)\s'

class Solve:

	def __init__(self,file_path:str):
		self.file = file_path
		self.results = []
		
	def analyze(self):
		with open(self.file, 'r') as file:
			Lines = file.readlines()
			for line in Lines:
				if(re.match(METHOD_REGEX, line)):
					self.perser(line)

	def perser(self, line:str):
		line = line.rsplit('\n')[0]
		methods_return_type = re.split(METHOD_NAME_SEPARTOR_REGEX , line)
		method_name, return_type =  methods_return_type[-1], methods_return_type[-2]
		self.results.append([method_name, return_type])

	def printer(self):
		print('Methods: ')
		for result in self.results:
			print(f'{result[0]}, return type: {result[1]}')



if __name__ == "__main__":
	solve = Solve('./input.txt')
	solve.analyze()
	solve.printer()