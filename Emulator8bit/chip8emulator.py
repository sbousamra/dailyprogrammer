import sys

class Emulator:
	def __init__(self):
		self.hasexit = 0
		self.keyinput = [0]*16 #keyboard input 16-button keyboard
		self.display = [0]*32*64 # rom's details on 64x32 display with sound buzzer
		self.memory = [0]*4096 #memory of interpreter, fonts and rom details
		self.stack = []
		self.stackpointer = 0
		# self.registers = [0]*16
		self.soundtimer = 0
		self.delaytimer = 0
		self.programcounter = 0x200
		self.v = [0]*16
		self.i = 0

	def load_rom(self):
		loadedrom = open("TETRIS", "rb").read() #take in input from rom
		
		i = 0
		while i < len(loadedrom):
			self.memory[i + 0x200] = loadedrom[i] #put rom input into memory
			i += 1

	def _0NNN(self, rawopcode): #used to correctly identify which 0 opcode is being used
		decodedopcode = (rawopcode & 0xf0ff)
		if decodedopcode == 0x00e0:
			self._00E0()

		elif decodedopcode == 0x00ee:
			self._00EE()

		else:
			print("Unknown _0NNN instruction " + rawopcode)

	def _00E0(self): #Clears the screen
		self.display = [0]*64*32

	def _00EE(self): #Returns from a subroutine
		self.programcounter = self.stack.pop()
		self.stackpointer = self.stackpointer - 1
		self.programcounter = self.programcounter + 2

	def _1NNN(self, rawopcode): #Jumps to the address NNN
		self.programcounter = (rawopcode & 0x0fff)

	def _2NNN(self, rawopcode):
		self.stackpointer = self.stackpointer + 1
		self.stack.append(self.programcounter)  
		self.programcounter = (rawopcode & 0x0fff)

	def _3XKK(self, rawopcode):
		if self.v[(rawopcode & 0x0f00) >> 8] == (rawopcode & 0x00ff):
			self.programcounter += 4
		else:
			self.programcounter += 2

	def _4XKK(self, rawopcode):
		if self.v[(rawopcode & 0x0f00) >> 8] != (rawopcode & 0x00ff):
			self.programcounter += 4
		else:
			self.programcounter +=2

	def _5XY0(self):
		if self.v[(rawopcode & 0x0f00) >> 8] == self.v[(rawopcode & 0x00f0) >> 4]:
			self.programcounter += 4
		else:
			self.programcounter +=2

	def _6XKK(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = (rawopcode & 0x00ff)
		self.programcounter = self.programcounter + 2

	def _7XNN(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] + (rawopcode & 0x00ff)
		self.programcounter = self.programcounter + 2

	def _8XYN(self, rawopcode): #used to correctly identify which 8 opcode is being used
		decodedopcode = (rawopcode & 0xf00f)
		if decodedopcode == 0x8000:
			self._8XY0(rawopcode)

		elif decodedopcode == 0x8001:
			self._8XY1()

		elif decodedopcode == 0x8002:
			self._8XY2()

		elif decodedopcode == 0x8003:
			self._8XY3()

		elif decodedopcode == 0x8004:
			self._8XY4()

		elif decodedopcode == 0x8005:
			self._8XY5()

		elif decodedopcode == 0x8006:
			self._8XY6()

		elif decodedopcode == 0x8007:
			self._8XY6()

		elif decodedopcode == 0x800e:
			self._8XYE()

	def _8XY0(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x00f0) >> 4]

	def _8XY1(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] | self.v[(rawopcode & 0x00f0) >> 4]

	def _8XY2(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] & self.v[(rawopcode & 0x00f0) >> 4]

	def _8XY3(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] ^ self.v[(rawopcode & 0x00f0) >> 4]

	def _8XY4(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] + self.v[(rawopcode & 0x00f0) >> 4]
		if self.v[(rawopcode & 0x00f0) >> 4] > self.v[(rawopcode & 0x0f00) >> 8]:
			self.vf = 1

		else:
			self.vf = 0

	def _8XY5(self, rawopcode):
		self.v[(rawopcode & 0x0f00) >> 8] = self.v[(rawopcode & 0x0f00) >> 8] - self.v[(rawopcode & 0x00f0) >> 4]
		if self.v[(rawopcode & 0x00f0) >> 4] > self.v[(rawopcode & 0x0f00) >> 8]:
			self.vf = 0

		else:
			self.vf = 1

	def _ANNN(self, rawopcode):
		self.i = (rawopcode & 0x0fff)
		self.programcounter = self.programcounter + 2

	def _DXYN(self, rawopcode):
		print(self.display)
		input("")
		self.programcounter = self.programcounter + 2


	def run_opcode(self, rawopcode):
		decodedopcode = (rawopcode & 0xf000)
		print("pc : " + hex(self.programcounter) + " executing rawopcode: " + hex(rawopcode) + " decodedopcode: " + hex(decodedopcode))

		if decodedopcode == 0x0000:
			self._0NNN(rawopcode)

		elif decodedopcode == 0x1000:
			self._1NNN(rawopcode)

		elif decodedopcode == 0x2000:
			self._2NNN(rawopcode)

		elif decodedopcode == 0x3000:
			self._3XKK(rawopcode)

		elif decodedopcode == 0x4000:
			self._4XKK(rawopcode)

		elif decodedopcode == 0x5000:
			self._5NNN(rawopcode)

		elif decodedopcode == 0x6000:
			self._6XKK(rawopcode)

		elif decodedopcode == 0x7000:
			self._7XNN(rawopcode)

		elif decodedopcode == 0xa000:
			self._ANNN(rawopcode)

		elif decodedopcode == 0xd000:
			self._DXYN(rawopcode)
		else:
			raise Exception("Unknown Opcode: " + hex(rawopcode))

	def emulation_loop(self):
		while True:
			# input("entertorunprogram")
			rawopcode = (self.memory[self.programcounter] << 8) | self.memory[self.programcounter + 1] # check opcode against programcounter
			self.run_opcode(rawopcode)	

			self.print_emulation_loop()

		else:
			sys.exit()

	def print_emulation_loop(self):
		print(" PC: " + str(hex(self.programcounter)) + " stack: " + str(self.stack) + " i: " + str(hex(self.i)) + "0:" + str(self.v))



runemulator = Emulator()
runemulator.load_rom()
runemulator.emulation_loop()