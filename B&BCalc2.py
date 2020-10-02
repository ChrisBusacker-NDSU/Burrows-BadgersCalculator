#A Calculator for the game of Burrows and Badgers to create warbands.
#By: Christopher Busacker Last Update: 10/2/2020
import numpy as np
from tkinter import *

root = Tk()
root.title('Burrows and Badgers Calculator')
root.geometry("1500x1000")

#Arrays with a lists of Species
#Dimesion one is the type of animal
#Dimesion 2 is the cost in pennies 
#Dimesion 3 is the size of the animal
speciesSmall = np.array([["Mouse","Shrew","Bird (S)","Bat"],
						[24,28,26,27],
						["Small","Small","Small","Small"]])
speciesMed = np.array([["Hedgehog","Squirrel","Mole","Weasel","Cat","Black Rat","Ferret","Rabbit","Toad","Frog","Adder","Bird (M)","Raptor (M)","Hound (M)","Marmot (R)","Green Lizard (R)","Siamese Cat (R)","Tortoise (R)","Platypus (R)"],
						[29,34,30,36,35,33,42,31,52,26,36,30,42,30,28,35,36,25],
						["Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium","Medium"]])
speciesLarge = np.array([["Hare","WildCat","Brown Rat","Fox","Otter","Bird (L)","Rapor (L)","Hound (L)","Racoon (R)","Armadillo (R)","Fennec Fox (R)"],
						[53,62,42,43,51,35,50,45,40,62,35],	
						["Large","Large","Large","Large","Large","Large","Large","Large","Large","Large","Large"]])
speciesMass = np.array([["Badger","Beaver","Bird (Ma)","Raptor (Ma)","Hound (Ma)"],
						[65,60,40,64,65],
						["Massive","Massive","Massive","Massive","Massive"]])
#size list
size = ["Small","Medium","Large","Massive",]					
#Array with the different Dens
denList = ["Abandoned Burrow","Ruined Farmstead","Town Building"]
#array with differnt Allegiances
allegiance = ["Royalists","Rogues","Freebeasts","Wildbeasts"]
#Weapons Array
weapon = np.array([["none","one-handed","double-handed","Polearm","Spear","Bow","Crossbow","Sling","Thowing knives","Pistols","Caliver","Blunderbuss"],
					[0,8,13,15,15,15,20,5,8,15,20,20]])
#Armour Array
armour = np.array([["none","light armour","heavy armour","very heavy armour","buckler","light shield","heavy shield"],
					[0,15,25,35,8,12,20]])
#Item array
item = np.array([["none","rope & hook","lucky charm","talisman","mage's focus","mage's pouch","camouflage cloak","scent masker","healing potion","broadhead arrows","bodkins arrows","lead slingshot","superior black powder"],	
					[0,6,15,4,15,10,15,5,5,1,1,1,1]])
#Character Special Array
special = np.array([[],
						[]])
#The max point limit for the warband is 350 points or also known as 350 pennys
maxPointLimit = 350

pointTotal = 0

#Leader of the Warbands info inputs
leader = Label(root, text = "Leader").grid(row = 0, column = 1) #bg = "blue"
leaderName = Label(root, text = "Name").grid(row = 1, column = 0) #bg = "light green"
leaderSize = Label(root, text = "Size").grid(row = 2, column = 0)
leaderRace = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 0)
leaderWeapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 0)
leaderWeapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 0)
leaderArmour1 = Label(root, text = "Armour 1").grid(row = 6,column = 0)
leaderArmour2 = Label(root, text = "Armour 2").grid(row = 7, column = 0)
leaderItem = Label(root, text = "Item").grid(row = 8, column = 0)
leaderSpecial = Label(root, text = "Special").grid(row = 9, column = 0)


def leader(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		leaderRaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 1)
	elif clicked1.get() == "Medium":
		leaderRaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 1)
	elif clicked1.get() == "Large":
		leaderRaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 1)
	else:
		leaderRaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 1)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

leaderSizeField = OptionMenu(root, clicked1, *size, command=leader).grid(row = 2, column = 1)

leaderWeapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 1)
leaderWeapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 1)
leaderArmour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 1)
leaderArmour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 1)
leaderItem = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 1)

#Member1 of the Warbands info inputs
member1 = Label(root, text = "Member1").grid(row = 0, column = 3) #bg = "blue"
member1Name = Label(root, text = "Name").grid(row = 1, column = 2) #bg = "light green"
member1Size = Label(root, text = "Size").grid(row = 2, column = 2)
member1Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 2)
member1Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 2)
member1Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 2)
member1Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 2)
member1Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 2)
member1Item = Label(root, text = "Item").grid(row = 8, column = 2)
member1Special = Label(root, text = "Special").grid(row = 9, column = 2)


def memberOne(event):
	#myLabel = Label(root, text=mclicked1.get())
	if mclicked1.get() == "Small":
		member1RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 3)
	elif mclicked1.get() == "Medium":
		member1RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 3)
	elif mclicked1.get() == "Large":
		member1RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 3)
	else:
		member1RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 3)


mclicked1 = StringVar()
mclicked2 = StringVar()
mclicked3 = StringVar()
mclicked4 = StringVar()
mclicked5 = StringVar()
mclicked6 = StringVar()
mclicked7 = StringVar()
mclicked8 = StringVar()
mclicked9 = StringVar()
mclicked10 = StringVar()

mclicked1.set(size[0])
mclicked2.set(speciesSmall[0])
mclicked3.set(speciesMed[0])
mclicked4.set(speciesLarge[0])
mclicked5.set(speciesMass[0])
mclicked6.set(weapon[0,0])
mclicked7.set(weapon[0,0])
mclicked8.set(armour[0,0])
mclicked9.set(armour[0,0])
mclicked10.set(item[0,0])

member1SizeField = OptionMenu(root, clicked1, *size, command=memberOne).grid(row = 2, column = 3)

member1Weapon1Field = OptionMenu(root, mclicked6, *weapon[0]).grid(row = 4, column = 3)
member1Weapon2Field = OptionMenu(root, mclicked7, *weapon[0]).grid(row = 5, column = 3)
member1Armour1Field = OptionMenu(root, mclicked8, *armour[0]).grid(row = 6, column = 3)
member1Armour2Field = OptionMenu(root, mclicked9, *armour[0]).grid(row = 7, column = 3)
member1Item = OptionMenu(root, mclicked10, *item[0]).grid(row = 8, column = 3)

#Member2 of the Warbands info inputs
member2 = Label(root, text = "Member2").grid(row = 0, column = 5) #bg = "blue"
member2Name = Label(root, text = "Name").grid(row = 1, column = 4) #bg = "light green"
member2Size = Label(root, text = "Size").grid(row = 2, column = 4)
member2Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 4)
member2Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 4)
member2Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 4)
member2Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 4)
member2Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 4)
member2Item = Label(root, text = "Item").grid(row = 8, column = 4)
member2Special = Label(root, text = "Special").grid(row = 9, column = 4)


def memberTwo(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member2RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 5)
	elif clicked1.get() == "Medium":
		member2RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 5)
	elif clicked1.get() == "Large":
		member2RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 5)
	else:
		member2RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 5)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member2SizeField = OptionMenu(root, clicked1, *size, command=memberTwo).grid(row = 2, column = 5)

member2Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 5)
member2Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 5)
member2Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 5)
member2Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 5)
member2Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 5)

#Member3 of the Warbands info inputs
member3 = Label(root, text = "Member3").grid(row = 0, column = 7) #bg = "blue"
member3Name = Label(root, text = "Name").grid(row = 1, column = 6) #bg = "light green"
member3Size = Label(root, text = "Size").grid(row = 2, column = 6)
member3Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 6)
member3Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 6)
member3Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 6)
member3Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 6)
member3Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 6)
member3Item = Label(root, text = "Item").grid(row = 8, column = 6)
member3Special = Label(root, text = "Special").grid(row = 9, column = 6)


def memberThree(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member3RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 7)
	elif clicked1.get() == "Medium":
		member3RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 7)
	elif clicked1.get() == "Large":
		member3RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 7)
	else:
		member3RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 7)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member3SizeField = OptionMenu(root, clicked1, *size, command=memberThree).grid(row = 2, column = 7)

member3Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 7)
member3Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 7)
member3Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 7)
member3Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 7)
member3Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 7)

#Member4 of the Warbands info inputs
member4 = Label(root, text = "Member4").grid(row = 0, column = 9) #bg = "blue"
member4Name = Label(root, text = "Name").grid(row = 1, column = 8) #bg = "light green"
member4Size = Label(root, text = "Size").grid(row = 2, column = 8)
member4Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 8)
member4Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 8)
member4Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 8)
member4Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 8)
member4Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 8)
member4Item = Label(root, text = "Item").grid(row = 8, column = 8)
member4Special = Label(root, text = "Special").grid(row = 9, column = 8)

def memberFour(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member4RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 9)
	elif clicked1.get() == "Medium":
		member4RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 9)
	elif clicked1.get() == "Large":
		member4RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 9)
	else:
		member4RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 9)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member4SizeField = OptionMenu(root, clicked1, *size, command=memberFour).grid(row = 2, column = 9)

member4Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 9)
member4Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 9)
member4Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 9)
member4Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 9)
member4Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 9)

#Member5 of the Warbands info inputs
member5 = Label(root, text = "Member5").grid(row = 0, column = 11) #bg = "blue"
member5Name = Label(root, text = "Name").grid(row = 1, column = 10) #bg = "light green"
member5Size = Label(root, text = "Size").grid(row = 2, column = 10)
member5Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 10)
member5Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 10)
member5Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 10)
member5Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 10)
member5Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 10)
member5Item = Label(root, text = "Item").grid(row = 8, column = 10)
member5Special = Label(root, text = "Special").grid(row = 9, column = 10)

def memberFive(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member5RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 11)
	elif clicked1.get() == "Medium":
		member5RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 11)
	elif clicked1.get() == "Large":
		member5RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 11)
	else:
		member5RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 11)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member5SizeField = OptionMenu(root, clicked1, *size, command=memberFive).grid(row = 2, column = 11)

member5Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 11)
member5Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 11)
member5Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 11)
member5Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 11)
member5Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 11)

#Member6 of the Warbands info inputs
member6 = Label(root, text = "Member6").grid(row = 0, column = 13) #bg = "blue"
member6Name = Label(root, text = "Name").grid(row = 1, column = 12) #bg = "light green"
member6Size = Label(root, text = "Size").grid(row = 2, column = 12)
member6Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 12)
member6Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 12)
member6Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 12)
member6Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 12)
member6Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 12)
member6Item = Label(root, text = "Item").grid(row = 8, column = 12)
member6Special = Label(root, text = "Special").grid(row = 9, column = 12)

def memberSix(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member6RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 13)
	elif clicked1.get() == "Medium":
		member6RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 13)
	elif clicked1.get() == "Large":
		member6RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 13)
	else:
		member6RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 13)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member6SizeField = OptionMenu(root, clicked1, *size, command=memberSix).grid(row = 2, column = 13)

member6Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 13)
member6Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 13)
member6Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 13)
member6Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 13)
member6Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 13)

#Member7 of the Warbands info inputs
member6 = Label(root, text = "Member7").grid(row = 0, column = 15) #bg = "blue"
member6Name = Label(root, text = "Name").grid(row = 1, column = 14) #bg = "light green"
member6Size = Label(root, text = "Size").grid(row = 2, column = 14)
member6Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 14)
member6Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 14)
member6Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 14)
member6Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 14)
member6Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 14)
member6Item = Label(root, text = "Item").grid(row = 8, column = 14)
member6Special = Label(root, text = "Special").grid(row = 9, column = 14)

def memberSeven(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member7RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 15)
	elif clicked1.get() == "Medium":
		member7RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 15)
	elif clicked1.get() == "Large":
		member7RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 15)
	else:
		member7RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 15)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member7SizeField = OptionMenu(root, clicked1, *size, command=memberSeven).grid(row = 2, column = 15)

member7Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 15)
member7Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 15)
member7Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 15)
member7Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 15)
member7Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 15)

#Member8 of the Warbands info inputs
member8 = Label(root, text = "Member8").grid(row = 0, column = 17) #bg = "blue"
member8Name = Label(root, text = "Name").grid(row = 1, column = 16) #bg = "light green"
member8Size = Label(root, text = "Size").grid(row = 2, column = 16)
member8Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 16)
member8Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 16)
member8Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 16)
member8Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 16)
member8Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 16)
member8Item = Label(root, text = "Item").grid(row = 8, column = 16)
member8Special = Label(root, text = "Special").grid(row = 9, column = 16)

def memberEight(event):
	#myLabel = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member8RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 17)
	elif clicked1.get() == "Medium":
		member8RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 17)
	elif clicked1.get() == "Large":
		member8RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 17)
	else:
		member8RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 17)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member8SizeField = OptionMenu(root, clicked1, *size, command=memberEight).grid(row = 2, column = 17)

member8Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 17)
member8Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 17)
member8Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 17)
member8Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 17)
member8Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 17)

#Member9 of the Warbands info inputs
member9 = Label(root, text = "Member9").grid(row = 0, column = 19) #bg = "blue"
member9Name = Label(root, text = "Name").grid(row = 1, column = 18) #bg = "light green"
member9Size = Label(root, text = "Size").grid(row = 2, column = 18)
member9Race = Label(root, text = "Race", bg = "light green").grid(row = 3, column = 18)
member9Weapon1 = Label(root, text = "Weapon 1").grid(row = 4,column = 18)
member9Weapon2 = Label(root, text = "Weapon 2").grid(row = 5,column = 18)
member9Armour1 = Label(root, text = "Armour 1").grid(row = 6,column = 18)
member9Armour2 = Label(root, text = "Armour 2").grid(row = 7, column = 18)
member9Item = Label(root, text = "Item").grid(row = 8, column = 18)
member9Special = Label(root, text = "Special").grid(row = 9, column = 18)

def memberNine(event):
	myLabel9 = Label(root, text=clicked1.get())
	if clicked1.get() == "Small":
		member9RaceField = OptionMenu(root, clicked2, *speciesSmall[0]).grid(row = 3, column = 19)
	elif clicked1.get() == "Medium":
		member9RaceField = OptionMenu(root, clicked3, *speciesMed[0]).grid(row = 3, column = 19)
	elif clicked1.get() == "Large":
		member9RaceField = OptionMenu(root, clicked4, *speciesLarge[0]).grid(row = 3, column = 19)
	else:
		member9RaceField = OptionMenu(root, clicked5, *speciesMass[0]).grid(row = 3, column = 19)


clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()
clicked7 = StringVar()
clicked8 = StringVar()
clicked9 = StringVar()
clicked10 = StringVar()

clicked1.set(size[0])
clicked2.set(speciesSmall[0])
clicked3.set(speciesMed[0])
clicked4.set(speciesLarge[0])
clicked5.set(speciesMass[0])
clicked6.set(weapon[0,0])
clicked7.set(weapon[0,0])
clicked8.set(armour[0,0])
clicked9.set(armour[0,0])
clicked10.set(item[0,0])

member9SizeField = OptionMenu(root, clicked1, *size, command=memberNine).grid(row = 2, column = 19)

member9Weapon1Field = OptionMenu(root, clicked6, *weapon[0]).grid(row = 4, column = 19)
member9Weapon2Field = OptionMenu(root, clicked7, *weapon[0]).grid(row = 5, column = 19)
member9Armour1Field = OptionMenu(root, clicked8, *armour[0]).grid(row = 6, column = 19)
member9Armour2Field = OptionMenu(root, clicked9, *armour[0]).grid(row = 7, column = 19)
member9Item = OptionMenu(root, clicked10, *item[0]).grid(row = 8, column = 19)


def CalcList(leaderSize,leaderRaceField, leaderWeapon1Field,leaderWeapon2Field,leaderArmour1Field,leaderArmour2Field,leaderItem):
	if leaderSize == "small":
		for i in speciesSmall:
			if speciesSmall[i]==leaderRaceField:
				pointTotal + speciesSmall[i,1]
				




#def clicker(event):
	#displayLabel = Label(root, text="Total Pennies =" + pointTotal).grid(row = 10, column = 1) 

#myButton = Button(root, text="Calc").grid(row = 10, column = 0)



root.mainloop()
