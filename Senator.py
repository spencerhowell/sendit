class Senator:
    def __init__(self, name, state, email):
        self.name = name
        self.state = state
        self.email = email


s1 = Senator("Corker")
print(s1.name)

class Node:
    def __init__(self, senator=None, next_senator=None):
        self.senator = senator
        self.next_senator = next_senator

    def getSenator(self):
        return self.senator

    def getNext(self):
        return self.next_senator

    def setNext(self, next):
        self.next_senator = next

class Senate:
    def __init__(self, size = 100, firstSenator = None):
        self.size = size
        self.firstSenator = firstSenator

    def moveToLastSenator(self):
        currentSenator = self.firstSenator
        while(currentSenator != None):
            currentSenator = currentSenator.getNext
        return currentSenator


    def addSenator(self, senator):
        if(self.firstSenator == None):
            self.firstSenator = senator
        else:
            lastSenator = self.moveToLastSenator()
            lastSenator.setNext(senator)


    def findSentaors(self, state):
        foundSenators = 0
        currentSenator = self.firstSenator
        thisState = Senate(2)
        while (currentSenator.next_Senator != None & foundSenators < 2 ):
            if(currentSenator.state == state):
                thisState.addSenator(currentSenator)
        return thisState

    def getSenatorName(self, senatorName):
        currentSenator = self.firstSenator
        while (currentSenator.next_Senator != None):
            if(currentSenator.name == senatorName):
                return currentSenator
        nullSenator = Senator("null", "null", "null")
        return nullSenator

    def getSenatorNum(self, senatorNum):
        currentSenator = self.firstSenator
        for x in range(1, senatorNum):
            currentSenator = currentSenator.getNext
        return currentSenator