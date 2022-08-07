import time


class Elevator:

    def __init__(self, id, speed=5, minFloor=5, maxFloor=11, closeTime=5, openTime=5, startTime=5, stopTime=5, lastFloor=0) ->None:
        self._id=id
        self._speed=speed
        self._minFloor=minFloor
        self._maxFloor=maxFloor
        self._closeTime=closeTime
        self._openTime=openTime
        self._startTime=startTime
        self._stopTime=stopTime
        self._lastFloor=lastFloor

    def __str__(self) -> str:
        return str(self.__dict__)

    def timeForTravel(self, srcFloor, destFloor):
        if srcFloor ==destFloor: return 0
        dist=abs(srcFloor-destFloor)
        x = dist/self._speed
        return self._closeTime +self._startTime +x+ self._stopTime + self._openTime






