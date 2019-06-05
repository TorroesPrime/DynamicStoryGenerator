from character import *
from race import *
from skill import *
RaceHuman = Race('Human')
Character_01 = Character("Bob",10,10,10,10,10,10,10,10,10,RaceHuman)
Skill_01 = Skill("Skill Name", "No pre-req","This is a description of the skill","Benefits of having the skill","Untrained")
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