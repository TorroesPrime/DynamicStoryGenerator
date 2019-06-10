import textwrap
from character import *
from race import *
from skill import *
RaceHuman = Race('Human')
Character_01 = Character("Bob",10,10,10,10,10,10,10,10,10,RaceHuman)
Skill_01 = Skill("Skill Name", "No pre-req","""All Forbidden Lore Skills represent knowledge forbidden or hidden to the average 
citizen of the Imperium of Man. In many cases, it is a heinous crime to even possess such 
knowledge. Though a Heretic in BLACK CRUSADE has nothing but contempt for the Imperium’s
restrictions, such knowledge is forbidden for a reason, and is often highly dangerous. In other
cases, those within the group in question wish to keep such knowledge secret, and may go great
lengths to ensure this.""","Benefits of having the skill","Untrained")
print(Character_01.name)
print(Character_01.statWeaponSkill)
print(Character_01.statBallisticSkill)
print(Character_01.statStrength)
print(Character_01.statToughess)
print(Character_01.statAgility)
print(Character_01.statIntelligence)
print(Character_01.statPerception)
print(Character_01.statWillPower)
print(Character_01.statFellowship)

Character_01.characterSheet()
Skill_01.SkillSheet()
