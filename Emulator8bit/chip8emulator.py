class Emulator:
	def __init__(self):
		self.hasexit() = 0
		self.keyinput = [0]*16 #keyboard input 16-button keyboard
		self.displayoutput = [0]*32*64 #output rom's details on 64x32 display with sound buzzer
		self.memory = [0]*4096 #memory of interpreter, fonts and rom details
		self.stack = []
		self.registers = [0]*16
		self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0
		self.opcode = 0
		self.vx = (self.opcode & 0x0f00)
		self.vy = (self.opcode & 0x00f0)
		self.functionlist = {0x00e0: self._0NN0, 0x00ee: self._0NNE, 0x1000: self._1NNN, 0x2000: self._2NNN, 0x3000: self._3NNN}

	def initialization(self): #reset all values of variables, start programcounter at 0x200
		self.keyinput = [0]*16
		self.displayoutput = [0]*32*64
		self.memory = [0]*4096
		self.registers = [0]*16
		self.stack = []
		self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0x200
		self.opcode = 0

	def loadrom(self):
		loadedrom = open("rominput.txt").read() #take in input from rom
		i = 0
		while i < len(loadedrom):
			self.memory[i + 0x200] = ord(loadedrom[i]) #put rom input into memory
			i += 1

	def _0NN0(self): #Clears the screen
		self.displayoutput = [0]*64*32

	def _0NNE(self): #Returns from a subroutine
		self.programcounter = self.stack

	def _1NNN(self): #Jumps to the address NNN
		self.programcounter = self.opcode & 0x0fff

	def _2NNN(self):
		self.programcounter = self.opcode & 0x0fff

	def _3NNN(self):
		if self.registers[self.vx] == (self.opcode & 0x00ff):
			self.programcounter += 2

	def _4NNN(self):
		if self.registers[self.vx] != (self.opcode & 0x00ff):
			self.programcounter += 2

	def _5NN0(self):
		if self.registers[self.vx] == self.registers[self.vy]:
			self.programcounter += 2

	def _6NNN(self):
		self.registers[self.vx] = self.opcode & 0x00ff

	def _7NNN(self):
		self.registers[self.vx] = self.registers[self.vx] + (self.opcode & 0x00ff)

	def _8NN0(self):
		self.vx = self.vy

	def _8NN1(self):
		self.vx = self.vx or self.vy

	def _8NN2(self):
		self.vx = self.vx and self.vy

	def _8NN3(self):
		self.vx = self.vx xor self.vy

	def _8NN4(self):
		self.vx = self.vx + self.vy

	def emulationloop(self):
		while self.hasexit is False:
			self.opcode = self.memory[self.programcounter] # check opcode against programcounter
			extractedopcode = self.opcode & 0xf000
			try:
				self.functionlist[extractedopcode] #call the opcode's associated function
			except:
				print "Unknown instruction"

			self.programcounter += 2

		else:
			sys.exit()


runemulator = Emulator()
runemulator.initialization()
runemulator.loadrom()
runemulator.emulationloop()