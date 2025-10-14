from House import House

def ShowHouseState(houseObj):
    if houseObj.GetDoor():
        print("Door is open")
    else:
        print("Door is closed")

    if houseObj.GetWindow():
        print("Window is open")
    else:
        print("Window is closed")
    # White space
    print()

# First using boolean values. Would be the easiest method in any other language

house = House(False, True)

ShowHouseState(house)

house.SetDoor(True)

ShowHouseState(house)

house.SetWindow(False)

ShowHouseState(house)