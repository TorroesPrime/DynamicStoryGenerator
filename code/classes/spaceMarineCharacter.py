import strings
from strings import width, header, divider
class spaceMarineCharacter:
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
        #break_01 = int((width-len(name))/2-1)
        side = "|"
        print('break_01:'+str(break_01))
        print(side+' '*break_01+name+' '*break_01+side)
        print(divider)
        
        
        #print(testing)
        #line_name = "| "+(' '*int((width-len(self.name))/2)-1)+self.name+(' '*int((width-len(self.name))/2)-1)+" |"
        
        #print(line_name)
        
    def __selectChapter_():
        chapters = ['Ultramarines']
    def __selectName__():
        pass
