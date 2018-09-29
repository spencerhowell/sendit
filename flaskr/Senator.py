import csv

class Senator:
    def __init__(self, name, state, contact_me, party, pic, facebook, twitter, bio, next_senator=None):
        self.name = name
        self.state = state
        self.contact_me = contact_me
        self.party = party
        self.pic = pic
        self.facebook = facebook
        self.twitter = twitter
        self.bio = bio
        self.next_senator = next_senator

class Senate:
    def __init__(self, size = 100, firstSenator = None):
        self.size = size
        self.firstSenator = firstSenator

    def moveToLastSenator(self):
        currentSenator = self.firstSenator
        while(currentSenator.next_senator != None):
            currentSenator = currentSenator.next_senator
        return currentSenator


    def addSenator(self, senator):
        if(self.firstSenator == None):
            self.firstSenator = senator
        else:
            lastSenator = self.moveToLastSenator()
            lastSenator.next_senator = senator

    def findSenators(self, state):
        foundSenators = 0
        currentSenator = self.firstSenator
        thisState = Senate(2)
        while ((currentSenator.next_senator != None) & (foundSenators < 2)):
            if(currentSenator.state == state):
                thisState.addSenator(currentSenator)
                foundSenators = foundSenators + 1
            currentSenator = currentSenator.next_senator
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
            currentSenator = currentSenator.next_senator
        return currentSenator

    def populateFromCSV(self):
        with open('./static/us-senate.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                state = row['state_name']
                contact_me = row['contact_page']
                party = row['party'].capitalize()
                pic = row['photo_url']
                facebook = row['facebook_url']
                twitter = row['twitter_url']
                bio = row['bioguide']
                senator1 = Senator(name, state, contact_me, party, pic, facebook, twitter, bio)
                self.addSenator(senator1)

#TEST CODE
#ourSenate = Senate(100, None)
#ourSenate.populateFromCSV()
#Georgia = ourSenate.findSenators("Georgia")
#print(Georgia.getSenatorNum(1).name)
#print(Georgia.getSenatorNum(2).name)
