#Used to create a huge catalog of anime shows
#for the "animequiz" minigame in games.py
class anime:
    def __init__(self, client) :
        self.client = client

    ############################
    ## The Anime List Library ##
    ############################

animList = {
    "jojo" : {
        "name" : ["Jojo's Bizzare Adventure", "Jojo", "jojos bizzare adventure", "JoJo no Kimyou na Bouken"],
        "desc" : "An adventure story that involves vampires and big burly men.",
        "picBanner" : "https://images-na.ssl-images-amazon.com/images/I/81wu-HcQorL._RI_.jpg",
        "hint" : ["It seperates itself into parts rather that seasons. (Which mean the same thing, but its a hint)", "A very cool and manly artstyle.", 
                    "A german robotic general.", "Three Big Burly Men.", "Part 2 was the best season."],
        "picHint" : ["https://bit.ly/3svNg5B","https://bit.ly/3mXo0UB"]
    },
    "clannad" : {
        "name" : ["Clannad", "Clannad After Story", "Clannad: After Story"],
        "desc" : "A tragic supernatural high school story, involving themes of family and change.",
        "picBanner" : "https://cdn.myanimelist.net/images/anime/1804/95033.jpg",
        "hint" : ["A delinquent student that finds himself solving various personal problems from his friends.",
                "His best friend is a blonde delinquent.", "At some point, the main character is a robot.", 
                "A show that continues past it's high school arc.", "The name is based after an Irish Band of the same name."],
        "picHint" : ["https://bit.ly/3n07vHy", "https://bit.ly/3n06L4R"]
    },
    "demon slayer" : {
        "name" : ["Demon Slayer", "Kimetsu no Yaiba"],
        "descHint" : "A boy's family is destroyed by demons and his sister has turned into one.",
        "picBanner" : "https://cdn.myanimelist.net/images/anime/1286/99889.jpg",
        "hint" : ["The main character has a unique scar on his head.", "The animation studio that created this anime is ufotable.", "One of the characters has a boar helmet."],
        "picHint" : ["https://bit.ly/3P9BOaY", "https://bit.ly/3P8AVzC", "https://bit.ly/3SDxqny"]
    },
    "love is war" : {
        "name" : ["Kaguya-Sama: Love is War", "Love is War", "Kaguya-Sama", "Kaguyasama", "Kaguya-sama wa Kokurasetai", "Kaguya-sama wa Kokurasetai: Ultra Romantic", "Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen"],
        "desc" : "A love comedy revolving a certain student council cast.",
        "picBanner" : "https://bit.ly/3JIMg8h",
        "hint" : ["It's a popular romantic comedy set in school.", "One the characters is known for dancing to a certain song.", "A-1 pictures is the studio behind it."],
        "picHint" : ["https://bit.ly/3A8qlnK", "https://bit.ly/3Qs436t", "https://bit.ly/3PeWMFo"]
    },
    "violet evergarden" : {
        "name" : ["Violet Evergarden", "Evergarden"],
        "desc" : "A show that features a wandering girl searching what it means to have emotion.",
        "picBanner" : "https://bit.ly/3dhSO1J",
        "hint" : ["The girl is a doll.", "She writes letters to people.", "She has mechanical arms.", "She was raised as a killing machine.", "The studio behind this was Kyoto Animation"],        
        "picHint" : ["https://bit.ly/3BPmNYY", "https://bit.ly/3SBhAda", "https://bit.ly/3zIUn01"],
    },
    "bleach" : {
        "name" : ["Bleach"],
        "desc" : "A high schooler that fights demons.",
        "picBanner" : "https://bit.ly/3dlhAO8",
        "hint" : ["The main character has orange hair.", "The show has around 360 episodes.", "The main character can tranform into many forms."],
        "picHint" : ["https://bit.ly/3BY4cdr", "https://bit.ly/3QhjyOj", "https://bit.ly/3QdrXSY"]        
    },
    "death note" : {
        "name" : ["Death Note", "DN"],
        "desc" : "An anime where one guy goes on a vigilante spree while trying to cover his tracks.",
        "picBanner" : "https://bit.ly/3STLrxR",
        "hint" : ["Has a sort of cat and mouse relationship with one of the main antagonists.", "The main character has edgy hair.", "The main characters main weapon is a book."],
        "picHint" : ["https://bit.ly/3JLaAX6", "https://bit.ly/3zP7OLP", "https://bit.ly/3p7xFKj"]
    },
    "future diary" : {
        "name" : ["The Future Diary", "Future Diary", "The Future Diaries", "Future Diaries", "Mirai Nikki"],
        "desc" : "A survival game involving two high school students and one victory royale.",
        "picBanner" : "https://bit.ly/3djqlZd",
        "hint" : ["The main chick is fucking cray cray.", "One of the supporting characters is gay for the main character.", "The main tool for every participant for survival is an everyday item."],
        "picHint" : ["https://bit.ly/3JJlQ6m", "https://bit.ly/3JNMs64", "https://bit.ly/3QxE3Gf"]   
    },
    "deadman wonderland" : {
        "name" : ["Deadman Wonderland"],
        "desc" : "A kid is falsely accused of mass murdering his entire classroom and has to survive the world's most comically horrific prison.",
        "picBanner" : "https://bit.ly/3bJcFGG",
        "hint" : ["The powers the main character uses invovles using his blood.", "It has a lot of blood.", "The main chick really likes the color white."],
        "picHint" : ["https://bit.ly/3Ae4f3x", "https://bit.ly/3zN0X5H", "https://bit.ly/3SEAekp"]        
    },
    "arknights": {
        "name" : ["Arknights", "AK", "Arknights: Prelude to Dawn"],
        "desc" : "A dystopian world where magic cancer has taken over the world.",
        "picBanner" : "http://bit.ly/3JWnTFF",
        "hint" : ["The general populace hate people with magic cancer.", "The main character is a rabbit.", "Activate Melantha skill now."],
        "picHint" : ["https://bit.ly/3PWOmXk", "https://bit.ly/3Q1ko4F", "https://bit.ly/44DNNpo"]
    },
    "fate stay night UBW": {
        "name" : ["Fate Stay Night", "Fate Stay Night: Unlimited Blade Works", "FST UBW"],
        "desc" : "Battle royale between mages using fabled warriors of the past.",
        "picBanner" : "https://imdb.to/46OMjun",
        "hint" : ["Astolfo.", "An anime created in 2014.", "Has three different anime with three different routes for each of them"],
        "picHint" : ["https://bit.ly/3PZaBMf","https://bit.ly/3PW2b8C", "https://bit.ly/3JZ2209"]
    },
    "konosuba": {
        "name" : ["Kono Subarashii Sekai ni Shukufuku wo", "KonoSuba"],
        "desc" : "An anime about a band of adventurers in a world.",
        "picBanner" : "http://tinyurl.com/jsxakxyd",
        "hint" : ["A boy gets transported to a fantasy world with useless companions.", "Main characters have unique and quirky personalities while going on quests.", "The protagonist's party is known for causing chaos wherever they go."],
        "picHint" : ["http://tinyurl.com/yc7krndu", "http://tinyurl.com/2f3fvuwd", "http://tinyurl.com/3cs99js4"]
    },
    "hyperdimension neptunia": {
        "name" : ["Choujigen Game Neptune The Animation", "Hyperdimension Neptunia", "Neptunia"],
        "desc" : "Console wars but in real life.",
        "picBanner" : "http://tinyurl.com/368tfyt9",
        "hint" : ["A world where video game consoles take human form and fight each other.", "Features goddesses battling in a war that mirrors the console wars.", "Characters represent different gaming consoles and companies in a fantasy setting."],
        "picHint" : ["http://tinyurl.com/49steas8", "http://tinyurl.com/ycxk26t3", "http://tinyurl.com/5cx5v24x"]
    },
    "one piece": {
        "name" : ["One Piece", "OP"],
        "desc" : "An anime about this one pirate in particular.",
        "picBanner" : "http://tinyurl.com/52wewa5p",
        "hint" : ["Follows a rubber man and his friends searching for a legendary treasure.", "Set in a vast world of islands and seas, pirates seek the greatest treasure.", "The journey includes facing powerful enemies and uncovering hidden truths of the world."],
        "picHint" : ["http://tinyurl.com/ysbs63m5","http://tinyurl.com/3smn93rs","http://tinyurl.com/mr3xk4b7"]
    },
    "attack on titan": {
        "name" : ["Attack on Titan", "Shingeki no Kyojin", "AoT", "SnK"],
        "desc" : "big monsters attack the capital.",
        "picBanner" : "http://tinyurl.com/49dvvm8s",
        "hint" : ["Humans fight against giant humanoid creatures for survival.", "The story features a military dedicated to protecting humanity from external threats.", "Characters uncover the truth about the world and the origins of the Titans."],
        "picHint" : ["http://tinyurl.com/mnswypnb","http://tinyurl.com/3anx9rrs","http://tinyurl.com/4dbcbxtt"]
    },
    "love live": {
        "name" : ["Love Live! School Idol Project", "Love Live", "Love Live Sunshine", "LL"],
        "desc" : "An anime where a group of girls save their school with the power of singing.",
        "picBanner" : "http://tinyurl.com/4pb63tv7",
        "hint" : ["High school girls become idols to save their school.", "All men have been eradicated from existence.", "There's an incredibly iconic character here."],
        "picHint" : ["http://tinyurl.com/5eb5btt2","http://tinyurl.com/4fd5vpje","http://tinyurl.com/muf8v4t9"]
    },
    "gurren lagann": {
        "name" : ["Tengen Toppa Gurren Lagann", "Gurren Lagann", "TTGL"],
        "desc" : "An anime about some underground dweebs fighting for freedom.",
        "picBanner" : "http://tinyurl.com/582sv2k3",
        "hint" : ["Humans fight for freedom using robots powered by sheer willpower.", "The story escalates from underground villages to battles in space.", "Characters grow from humble beginnings to legendary heroes."],
        "picHint" : ["http://tinyurl.com/3y8b8t7t","http://tinyurl.com/2s4k7nku","http://tinyurl.com/36jsvsdh"]
    },
    "solo leveling": {
        "name" : ["Solo Leveling", "Na Honjaman Level-Up", "I Level Up Alone"],
        "desc" : "some web novel about some guy wanting to be stronger.",
        "picBanner" : "http://tinyurl.com/5n729943",
        "hint" : ["A low-ranked hunter becomes the most powerful through a unique system.", "Set in a world where hunters enter dungeons to fight monsters.", "The protagonist discovers a secret power that allows him to grow stronger."],
        "picHint" : ["http://tinyurl.com/sfrzxvwp","http://tinyurl.com/bvx3tpz8","http://tinyurl.com/3bs4p4he"]
    } 
}

"""
List Template:
"anime name": {
        "name" : [],
        "desc" : "",
        "picBanner" : "",
        "hint" : [],
        "picHint" : []
    }
"""