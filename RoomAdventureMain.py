class Room(object):
	def __init__(self,name):
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,value):
		self._name = value
	@property
	def exits(self):
		return self._exits
	@exits.setter
	def exits(self, value):
		self._exits = value
	@property
	def exitLocations(self):
		return self._exitLocations
	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value
	@property
	def items(self):
		return self._items
	@items.setter
	def items(self, value):
		self._items = value
	@property
	def itemDescriptions(self):
		return self._itemDescriptions
	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value
	@property
	def grabbables(self):
		return self._grabbables
	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	def addExit(self,exit,room):
		self._exits.append(exit)
		self._exitLocations.append(room)

	def addItem(self,item,desc):
		self._items.append(item)
		self._itemDescriptions.append(desc)
	def addGrabbable(self,item):
		self._grabbables.append(item)

	def delGrabbable(self,item):
		self._grabbables.remove(item)

	def __str__(self):
		s = f"You are in {self.name}. \n"
		s += "You see: "
		for item in self.items:
			s += item + " "
		s += "\n"

		s += "Exits: "

		for exit in self.exits:
			s += exit + " "
		return s

def createRooms():
	global currentRoom

	r1 = Room("Room 1 15pts EASY")
	r2 = Room("Room 2 35pts MEDIUM")
	r3 = Room("Room 3 EASY")
	r4 = Room("Room 4 HARD")

	# Room1 Setup
	r1.addItem("Painting","its just the aphabet backwards?")

	# Room2 Setup
	# Room3 Setup
	r3.addItem("Bookshelf","its weird, every book is either Red Or Blue?")
	r3.addItem("Paper","01010101011100110110010100100000001110000010000001100010011010010111010000100000011000100110100101101110011000010111001001111001")
	# Room4 Setup
	r4.addItem("Plaque","Solve each room to complete the bigger picture. It's initials say R.S.A")



###########################################################
####################   Main    ############################
###########################################################

inventory = []
createRooms()
currentRoom = r1

while True:
	status = f"{currentRoom}\nYou are carrying: {inventory}\n"

	print("==================================================")
	print(status)

	action = input("What to do? ")
	action = action.lower()

	if (action == "quit" or action == "exit" or action == "bye"):
		break

	response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
	words = action.split()

	if (len(words) == 2):
		verb = words[0]
		noun = words[1]

	if(verb == "go"):
		response = "Invalid exit"

		for i in range(len(currentRoom.exits)):
			if(noun == currentRoom.exits[i]):
				currentRoom = currentRoom.exitLocations[i]
				response = "Room changed."
				break
	elif (verb == "look"):
		response = "I don't see that item."
		for i in range(len(currentRoom.items)):
			if(noun == currentRoom.items[i]):
				response = currentRoom.itemDescriptions[i]
				break
	elif(verb == "take"):
		response = "I don't see that item."
		for grabbable in currentRoom.grabbables:
			if (noun == grabbable):
				inventory.append(grabbable)
				currentRoom.delGrabbable(grabbable)
				response = "Item grabbed."
				break
	print(f"\n{response}")

