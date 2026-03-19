using System;
using System.Collections.Generic;
using System.Text;

namespace Text_Game_CS
{
    internal class Witcher : Character
    {
        public List<string> Signs { get; private set; } = new List<string> { "Aard", "Igni", "Yrden", "Quen", "Axii" };  // Placeholder for Witcher signs, can be expanded with effects and mechanics later
        public Witcher(string name) : base(name)
        {
            // Additional initialization for Witcher-specific attributes can be added here
            this.HP = 160;
            this.Stamina = 120;
            this.Mana = 60;
            this.Defense = 70;
            this.Skill = 1.5;
            this.ExperienceToNextLevel = 150; // Adjusted for Witcher leveling
            //this.ASCII = 
        }
    }
}
