using System;
using System.Collections.Generic;
using System.Text;

namespace Text_Game_CS
{
    internal class Dwarf : Character
    {
        public Dwarf(string name) : base(name)
        {
            this.HP = 160;
            this.Stamina = 120;
            this.Mana = 20;
            this.Defense = 60;
            this.Skill = 25;
        }
    }
}