using System;
using System.Collections.Generic;
using System.Text;

namespace Text_Game_CS
{
    internal class Monster : Character
    {
        public List<string> Abilities { get; private set; } = new List<string> { "Claw Swipe", "Roar", "Tail Whip" };  // Placeholder for Monster abilities, can be expanded with effects and mechanics later
        public Monster(string name) : base(name)
        {
            // Additional initialization for Monster-specific attributes can be added here
            this.HP = 200;
            this.Stamina = 150;
            this.Mana = 30;
            this.Defense = 80;
            this.Skill = 1.2;
            this.ExperienceToNextLevel = 200; // Adjusted for Monster leveling
        }
    }
}