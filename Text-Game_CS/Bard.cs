using System;
using System.Collections.Generic;
using System.Text;

namespace Text_Game_CS
{
    internal class Bard : Character
    {
        public List<string> Songs { get; private set; } = new List<string> { "Song of Valor", "Melody of Healing", "Ballad of Strength", "Harmony of Protection", "Lullaby of Sleep" };  // Placeholder for Bard songs, can be expanded with effects and mechanics later
        public Bard(string name) : base(name)
        {
            // Additional initialization for Bard-specific attributes can be added here
            this.HP = 110;
            this.Stamina = 90;
            this.Mana = 120;
            this.Defense = 60;
            this.Skill = 1.6;
            this.ExperienceToNextLevel = 110; // Adjusted for Bard leveling
        }
    }
}
