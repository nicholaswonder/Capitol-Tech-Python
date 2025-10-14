# WroldSeriesV1.py
# Problem 10 on page 404 Chap 7

def getData(fileName):
    rawData = []
    try:
        myFile = open(fileName, "r")
        for line in myFile:
            rawData.append(line)
        myFile.close()
    except IOError:
        print("File not found!")
    return rawData
def setMenu(data): # create a list of unique teams
    teams = []
    for item in data:
        unique = True
        for i in teams:
            if item == i:
                unique = False

        if unique == True:
            teams.append(item)
    return teams
def displayMenu(teams):
    counter = 1
    for team in teams:
        print(counter, ": ", team)
        counter += 1
    choice = int(input("Enter your team ID: "))
    return choice
def howManyWins(teamID, teams, rawData):
    numberOfWins = 0

    # BEGIN MY CODE
    print("You chose", teams[teamID - 1])
    for team in rawData:
        if team == teams[teamID - 1]:
            numberOfWins += 1
    # END MY CODE

    return numberOfWins
def main():
    myData = getData("WorldSeriesWinners.txt")
    print(myData) # test the raw list
    uniqueTeams = setMenu(myData)
    print(uniqueTeams) # test the list with unique teams
    option = displayMenu(uniqueTeams)
    print("This team won: ", howManyWins(option, uniqueTeams, myData))
main()