import sys

class Emulator:
	def __init__(self):
		self.hasexit = 0
		self.keyinput = [0]*16 #keyboard input 16-button keyboard
		self.displayoutput = [0]*32*64 #output rom's details on 64x32 display with sound buzzer
		self.memory = [0]*4096 #memory of interpreter, fonts and rom details
		self.stack = []
		# self.registers = [0]*16
		self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0
		self.opcode = 0
		self.vx = (self.opcode & 0x0f00)
		self.vy = (self.opcode & 0x00f0)
		self.i = (self.opcode & 0x0fff)
		self.functionlist = {0xa000: self._ANNN}

	def initialization(self): #reset all values of variables, start programcounter at 0x200
		self.keyinput = [0]*16
		self.displayoutput = [0]*32*64
		self.memory = [0]*4096
		# self.registers = [0]*16
		self.stack = []
		self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0x200
		self.opcode = 0

	def loadrom(self):
		loadedrom = open("TETRIS", "rb").read() #take in input from rom
		
		i = 0
		while i < len(loadedrom):
			self.memory[i + 0x200] = loadedrom[i] #put rom input into memory
			i += 1

	# def _0NNN(self): #used to correctly identify which 0 opcode is being used
	# 	extractedopcode = (self.opcode & 0xf0ff)
	# 	try:
	# 		self.functionlist[extractedopcode]()
	# 	except:
	# 		print ("Unknown Instruction")

	# def _0NN0(self): #Clears the screen
	# 	self.displayoutput = [0]*64*32

	# def _0NNE(self): #Returns from a subroutine
	# 	self.programcounter = self.stack

	# def _1NNN(self): #Jumps to the address NNN
	# 	self.programcounter = (self.opcode & 0x0fff)

	# def _2NNN(self):
	# 	self.programcounter = (self.opcode & 0x0fff)

	# def _3NNN(self):
	# 	if self.vx == (self.opcode & 0x00ff):
	# 		self.programcounter += 2

	# def _4NNN(self):
	# 	if self.vx != (self.opcode & 0x00ff):
	# 		self.programcounter += 2

	# def _5NN0(self):
	# 	if self.vx == self.vy:
	# 		self.programcounter += 2

	# def _6NNN(self):
	# 	self.vx = (self.opcode & 0x00ff)

	# def _7NNN(self):
	# 	self.vx = self.vx + (self.opcode & 0x00ff)

	# def _8NNN(self): #used to correctly identify which 8 opcode is being used
	# 	extractedopcode = (self.opcode & 0xf00f)
	# 	try:
	# 		self.functionlist[extractedopcode]()
	# 	except:
	# 		print ("Unknown Instruction")

	# def _8NN0(self):
	# 	self.vx = self.vy

	# def _8NN1(self):
	# 	self.vx = self.vx | self.vy

	# def _8NN2(self):
	# 	self.vx = self.vx & self.vy

	# def _8NN3(self):
	# 	self.vx = self.vx ^ self.vy

	# def _8NN4(self):
	# 	self.vx = self.vx + self.vy

	# def _8NN5(self):

	def _ANNN(self):
		self.i = (self.opcode & 0x0fff)


	def emulationloop(self):

		while self.hasexit is False:
			input(entertorunprogram)
			self.opcode = self.memory[self.programcounter] # check opcode against programcounter
			extractedopcode = self.opcode & 0xf000
			try:
				self.functionlist[extractedopcode]() #call the opcode's associated function
			except:
				print ("Unknown instruction")

			self.programcounter += 2
			printemulationloop()

		else:
			sys.exit()

	def printemulationloop(self):
		print (self.memory)
		print (self.programcounter)
		print (self.registers)
		print (self.stack)
		print (self.opcode)



runemulator = Emulator()
runemulator.initialization()
runemulator.loadrom()
runemulator.printemulationloop()
runemulator.emulationloop()



# 0x0000: self._0NNN, 0x00e0: self._0NN0, 0x00ee: self._0NNE, 0x1000: self._1NNN, 0x2000: self._2NNN, 0x3000: self._3NNN, 0x4000: self._4NNN, 0x5000: self._5NN0, 0x6000: self._6NNN, 0x7000: self._7NNN, 0x8000: self._8NNN, 0x8001: self._8NN0, 0x8002: self._8NN1,