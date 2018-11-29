
BarnhillGarage = "BarnhillG.csv"
BarnhillG = open(BarnhillGarage, 'r')
BarnhillG.readline()
for eachline in BarnhillG:
	BarnhillData = eachline.split(",")

BlackfordGarage = "BlackfordG.csv"
BlackfordG = open(BlackfordGarage, 'r')
BlackfordG.readline()
for eachline in BlackfordG:
	BlackfordData = eachline.split(",")

GatewayGarage = "GatewayG.csv"
GatewayG = open(GatewayGarage, 'r')
GatewayG.readline()
for eachline in GatewayG:
	GatewayData = eachline.split(",")

RiverwalkGarage = "RiverwalkG.csv"
RiverwalkG = open(RiverwalkGarage, 'r')
RiverwalkG.readline()
for eachline in RiverwalkG:
	RiverwalkData = eachline.split(",")

SportsGarage = "SportsG.csv"
SportsG = open(SportsGarage, 'r')
SportsG.readline()
for eachline in SportsG:
	SportsData = eachline.split(",")

# a function to input garage, day, and time.  
# a = Garage 
# b = Day
# c = Time
def search("a", b):

	Divider = 49
	
	if a = "BarnhillGarage":
		SumSpots += int(BarnhillData[b])
		if int(BarnhillData[b]) = "":
			Divider -= 1


	elif a = "BlackfordGarage":
		SumSpots += int(BlackfordData[b])
		if int(BlackfordData[b]) = "":
			Divider -= 1

	elif a = "GatewayGarage":
		SumSpots += int(GatewayData[b])
		if int(GatewayData[b]) = "":
			Divider -= 1

	elif a = "RiverwalkGarage":
		SumSpots += int(RiverwalkData[b])
		if int(RiverwalkData[b]) = "":
			Divider -= 1

	elif a = "SportsGarage":
		SumSpots += int(SportsData[b])
		if int(SportsData[b]) = "":
			Divider -= 1

	else: 
		Print("Error")


	SpotsLeft = SumSpots % Divider
	return SumSpots

search(BarnhillGarage, 3)