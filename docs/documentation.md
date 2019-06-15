## documention

This folder will include any document developed for this project.


## test.py
This is a simple test segment of code that will import 2 characters from characters.py, and a ranged weapons from weapons.py, and run a series of test operations that can include:
1- Picking up a ranged weapon
2- conducting a ranged attack at the second character
3- conducting a melee attack.

And then generate a short story snippet based on those actions.
If character 1 is unable to pick up the ranged weapon, they are struck by an attack by the second character.
If the character is able to pick up the weapon, they will attempt to shoot the second character.
If the shooting attack is unsuccessful, they will conduct a melee attack against the second character.
If the melee attack fails, the simulation ends with a chidding by the first characters' commanding officer.

Following the conclusion of this test, the program will print out character sheets for both characters.
## race.py

This file contains the attributes and methods for the race class. 

### self.name = name
name of the race

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
an integer that is the result of the genFatePoints method.
### self.statCorruption = 0
an integer that represents the characters corruption
### self.statInsanity = 0
and integer that represents the characters insanity
### self.statPsy = 0
an integer that represents the characters psy rating.

### genFatePoints
a private method that selects the number of fate points that a character starts with. A character can have 3, 4, or 5 fate points, with 5 being the least common. 

### characterSheet
The character sheet is private method that will generate a sheet displaying all of the stats and materials of a character.
Because most of the basic stats are simple 2 digit integers, it's just a matter of adding sufficient spaces so the value lines up under the header for that stat. 

Because the insanity, corruption and Psy rating can change during action, and thus will go from a single digit integer to a 2 digit one, there are checks for determining the length of the stat and thus how many spaces to add to the value.

## Skill
The class for skill objects.

### SkillSheet
Generates a skill sheet for a skill object that includes the name of the skill, any pre-requisits for the skill, a description of the skill, the benefits of the skill, and training level of the skill.