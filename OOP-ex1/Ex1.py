import sys
import json
from Call import Call, Calls
from Building import Building

theBuilding=Building() # creating a building
theBuilding.loadJson(sys.argv[1]) # getting the building attributes from the json file

theCall=Calls() # creating a calls object
theCall.loadCSV(sys.argv[2]) #  getting the calls attributes from the csv file

# this method is calculating the expected time to finish a call
def timeToFinish(numberOfCall, elev):
    lastCallOfLift = theCall.lastTimeCalled(elev._id)
    temp = elev.timeForTravel(elev._lastFloor,theCall._calls[numberOfCall]._srcFloor) #the time for elevator to go from its current position to the source floor of the next call
    time = max(theCall._calls[numberOfCall]._time,theCall._calls[lastCallOfLift]._endTime + temp) #setting the time that the call will expected to start the new call
    time = time + elev.timeForTravel(theCall._calls[numberOfCall]._srcFloor,theCall._calls[numberOfCall]._destFloor)
    return time

# this method is allocating the elevator to the call
def allocating(numberOfCall, elev):
    theCall._calls[numberOfCall]._endTime=timeToFinish(numberOfCall,elev) #setting end time of the call
    theCall._calls[numberOfCall]._assignment= elev._id
    elev._lastFloor=theCall._calls[numberOfCall]._destFloor # saving the position of the elevator after taking care of the call

# this method returns the elevator that will get to the floor the fastest
def theFastesetLiftToCome(floor):
    ans=0
    time=float('inf')
    for elev in theBuilding._elevators:
        lastCallOfLift = theCall.lastTimeCalled(elev._id)
        t= theCall._calls[lastCallOfLift]._endTime + elev.timeForTravel(elev._lastFloor,floor)
        if t<time:
            time=t
            ans=elev._id
    return ans

allocating(0,theBuilding._elevators[0]) # allocating elevator 0 to the first call

i=0
for c in theCall._calls: # iterating over every call except for the first call
    if i>0:
        prevCall=theCall._calls[i-1]
        lastAssignment=prevCall._assignment
        lastElev=theBuilding._elevators[lastAssignment]

        t=prevCall._endTime + lastElev.timeForTravel(lastElev._lastFloor, c._srcFloor) #calculating the time that the last used elevator will get to the source floor of the next call
        if  t <= c._time:
             allocating(i,lastElev) #if the elevator can get in time, we will assign it to the call

        else:
            newElev=theFastesetLiftToCome(c._srcFloor) #otherwise the call will get the elevator that will start the taking care of the call faster
            allocating(i,theBuilding._elevators[newElev])
        i=i+1
    else:
        i=i+1


theCall.exportCSv(sys.argv[3]) # exporting the calls to a new csv file




