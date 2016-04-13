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

	def initialization(): #reset all values of variables, start programcounter at 0x200
		self.keyinput = [0]*16
		self.displayoutput = [0]*32*64
   		self.memory = [0]*4096
    	self.registers = [0]*16
    	self.stack = []
    	self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0x200
		self.opcode = 0

	def loadrom():
		loadedrom = open("rominput.txt").read() #take in input from rom
		i = 0
    	while i < len(binary):
      		self.memory[i + 0x200] = ord(loadedrom[i]) #put rom input into memory
      		i += 1

	def opcode():
		if self.opcode 

	def emulationloop():
		while self.hasexit is False:
			self.opcode = self.memory[self.programcounter] # check opcode against programcounter
			opcode(self.opcode)
			self.programcounter += 2

		else:
			sys.exit()