class starRail:
    def __init__(self, client) :
        self.client = client

# Updated for 1.5 
#  Latest Characters: 
#  - Huohuo and Argenti (Limited 5* Heroes)
#  - Night of Fright and An Instant Before a Gaze (Limited 5* Light Cones)
#  - Hanya (4* Hero)
        
threeStarLightCones = {"Sagacity": "https://tinyurl.com/2p8a4zha", 
                       "Mediation":"https://tinyurl.com/mwryjmb4", 
                       "Hidden Shadow":"https://tinyurl.com/yc76n7b3", 
                       "Pioneering":"https://tinyurl.com/msfrekdh", 
                       "Mutual Demise":"https://tinyurl.com/4chmc7a3", 
                       "Multiplication":"https://tinyurl.com/4f2975wj", 
                       "Adversarial":"https://tinyurl.com/3y5yedt7", 
                       "Passkey":"https://tinyurl.com/syxxxscw", 
                       "Meshing Cogs":"https://tinyurl.com/yp45ehbe", 
                       "Loop":"https://tinyurl.com/54ekk8xb",
                       "Defense":"https://tinyurl.com/msef89r",
                       "Shattered Home":"https://tinyurl.com/5h8cmrm2", 
                       "Fine Fruit":"https://tinyurl.com/2p9vwhmp",
                       "Darting Arrow":"https://tinyurl.com/mwjp8jxk",
                       "Data Bank":"https://tinyurl.com/yckyj4aj", 
                       "Chorus":"https://tinyurl.com/mw64drrs", 
                       "Void":"https://tinyurl.com/45c9fawd",
                       "Amber":"https://tinyurl.com/4es6rpt9",
                       "Collapsing Sky":"https://tinyurl.com/mr3u729k",
                       "Cornucopia":"https://tinyurl.com/2mebeemb",
                       "Arrows":"https://tinyurl.com/4h6txkm4"}

fourStarLightCones = {"Under the Blue Sky": "https://tinyurl.com/ycx8dbnr",
                       "Geniuses' Repose": "https://tinyurl.com/542ejv3u", 
                       "Dance! Dance! Dance!": "https://tinyurl.com/2avf8keu", 
                       "Subscribe for More!":"https://tinyurl.com/5a38se2s", 
                       "Trend of the Universal Market": "https://tinyurl.com/yezvuamb", 
                       "Resolution Shines As Pearls of Sweat": "https://tinyurl.com/34rx2se9", 
                       "Perfect Timing": "https://tinyurl.com/497838wa", 
                       "Make the World Clamor":"https://tinyurl.com/st93dtzm", 
                       "A Secret Vow":"https://tinyurl.com/3ue7b36w", 
                       "Planetary Rendezous":"https://tinyurl.com/yamxdfmm", 
                       "Swordplay": "https://tinyurl.com/mptfspwt", 
                       "Landau's Choice": "https://tinyurl.com/rk8hdcwc", 
                       "Eyes of the Prey": "https://tinyurl.com/4s8rmeyu", 
                       "Shared Feeling": "https://tinyurl.com/5xhtzd8t", 
                       "The Birth of the Self": "https://tinyurl.com/ysep9zwx", 
                       "The Moles Welcome You": "https://tinyurl.com/2p8kw5pm", 
                       "Memories of the Past":"https://tinyurl.com/4sfpy77s", 
                       "Only Silence Remains": "https://tinyurl.com/434x6wmf", 
                       "Day One of My New Life": "https://tinyurl.com/3yaj6uyb", 
                       "Good Night and Sleep Well":"https://tinyurl.com/3dajc5vz", 
                       "Post-Op Conversation": "https://tinyurl.com/mwmxe29n"}

fourStarHeroes = {"Serval":"https://tinyurl.com/mw3vkz6r", 
                  "Arlan": "https://tinyurl.com/4pxrxf8a", 
                  "Asta": "https://tinyurl.com/yckpt2cy", 
                  "Shampoo": "https://tinyurl.com/33s8c2jc", 
                  "Yukong": "https://tinyurl.com/2jvts454", 
                  "Sushang": "https://tinyurl.com/ybae7y7b", 
                  "Tingyun": "https://tinyurl.com/4rksvxmb", 
                  "Qingque": "https://tinyurl.com/3jnra4fw", 
                  "Hook": "https://tinyurl.com/2p9xhy2u", 
                  "Pela": "https://tinyurl.com/mfxz5yse", 
                  "Natasha": "https://tinyurl.com/yc7x4m9f", 
                  "Herta": "https://tinyurl.com/3vafwcfw", 
                  "Dang Heng": "https://tinyurl.com/4tn8fs8d", 
                  "March 7th": "https://tinyurl.com/4bvhme2k", 
                  "Luka": "http://tinyurl.com/5e5k7xhz", 
                  "Lynx": "http://tinyurl.com/5n6jk5re", 
                  "Guinaifen": "http://tinyurl.com/54mpab9m", 
                  "Hanya": "http://tinyurl.com/mvy3xv6k"}

fiveStarHeroes  = {"Bailu": "https://tinyurl.com/ymwuawpt", 
                   "Yanqing":"https://tinyurl.com/5n72trtf", 
                   "Clara":"https://tinyurl.com/yc82uyfx",
                   "Gepard":"https://tinyurl.com/3vy9mmab",
                   "Bronya":"https://tinyurl.com/p8r4a6x7",
                   "Welt":"https://tinyurl.com/r7kvhjaz",
                   "Himeko":"https://tinyurl.com/2p84k9f6"}

fiveStarLightCones = {"Time Waits for No One":"https://tinyurl.com/s9vu2zts", 
                      "Moment of Victory":"https://tinyurl.com/4ewpp8c3",
                      "In the Name of the World":"https://tinyurl.com/bdhp4m24", 
                      "But the Battle Isn't Over":"https://tinyurl.com/w37w2vs8",
                      "Something Irreplaceable":"https://tinyurl.com/5ad8srte",
                      "Night on the Milky Way":"https://tinyurl.com/4xnamfep", 
                      "Sleep Like the Dead": "https://tinyurl.com/ad4t3pvm"}

limitedFiveStarHeroes = {"Seele":"https://tinyurl.com/5n87vzhc", 
                         "Jing Yuan":"https://tinyurl.com/2h7sb9n5",
                         "Silver Wolf":"https://tinyurl.com/38rffb7x",
                         "Loucha":"https://tinyurl.com/4hbjy5ee", 
                         "Blade": "http://tinyurl.com/3w9bxje5", 
                         "Kafka": "http://tinyurl.com/4vj2mu4v", 
                         "Imbibitor Lunae": "http://tinyurl.com/bde6vc33", 
                         "Fu Xuan": "http://tinyurl.com/5bucks62", 
                         "Topaz and Numby":"http://tinyurl.com/2s3v8en6", 
                         "Jingliu": "http://tinyurl.com/7evvmsaa", 
                         "Huohuo": "http://tinyurl.com/y69psnfn", 
                         "Argenti": "http://tinyurl.com/md432tzx"}

limitedFiveStarLightCones = {"In the Night":"https://tinyurl.com/56ht5yfm", 
                             "Before Dawn":"https://tinyurl.com/3ckswmzp",
                             "Incessant Rain":"https://tinyurl.com/2nhf9zdu", 
                             "Echoes of the Coffin":"https://tinyurl.com/44bnxmpr", 
                             "The Unreachable Side":"http://tinyurl.com/mh77a6j8", 
                             "Paitence is All You Need":"http://tinyurl.com/3enka4zw", 
                             "Brighter than the Sun":"http://tinyurl.com/ywbtces7", 
                             "She Already Shut Her Eyes":"http://tinyurl.com/4bmv8khc", 
                             "Worrisome, Blissful":"http://tinyurl.com/y7ecrzuw", 
                             "I Shall Be My Own Sword":"http://tinyurl.com/ycxfscpd", 
                             "Night of Fright":"http://tinyurl.com/44ymh23j", 
                             "An Instant Before A Gaze": "http://tinyurl.com/mr9ve8pn"}

# Place to store the banner pictures
limitedBannerThumbnails = {}