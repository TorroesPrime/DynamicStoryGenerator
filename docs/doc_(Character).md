## Character.py

This file contains the attributes and methods for the character super class. 

### self.name = name
a string that is the name of the character
### self.statWeaponSkill = weap
an integer that represents the characters Weapon Skill
### self.statBallisticSkill = ball
an integer that represents the characters ballistic skill
### self.statStrength = stre
an integer that represents the characters strength 
### self.statToughess = toug
an integer that represents the characters toughness
### self.statAgility = agil
an integer that represents the characters agility
### self.statIntelligence = inte
an integer that represents the characters intelligence
### self.statPerception = perc
an integer that represents the characters perception
### self.statWillPower = will
an integer that represents the characters will power
### self.statFellowship = fell
an integer that represents the characters fellowship
### self.statFate = self.__genFatePoints__()
an integer that is the result of the __genFatePoints__ method.
### self.statCorruption = 0
an integer that represents the characters corruption
### self.statInsanity = 0
and integer that represents the characters insanity
### self.statPsy = 0
an integer that represents the characters psy rating.

### __genFatePoints__
a private method that selects the number of fate points that a character starts with. A character can have 3, 4, or 5 fate points, with 5 being the least common. 

### __characterSheet__
The character sheet is private method that will generate a sheet displaying all of the stats and materials of a character.
Because most of the basic stats are simple 2 digit integers, it's just a matter of adding sufficient spaces so the value lines up under the header for that stat. 

Because the insanity, corruption and Psy rating can change during action, and thus will go from a single digit integer to a 2 digit one, there are checks for determining the length of the stat and thus how many spaces to add to the value.