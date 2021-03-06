import random
import Tkinter
import time
import os

#Setting all Initial Values
table = Tkinter.Tk()
table.configure(background = "green")
bet = 0
uMoney = 1000
dHand = 0
uHand = 0
dLine = "Dealer's hand:"
uLine = "Your hand: "
dCardImages = []
uCardPosition = 83
dCardPosition = 83

class card:
	suit = ""
	value = 0
	wasUsed = False
	cardLocation = "card.gif"
	cardLocationString = "cards"
	image = Tkinter.PhotoImage(file=cardLocation)
	def stringIt(self):
		output = " " + str(self.value) + " of "+ self.suit
		return output

class faceCard(card):
	face = ""
	def stringIt(self): 
		output = " " + self.face + " of " + self.suit
		return output

#Set Deck
cardDeck = []
faces = ["Jack", "Queen", "King", "Ace"]
facesFirstL = ["J", "Q", "K", "A"]
suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

for j in range(4):
	for i in range(13):
		if i > 8:
			newCard = faceCard()
			newCard.face = faces[9 - i]
			newCard.value = 10
			newCard.cardLocationString = os.path.join(newCard.cardLocationString, facesFirstL[9 - i])
		else:
			newCard = card()
			index = i + 2
			newCard.cardLocationString = os.path.join(newCard.cardLocationString, str(index))
			newCard.value = index

		newCard.cardLocationString += suits[j][:1] + ".gif"
		newCard.cardLocation = newCard.cardLocationString
		newCard.image = Tkinter.PhotoImage(file = newCard.cardLocationString)
		newCard.suit = suits[j]
		cardDeck.append(newCard)

def resetAll():
	global dCardImages
	global uHand
	global dHand
	global uLine
	global dLine
	global dCardPosition
	global uCardPosition
	global cardTrayLabel
	global cardDeck
	for thisCard in cardDeck:
		thisCard.wasUsed = False
	dCardImages = []
	uHand = 0
	dHand = 0
	uLine = "Your Hand: "
	dLine = "Dealer's Hand: "
	uCardPosition = 83
	dCardPosition = 83
	cardTrayLabel.destroy()
	cardTray = Tkinter.PhotoImage(file = "greenBox 4.gif")
	cardTrayLabel = Tkinter.Label(image = cardTray)
	cardTrayLabel.image = cardTray
	cardTrayLabel.place(x = 83, y = 100)

def showCards(winner):
	global dCardImages
	global uMoney
	global instLabel
	global sb
	global hb
	global betInput
	global bb
	global bet
	global label
	pos = 83
	for i in dCardImages:
		cardImage = i.image
		blankCard = Tkinter.Label(image = cardImage)
		blankCard.image = cardImage
		blankCard.place(x = pos, y = 100)
		pos += 100
	sb.configure(state = "disabled")
	hb.configure(state = "disabled")
	betInput.configure(state = "normal")
	bb.configure(state = "normal")
	if winner == "draw":
		label.configure(text = "It's a draw")
	elif winner == "u":
		label.configure(text = "You win!")
		uMoney += bet
	elif winner == "d":
		label.configure(text = "Dealer wins!")
		uMoney -= bet
	instLabel.configure(text = "Bet to start (Bet 0 to quit)")
	scoreLabel.configure(text = 'Total Money: $' + str(uMoney) + '\nYour Hand Value: ' + str(uHand))

def checkWin(uStayed):
	global uHand
	global dHand
	global uLine
	global dLine
	if uHand > 21 and dHand > 21:
		showCards("draw")
	elif dHand > 21:
		showCards("u")
	elif uHand > 21:
		showCards("d")
	elif uStayed:
		if uHand > dHand:
			showCards("u")
		elif dHand > uHand:
			showCards("d")
		else:
			showCards("draw")

def hitButton():
	global dCardPosition
	global uCardPosition
	global dHand
	global dLine
	global cardDeck
	global uHand
	global uLine
	global dCardImages
	label.configure(text = "Dealing...")
	rand = random.randint(0,51)
	thisCard = cardDeck[rand]
	while thisCard.wasUsed:
		rand = random.randint(0,51)
		thisCard = cardDeck[rand]
	if dHand < 16:
		dHand += thisCard.value
		dLine += thisCard.stringIt()
		cardDeck[rand].wasUsed = True
		cardImage = Tkinter.PhotoImage(file = "card.gif")
		blankCard = Tkinter.Label(image = cardImage)
		blankCard.image = cardImage
		dCardImages.append(thisCard)
		blankCard.place(x = dCardPosition, y = 100)
		dCardPosition += 100

	rand = random.randint(0,51)
	thisCard = cardDeck[rand]
	while thisCard.wasUsed:
		rand = random.randint(0,51)
		thisCard = cardDeck[rand]
	cardDeck[rand].wasUsed = True
	uHand += thisCard.value
	uLine += thisCard.stringIt()
	cardImage = thisCard.image
	blankCard = Tkinter.Label(image = cardImage)
	blankCard.image = cardImage
	blankCard.place(x = uCardPosition, y = 470)
	uCardPosition += 100
	scoreLabel.configure(text = 'Total Money: $' + str(uMoney) + '\nYour Hand Value: ' + str(uHand))
	checkWin(False)

def stayButton():
	global dCardPosition
	global dHand
	global dCardImages
	global dLine
	while dHand < 16:
		#do stuff
		rand = random.randint(0,51)
		thisCard = cardDeck[rand]
		while thisCard.wasUsed:
			rand = random.randint(0,51)
			thisCard = cardDeck[rand]
		dHand += thisCard.value
		dLine += thisCard.stringIt()
		cardDeck[rand].wasUsed = True
		cardImage = Tkinter.PhotoImage(file = "card.gif")
		blankCard = Tkinter.Label(image = cardImage)
		blankCard.image = cardImage
		dCardImages.append(thisCard)
		blankCard.place(x = dCardPosition, y = 100)
		dCardPosition += 100
	checkWin(True)

def makeBet():
	global dCardPosition
	global uCardPosition
	global betInput
	global bet
	global dCardImages
	global table
	global instLabel
	global scoreLabel
	global uLine
	global uHand
	global dLine
	global dHand
	resetAll()
	bet = int(betInput.get())
	if bet == 0:
		table.destroy()
	label.configure(text = "Dealing...")
	rand = random.randint(0,51)
	thisCard = cardDeck[rand]
	while thisCard.wasUsed:
		rand = random.randint(0,51)
		thisCard = cardDeck[rand]
	dHand += thisCard.value
	dLine += thisCard.stringIt()
	cardImage = thisCard.image
	blankCard = Tkinter.Label(image = cardImage)
	blankCard.image = cardImage
	dCardImages.append(thisCard)
	blankCard.place(x = dCardPosition, y = 100)
	dCardPosition += 100
	cardDeck[rand].wasUsed = True
	rand = random.randint(0,51)
	thisCard = cardDeck[rand]
	while thisCard.wasUsed:
		rand = random.randint(0,51)
		thisCard = cardDeck[rand]
	cardDeck[rand].wasUsed = True
	uHand += thisCard.value
	uLine += thisCard.stringIt()
	cardImage = thisCard.image
	blankCard = Tkinter.Label(image = cardImage)
	blankCard.image = cardImage
	blankCard.place(x = uCardPosition, y = 470)
	uCardPosition += 100
	instLabel.configure(text = "Hit or stay")
	hb.configure(state = "normal")
	sb.configure(state = "normal")
	betInput.configure(state = "disabled")
	bb.configure(state = "disabled")
	scoreLabel.configure(text = 'Total Money: $' + str(uMoney) + '\nYour Hand Value:' + str(uHand))

	# Interface
table.geometry("1500x750")
table.resizable(0,0)
label = Tkinter.Label(table, padx = 5, text = "Welcome to Black Jack!", background = "green")
instLabel = Tkinter.Label(table, text =  "Bet to start (Bet 0 to quit)", background = "green")
scoreLabel = Tkinter.Label(table, text = 'Total Money: $' + str(uMoney) + '\nYour Hand Value: ' + str(uHand), background = "green")
hb = Tkinter.Button(table, highlightbackground = "green", text = "Hit?", command = hitButton, state = "disabled")
sb = Tkinter.Button(table, highlightbackground = "green", text = "Stay?", command = stayButton, state = "disabled")
bb = Tkinter.Button(table, highlightbackground = "green", text = "Bet it!", command = makeBet)
betInput = Tkinter.Entry(table)
cardTray = Tkinter.PhotoImage(file = "greenBox 4.gif")
cardTrayLabel = Tkinter.Label(image = cardTray)
cardTrayLabel.place(x = 83, y = 100)
label.pack()
instLabel.pack()
scoreLabel.place(x = 10, y = 10)
hb.place(x = 590, y = 650)
sb.place(x = 850, y = 650)
bb.pack(side = "bottom")
betInput.pack(side = "bottom")
table.mainloop()
