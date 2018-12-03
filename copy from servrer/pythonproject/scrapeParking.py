# Copyright 2018

import bs4
import requests
import requests_cache

requests_cache.install_cache("parking_cache", expire_after=30)

def getParking(): 
    # Get parking page 
    try:
        parkingPage = requests.get("https://v2.aitapps.iu.edu/INPARK_LotCount_V1_Online/IN")
        parkingPage.raise_for_status
    except Exception as exc:
        print("Error " + exc)
        return "Could not fetch parking data"

    # bs4 the parking page
    parking = bs4.BeautifulSoup(parkingPage.text, 'html.parser')
    # get all elements with class=content
    locations = parking.select(".content")

    livestats = {}
    totalstats = {}

    for location in locations:
        # get h1 from first div
        name = location.select("div h1")
        name = name[0].getText()

        # get available spots
        stats = location.select("div div p")
        stats = stats[0].getText()
        available = stats.split("Available: ")
        available = available[1].split("\r\n")
        available = available[0]

        # get total spots
        total = stats.split("Capacity: ")
        total = total[1].split("\r\n")
        total = total[0]
        info = name + ": " + available
        print(info)
        
        # add available slots to dictionary
        livestats[name] = available
        totalstats[name] = total

    return [livestats, totalstats]


def getLot(lot):
    try: 
        parking = getParking()
    except Exception as exc:
        return "Could not fetch parking data"

    parkingInfo = []

    if lot.startswith("xf") or lot.startswith("blackford garage") or lot.startswith("blackford"): 
        parkingInfo.append(parking[0]["Blackford Garage"])
        parkingInfo.append("Blackford Garage")
        parkingInfo.append(parking[1]["Blackford Garage"])
    elif lot.startswith("xh") or lot.startswith("barnhill garage") or lot.startswith("barnhill"): 
        parkingInfo.append(parking[0]["Barnhill Garage"])
        parkingInfo.append("Barnhill Garage")
        parkingInfo.append(parking[1]["Barnhill Garage"])
    elif lot.startswith("xl") or lot.startswith("gateway garage") or lot.startswith("gateway"): 
        parkingInfo.append(parking[0]["Gateway Garage"])
        parkingInfo.append("Gateway Garage")
        parkingInfo.append(parking[1]["Gateway Garage"])
    elif lot.startswith("xp") or lot.startswith("riverwalk garage") or lot.startswith("riverwalk"): 
        parkingInfo.append(parking[0]["Riverwalk Garage"])
        parkingInfo.append("Riverwalk Garage")
        parkingInfo.append(parking[1]["Riverwalk Garage"])
    elif lot.startswith("xd") or lot.startswith("sports garage") or lot.startswith("sports"): 
        parkingInfo.append(parking[0]["Sports Garage"])
        parkingInfo.append("Sports Garage")
        parkingInfo.append(parking[1]["Sports Garage"])
    elif lot.startswith("wx") or lot.startswith("lockefield garage") or lot.startswith("lockefield") or lot.startswith("lockefield student garage"): 
        parkingInfo.append(parking[0]["Lockefield Student Garage"])
        parkingInfo.append("Lockefield Student Garage")
        parkingInfo.append(parking[1]["Lockefield Student Garage"])

    return parkingInfo