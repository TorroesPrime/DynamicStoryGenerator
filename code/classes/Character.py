import strings
from strings import width, header, divider, char, side, CharacteristicsHeaderLine
class character:
    def __init__(self,name,weap,ball,stre,toug,agil,inte,perc,will,fell,chapter):
        self.name = name
        self.statWeaponSkill = weap
        self.statBallisticSkill = ball
        self.statStrength = stre
        self.statToughess = toug
        self.statAgility = agil
        self.statIntelligence = inte
        self.statPerception = perc
        self.statWillPower = will
        self.statFellowship = fell
        self.chapter = chapter
    def __characterSheet__(self):
        print(header)
        if len(self.name)/2 != 2:
            name = self.name+" "
        else:
            name = self.name
        break_01 = int((width-len(name))/2-1)
        break_02 = int((width-len(char))/2-1)
        
        #print('break_01:'+str(break_01))
        print(side+' '*break_01+name+' '*break_01+side)
        print(side+' '*break_02+char+' '+' '*break_02+side)
        print(divider)
        print(CharacteristicsHeaderLine)
        print(side+side)


