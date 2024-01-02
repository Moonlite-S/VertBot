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

limitedBanners = {"seele" : 
                        {"Name": "Butterfly on Swordtip",
                        "BannerUrl":"http://tinyurl.com/3c9bsmux",
                        "Icon":"https://tinyurl.com/5n87vzhc", 
                        "Focus":[("Natasha", fourStarHeroes["Natasha"]), ("Hook", fourStarHeroes["Hook"]), ("Pela", fourStarHeroes["Pela"])], 
                        "LightConeName":"In the Night",
                        "LightConeUrl":"https://tinyurl.com/56ht5yfm",
                        "LightConeThumbnailUrl":"http://tinyurl.com/34j77v8y",
                        "LightConeFocus":[("The Moles Welcome You", fourStarLightCones["The Moles Welcome You"]), "Good Night and Sleep Well", fourStarLightCones["Good Night and Sleep Well"], ("Post Op Conversation", fourStarLightCones["Post-Op Conversation"])]},

                  "jingyuan" : 
                        {"Name":"Swirl of Heavenly Spear",
                        "BannerUrl": "http://tinyurl.com/2zvpc925",
                        "Icon":"https://tinyurl.com/2h7sb9n5",
                        "Focus":[("Sushang", fourStarHeroes["Sushang"]), ("March 7th", fourStarHeroes["March 7th"]), ("Tingyun", fourStarHeroes["Tingyun"])],
                        "LightConeName":"Before Dawn",
                        "LightConeUrl":"https://tinyurl.com/3ckswmzp",
                        "LightConeThumbnailUrl":"http://tinyurl.com/muvrme6w",
                        "LightConeFocus":[("Planetary Rendezvous", fourStarLightCones["Planetary Rendezous"]), ("Only Silence Remains", fourStarLightCones["Only Silence Remains"]), ("Day One of My New Life", fourStarLightCones["Day One of My New Life"])]},


                   "silverwolf" : 
                        {"Name":"Contract Zero",
                        "BannerUrl": "http://tinyurl.com/2hk2n2hj",
                        "Icon":"https://tinyurl.com/38rffb7x",
                        "Focus":[("Dan Heng", fourStarHeroes["Dang Heng"]), ("Asta", fourStarHeroes["Asta"]), ("Serval", fourStarHeroes["Serval"])],
                        "LightConeName":"Incessant Rain",
                        "LightConeUrl":"https://tinyurl.com/2nhf9zdu",
                        "LightConeThumbnailUrl":"http://tinyurl.com/mrnktpua",
                        "LightConeFocus":[("Subscribe for More!", fourStarLightCones["Subscribe for More!"]), ("Memories of the Past", fourStarLightCones["Memories of the Past"]), ("Make the World Clamor", fourStarLightCones["Make the World Clamor"])]},

                    "loucha" : 
                        {"Name":"Laic Pursuit",
                        "BannerUrl": "http://tinyurl.com/2mj2njj3",
                        "Icon":"https://tinyurl.com/4hbjy5ee",
                        "Focus":[("Pela", fourStarHeroes["Pela"]), ("Qingque", fourStarHeroes["Qingque"]), ("Yukong", fourStarHeroes["Yukong"])],
                        "LightConeName":"Echoes of the Coffin",
                        "LightConeUrl":"https://tinyurl.com/44bnxmpr",
                        "LightConeThumbnailUrl":"http://tinyurl.com/5n862vsp",
                        "LightConeFocus":[("Good Night and Sleep Well", fourStarLightCones["Good Night and Sleep Well"]), ("Dance! Dance! Dance!", fourStarLightCones["Dance! Dance! Dance!"]), ("Geniuses' Repose", fourStarLightCones["Geniuses' Repose"])]},

                    "blade" : 
                        {"Name":"A Lost Soul",
                        "BannerUrl": "http://tinyurl.com/669nwzpd",
                        "Icon":"http://tinyurl.com/3w9bxje5",
                        "Focus":[("Arlan", fourStarHeroes["Arlan"]), ("Sushang", fourStarHeroes["Sushang"]), ("Natasha", fourStarHeroes["Natasha"])],
                        "LightConeName":"The Unreachable Side",
                        "LightConeUrl":"http://tinyurl.com/mh77a6j8",
                        "LightConeThumbnailUrl":"http://tinyurl.com/36wmv8dn",
                        "LightConeFocus":[("A Secret Vow", fourStarLightCones["A Secret Vow"]),("Shared Feeling", fourStarLightCones["Shared Feeling"]), ("Swordplay", fourStarLightCones["Swordplay"])]},

                    "kafka" : 
                        {"Name":"Nessun Dorma",
                        "BannerUrl": "http://tinyurl.com/5cuj8xhc",
                        "Icon":"http://tinyurl.com/4vj2mu4v",
                        "Focus":[("Luka", fourStarHeroes["Luka"]), ("Sampo", fourStarHeroes["Shampoo"]), ("Serval", fourStarHeroes["Serval"])],
                        "LightConeName":"Paitence is All You Need",
                        "LightConeUrl":"http://tinyurl.com/3enka4zw",
                        "LightConeThumbnailUrl":"http://tinyurl.com/52kdr2xa",
                        "LightConeFocus":[("Resolution Shines As Pearls of Sweat", fourStarLightCones["Resolution Shines As Pearls of Sweat"]), ("Eyes of the Prey", fourStarLightCones["Eyes of the Prey"]), ("The Birth of the Self", fourStarLightCones["The Birth of the Self"])]},
                    
                    "imbibitorlunae" : 
                        {"Name":"Epochal Spectrum",
                        "BannerUrl": "http://tinyurl.com/3m8x398r",
                        "Icon":"http://tinyurl.com/bde6vc33",
                        "Focus":[("Yukong", fourStarHeroes["Yukong"]), ("Asta", fourStarHeroes["Asta"]), ("March 7th", fourStarHeroes["March 7th"])],
                        "LightConeName":"Brighter than the Sun",
                        "LightConeUrl":"http://tinyurl.com/ywbtces7",
                        "LightConeThumbnailUrl":"http://tinyurl.com/3jswbayz",
                        "LightConeFocus":[("Dance! Dance! Dance!", fourStarLightCones["Dance! Dance! Dance!"]), ("Planetary Rendezvous", fourStarLightCones["Planetary Rendezous"]), ("Landau's Choice", fourStarLightCones["Landau's Choice"])]},

                    "fuxuan" : 
                        {"Name":"Forseen, Foreknown, Foretorld",
                        "BannerUrl": "http://tinyurl.com/4ajrt8xv",
                        "Icon":"http://tinyurl.com/5bucks62",
                        "Focus":[("Lynx", fourStarHeroes["Lynx"]), ("Hook", fourStarHeroes["Hook"]), ("Pela", fourStarHeroes["Pela"])],
                        "LightConeName":"She Already Shut Her Eyes",
                        "LightConeUrl":"http://tinyurl.com/4bmv8khc",
                        "LightConeThumbnailUrl":"http://tinyurl.com/bdz9ecwu",
                        "LightConeFocus":[("Perfect Timing", fourStarLightCones["Perfect Timing"]), ("Under the Blue Sky", fourStarLightCones["Under the Blue Sky"]), ("Trend of the Universal Market", fourStarLightCones["Trend of the Universal Market"])]},

                    "jingliu" : 
                        {"Name":"Gentle Eclipse of the Moon",
                        "BannerUrl": "http://tinyurl.com/ycxr6933",
                        "Icon":"http://tinyurl.com/7evvmsaa",
                        "Focus":[("Tingyun", fourStarHeroes["Tingyun"]), ("Qingque", fourStarHeroes["Qingque"]), ("Sampo", fourStarHeroes["Shampoo"])],
                        "LightConeName":"I Shall Be My Own Sword",
                        "LightConeUrl":"http://tinyurl.com/ycxfscpd",
                        "LightConeThumbnailUrl":"http://tinyurl.com/4n7577du",
                        "LightConeFocus":[("Memories of the Past", fourStarLightCones["Memories of the Past"]), ("Make the World Clamor", fourStarLightCones["Make the World Clamor"]),("Eyes of the Prey", fourStarLightCones["Eyes of the Prey"])]},

                    "topaz" : 
                        {"Name":"Sunset Clause",
                        "BannerUrl": "http://tinyurl.com/52985t7u",
                        "Icon":"http://tinyurl.com/2s3v8en6",
                        "Focus":[("Guinaifen", fourStarHeroes["Guinaifen"]), ("Luka", fourStarHeroes["Luka"]), ("Sushang", fourStarHeroes["Sushang"])],
                        "LightConeName":"Worrisome, Blissful",
                        "LightConeUrl":"http://tinyurl.com/y7ecrzuw",
                        "LightConeThumbnailUrl":"http://tinyurl.com/3yrb9fa9",
                        "LightConeFocus":[("The Moles Welcome You", fourStarLightCones["The Moles Welcome You"]), ("Resolution Shines as Pearls of Sweat", fourStarLightCones["Resolution Shines As Pearls of Sweat"]), ("Only Silence Remains", fourStarLightCones["Only Silence Remains"])]},

                    "huohuo" : 
                        {"Name":"Bloom in Gloom",
                        "BannerUrl": "http://tinyurl.com/mtusfsva",
                        "Icon":"http://tinyurl.com/y69psnfn",
                        "Focus":[("Dan Heng", fourStarHeroes["Dang Heng"]), ("Arlan", fourStarHeroes["Arlan"]), ("Serval", fourStarHeroes["Serval"])],
                        "LightConeName":"Night of Fright",
                        "LightConeUrl":"http://tinyurl.com/44ymh23j",
                        "LightConeThumbnailUrl":"http://tinyurl.com/2tzhr6x8",
                        "LightConeFocus":[("Shared Feeling", fourStarLightCones["Shared Feeling"]), ("Subscribe for More!", fourStarLightCones["Subscribe for More!"]), ("Trend of the Univseral Market", fourStarLightCones["Trend of the Universal Market"])]},
                    
                    "argenti" : 
                        {"Name":"Thorns of Scented Crown",
                        "BannerUrl": "http://tinyurl.com/ypxnn53x",
                        "Icon":"http://tinyurl.com/md432tzx",
                        "Focus":[("Hanya", fourStarHeroes["Hanya"]), ("Lynx", fourStarHeroes["Lynx"]), ("Asta", fourStarHeroes["Asta"])],
                        "LightConeName":"An Instant Before A Gaze",
                        "LightConeUrl":"http://tinyurl.com/mr9ve8pn",
                        "LightConeThumbnailUrl":"http://tinyurl.com/mwdnzf38",
                        "LightConeFocus":[("Post-Op Conversation", fourStarLightCones["Post-Op Conversation"]), ("Under the Blue Sky", fourStarLightCones["Under the Blue Sky"]), ("The Birth of the True Self", fourStarLightCones["The Birth of the Self"])]},
                   }
