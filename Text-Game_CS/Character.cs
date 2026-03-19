using System;
using System.Collections.Generic;
using System.Text;

namespace Text_Game_CS
{
    internal class Character
    {
        public string Name { get; private set; } = "Unknown";
        public bool IsAlive { get; private set; } = true;
        public int HP { get; protected set; }
        public int Stamina { get; protected set; }
        public int Mana { get; protected set; }
        public int Defense { get; protected set; }
        public double Skill { get; protected set; } // AttackMultiplier
        public int Respect { get; protected set; }
        public int Level { get; protected set; } = 1;                                // new idea of leveling system
        public int Experience { get; protected set; } = 0;                           // new idea of leveling system
        public int ExperienceToNextLevel { get; protected set; } = 100;              // new idea of leveling system
        public Dictionary<string, EffectStatus> Effects { get; protected set; }
        public Dictionary<string, EquipStatus> Equip { get; protected set; }
        //public string deathASCII { get; private set; } = $"    ___o .--.\r\n   /___| |OO|\r\n  /'   |_|  |_\r\n       (_    _)\r\n       | |   \\\r\n       | |oo_/sjw\r\n";

        string[] titles = new string[]
        {
            "Great King",
            "the Imperishable",
            "Khemrikhara",
            "The Great King of Nehekhara",
            "King of Kings",
            "Opener of the Way",
            "Wielder of the Divine Flame",
            "Punisher of Nomads",
            "The Great Unifier",
            "Commander of the Golden Legion",
            "Sacred of Appearance",
            "Bringer of Light",
            "Father of Hawks",
            "Builder of Cities",
            "Protector of the Two Worlds",
            "Keeper of the Hours",
            "Chosen of Ptra",
            "High Steward of the Horizon",
            "Sailor of the Great Vitae",
            "Sentinel of the Two Realms",
            "The Undisputed",
            "Begetter of the Begat",
            "Scourge of the Faithless",
            "Carrion-feeder",
            "First of the Charnel Valley",
            "Rider of the Sacred Chariot",
            "Vanquisher of Vermin",
            "Champion of the Death Arena",
            "Mighty Lion of the Infinite Desert",
            "Emperor of the Shifting Sands",
            "He Who Holds The Sceptre",
            "Great Hawk Of The Heavens",
            "Arch-Sultan of Atalan",
            "Waker of the Hierotitan",
            "Monarch of the Sky",
            "Majestic Emperor of the Shifting Sands",
            "Champion of the Desert Gods",
            "Breaker of the Ogre Clans",
            "Builder of the Great Pyramid",
            "Terror of the Living",
            "Master of the Never-Ending Horizon",
            "Master of the Necropolises",
            "Taker of Souls",
            "Tyrant to the Foolish",
            "Bearer of Ptra's Holy Blade",
            "Scion of Usirian",
            "Scion of Nehek",
            "The Great",
            "Chaser of Nightmares",
            "Keeper of the Royal Herat",
            "Founder of the Mortuary Cult",
            "Banisher of the Grand Hierophant",
            "High Lord Admiral of the Deathfleets",
            "Guardian of the Charnal Pass",
            "Tamer of the Liche King",
            "Unliving Jackal Lord",
            "Dismisser of the Warrior Queen",
            "Charioteer of the Gods",
            "He Who Does Not Serve",
            "Slayer of Reddittras",
            "Scarab Purger",
            "Favoured of Usirian",
            "Player of the Great Game",
            "Liberator of Life",
            "Lord Sand",
            "Wrangler of Scorpions",
            "Emperor of the Dunes",
            "Eternal Sovereign of Khemri's Legions",
            "Seneschal of the Great Sandy Desert",
            "Curserer of the Living",
            "Regent of the Eastern Mountains",
            "Warden of the Eternal Necropolis",
            "Herald of all Heralds",
            "Caller of the Bitter Wind",
            "God-Tamer",
            "Master of the Mortis River",
            "Guardian of the Dead",
            "Great Keeper of the Obelisks",
            "Deacon of the Ash River",
            "Belated of Wakers",
            "General of the Mighty Frame",
            "Summoner of Sandstorms",
            "Master of all Necrotects",
            "Prince of Dust",
            "Tyrant of Araby",
            "Purger of the Greenskin Breathers",
            "Killer of the False God's Champions",
            "Tyrant of the Gold Dunes",
            "Golden Bone Lord",
            "Avenger of the Dead",
            "Carrion Master",
            "Eternal Warden of Nehek's Lands",
            "Breaker of Djaf's Bonds"
        };


        string[] enemyNames = new string[]
        {
            "Eredin",
            "Imlerith",
            "Caranthir",
            "Avallac'h",
            "Emhyr",
            "Vilgefortz",
            "Bonhart",
            "Rience",
            "Dettlaff",
            "Gaunter",
            "Azar",
            "Letho",
            "Jacques",
            "Radovid",
            "Cahir",
            "Stefan",
            "Fringilla",
            "Sigismund",
            "Reynard",
            "Tissaia",
            "Settra"
        };

        string[] classes = new string[]
        {
            "Witcher",
            "Sorcerer",
            "Archer",
            "Jarl",
            "Bard",
            "Monster",
            "Dwarf"
        };


        public static void Death()
        {
            Console.WriteLine($"    ___o .--.\r\n   /___| |OO|\r\n  /'   |_|  |_\r\n       (_    _)\r\n       | |   \\\r\n       | |   /   \r\n");
            Console.WriteLine("You have died. Game over.");
        }

        public sealed class EffectStatus
        {
            public bool Is { get; set; }
            public int Duration { get; set; }

            public EffectStatus(bool isActive = false, int duration = 0)
            {
                Is = isActive;
                Duration = duration;
            }
        }

        public sealed class EquipStatus
        {
            public bool Own { get; set; }
            public int Dmg { get; set; }
            public string Effect { get; set; }
            public EquipStatus(int dmg = 0, bool own = false, string effect = "none")
            {
                Own = own;
                Effect = effect;
                Dmg = dmg;
            }
        }

        //            //# AI Ideas
        //            //# "white honey": {"own": 1, "amount": 0, "duration": 0},  # cleanses all effects
        //            //# "thunderbolt": {"own": 1, "amount": 0.25, "duration": 4},  # skill multiplier
        //            //# "cat": {"own": 1, "amount": 0.15, "duration": 4},  # defense multiplier
        //            //# "swallow": {"own": 1, "amount": 0.25, "duration": 4},  # healing multiplier
        //            //# "white gull": {"own": 1, "amount": 0.25, "duration": 4},  # mana multiplier
        //            //# "black blood": {"own": 1, "amount": 0.25, "duration": 4},  # defense against monsters
        //                "healing potion": { "own": 3,"amount": 50},
        //                        "stamina potion": { "own": 3,"amount": 45},
        //                        "mana potion": { "own": 3,"amount": 35}, 
        //                        "vlaštovka": { "own": 1,"amount": 25, "duration" : 4}, //# duration healing
        //                        "hrom": { "own": 2,"amount": 1.5}, # dmg multiplier
        //                        "vlk": { "own": 2,"amount": 0.15}, # sklill multiplier
        //                        "medvěd": { "own": 2,"amount": 0.25}, //# defense multiplier
        //                        "blizzard": { "own": 1,"amount": 20, "duration" : 4}, //# stamina regen
        //                        }

        //            self.equip = {
        //            //# "iron claws": {"own":False,"dmg_mutipl": 0.25},  # [owned, dmg multiplier]
        //            //# "elven lute": {"own":False,"dmg_mutipl": 0.25},  
        //            //# "siderite sword": {"own":False,"dmg_mutipl": 0.25},
        //            //# "skellige axe": {"own":False,"dmg_mutipl": 0.25},
        //            //# "brokilon bow": {"own":False,"dmg_mutipl": 0.25},
        //            //# "dimeritium staff": {"own":False,"dmg_mutipl": 0.25},
        //            //# "mahakam hammer" : {"own":False,"dmg_multiplier": 0.35}
        //                "bomb": { "own":True,"dmg": 60, "effect": None},  //# [owned, base dmg]
        //                        "poison bomb": { "own":True,"dmg": 50, "effect": "poisoned"},  //# [owned, base dmg, effect]
        //                        "fire bomb": { "own":True,"dmg": 50, "effect": "burning"},  
        //                        "frost bomb": { "own":True,"dmg": 50, "effect": "frozen"}, 
        //                        }

        public Character(string name)
        {
            if (string.IsNullOrWhiteSpace(name))
            {
                throw new ArgumentException("Parameter must not be null, empty or whitespace.");
            }
            // this.IsAlive = true;
            this.Name = name;
            this.HP = 100;
            this.Stamina = 100;
            this.Mana = 0;
            this.Defense = 50;
            this.Skill = 1.0;
            this.Respect = 15;  // starting respect  15 == standart ; 0 == absolute neutral ; 50 == respected ; 100 == legendary ; -50 == hated ; -100 ==  きっしょー
            this.Level = 1;
            this.Experience = 0;
            this.ExperienceToNextLevel = 100;
            this.Effects = new Dictionary<string, EffectStatus>(StringComparer.OrdinalIgnoreCase)
            {
                ["burning"] = new EffectStatus(false, 0),
                ["poisoned"] = new EffectStatus(false, 0),
                ["stunned"] = new EffectStatus(false, 0),
                ["frozen"] = new EffectStatus(false, 0),
                ["bleeding"] = new EffectStatus(false, 0),
                ["healing"] = new EffectStatus(false, 0),
                ["stamina regen"] = new EffectStatus(false, 0),
                ["shielding"] = new EffectStatus(false, 0),
                ["cleanse"] = new EffectStatus(false, 0)
            };
            this.Equip = new Dictionary<string, EquipStatus>(StringComparer.OrdinalIgnoreCase)
            {
                ["bomb"] = new EquipStatus(60, true),
                ["poison bomb"] = new EquipStatus(50, true, "poisoned"),
                ["fire bomb"] = new EquipStatus(50, true, "burning"),
                ["frost bomb"] = new EquipStatus(50, true, "frozen")
            };
        }
    }
}
