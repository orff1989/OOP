import json
from Elevator import Elevator
import csv

class Building:

    def __init__(self, minFloor=0, maxFloor=10, elevators=[]) ->None:
        self._minFloor=minFloor
        self._maxFloor=maxFloor
        self._elevators=elevators

    def __str__(self) ->str:
        return str(self.__dict__)


    def loadJson(self, file):
        try:
            with open(file, "r+") as f:
                dicBuilding=json.load(f)
                self._minFloor=dicBuilding['_minFloor']
                self._maxFloor=dicBuilding['_maxFloor']
                theElevators=dicBuilding["_elevators"]
                for i in theElevators:
                    elev= Elevator(id=i["_id"],speed=i["_speed"], minFloor=i["_minFloor"],maxFloor=i["_maxFloor"], closeTime=i["_closeTime"],openTime=i["_openTime"], startTime=i["_startTime"], stopTime=i["_stopTime"])
                    self._elevators.append(elev)
        except IOError as e:
           print(e)

    @property
    def elevators(self):
        return self._elevators

