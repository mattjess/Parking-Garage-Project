#Barnhill Garage "XH" ST Spaces:1324
#Gateway Garage "XL" ST Spaces:1308
#Blackford Garage "XF" ST Spaces: 862
#Sports Garage "XD" ST Spaces: 867
#Riverwalk Garage "XP" ST Spaces: 493

#########
XHOpen=433
XLOpen=200
XFOpen=456
XDOpen=149
XPOpen=35

XHTotal=1324
XLTotal=1308
XFTotal=862
XDTotal=867
XPTotal=493
##########

#User will send a text with one of the above Campus building codes
#This will respond with the current available parking spots in the garage
#Will also respond in the smae line with the percentage of spots taken
#Barnhill Garage currently has 230 available parking spaces with 17% of parking spots taken.

print("Below is a list of the Codes for each parking garage")
print("Barnhill Garage: XH")
print("Gateway Garage: XL")
print("Blackford Garage: XF")
print("Sports Garage: XD")
print("Riverwalk Garage: XP")
print("Enter the Campus Building code for the garage you want to park in and,")
print("I will tell your the current parking spots aviability")
userInput=input("Ender Code here: ")
if userInput == 'XH':
	print("Barnhill Garage currently has " + str(XHOpen)+ " available parking spaces with " + str(round((XHOpen/XHTotal), 2) + "% of parking spots taken.")
else:
	print("error please only enter the camus building code")