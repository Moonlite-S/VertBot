import random
#Used to create a huge catalog of anime shows
#for the "animequiz" minigame in games.py
class anime:
    #   Properties of the anime class   #
    def __init__(self, name, desc, picture):
        self.name = name
        self.alias = []                 #Any alternative wordings of the anime
        self.picture = picture          #URL picture
        self.description = desc         #Description of the anime
        self.hints = []                 #Array String filled with hints
        self.picHints = []              #Array Strings of URLs to pictures

    #   Accessors   #
    def getName(self):
        return self.name
    def getPicture(self):
        return self.picture
    def getDescription(self):
        return self.description
    def getAnswers(self, answer):               #String of the answer in question
        return questions.get(answer)
    def getAliases(self):
        return self.alias
    def askHint(self):                          #Returns a hint at random; returns a String
        return random.choice(self.hints)
    def askPicHint(self):
        return random.choice(self.picHints)

    #   Mutators    #
    def setPicture(self, URL):
        self.picture = URL
    def setDescription(self, desc):
        self.description = desc
    def setHint(self, hnt):          #Adds a question to the array
        self.hints.append(hnt)
    def setAlias(self, lst):
        self.alias = lst
    def setPicHint(self, URL):
        self.picHints.append(URL)

#Anime List Catalog (There has to be an easier and more streamlined way of doing this, right?)
#   [coulda just made everyone one nested object list.... bruh]
#Current Anime Lists:
#Clannad, Jojo
animList = []

#Anime adding stuff
clannad = anime("Clannad", "A tragic supernatural high school story, involving themes of family and change.",
                "https://cdn.myanimelist.net/images/anime/1804/95033.jpg")
clannad.setHint("A delinquent student that finds himself solving various personal problems from his friends.")
clannad.setHint("His best friend is a blonde delinquent.")
clannad.setHint("Everyone's eyes are so fucking huge, holy shit.")
clannad.setPicHint("https://bit.ly/3n07vHy")
clannad.setPicHint("https://bit.ly/3n06L4R")
clannad.setHint("A show that continues past it's high school arc.")
clannad.setHint("It's pretty depressing.")
clannad.setHint("At some point, the main character is a robot.")
clannad.setHint("The name is based after an Irish Band of the same name.")
clannad.setHint("It has alternate OVAs where the main character hangs around certain side characters.")
clannad.setHint("It has this weird alternate dimensional plane that connects to the real world in some way.")
clannad.setAlias(["Clannad: After Story", "Clannad after story", "that one anime with the huge eyes"])
animList.append(clannad)

jojo = anime("Jojo", "An adventure story", "https://images-na.ssl-images-amazon.com/images/I/81wu-HcQorL._RI_.jpg")
jojo.setHint("It seperates itself into parts rather that seasons. (Which mean the same thing, but its a hint)")
jojo.setHint("A very cool and manly artstyle.")
jojo.setHint("A german robotic general.")
jojo.setHint("Three Big Burly Men.")
jojo.setHint("Part 2 was the best season.")
jojo.setHint("Vampires exist for a while, I guess.")
jojo.setPicHint("https://bit.ly/3svNg5B")
jojo.setPicHint("https://bit.ly/3mXo0UB")
jojo.setHint("One of the most useless characters becomes the of the most liked characters.")
jojo.setAlias(["Jojo's Bizzare Adventure", "Jojos Bizzare Adventure"])
animList.append(jojo)



#Coulda done it like this...
#catalog = {
#    "clannad": {
#        "description:" : "Fun anime",
#        "picture: " : url,
#        "hints: " : ["Fun death", "Happy death"]}
#    }