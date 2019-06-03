import strings
import random
from strings import width, header, divider, char, side, CharacteristicsHeaderLine, SkillsHeaderLine, AbilitiesHeaderLine
class character:
    def __init__(self,name,weap,ball,stre,toug,agil,inte,perc,will,fell,race):
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
        self.statFate = self.__genFatePoints__()
        self.statCorruption = 0
        self.statInsanity = 0
        self.statPsy = 0
        self.statRace = race
    
    def __genFatePoints__(self):
        fate = (3,3,3,3,3,3,3,4,4,5)
        return(random.choice(fate))


    def __characterSheet__(self):
        print(header)
        if len(self.name)/2 != 2:
            name = self.name+" "
        else:
            name = self.name
        break_01 = int((width-len(name))/2-1)
        break_02 = int((width-len(char))/2-1)

        statWeaponSkill = " "+str(self.statWeaponSkill)+" "
        statBallisticSkill = " "+str(self.statBallisticSkill)+" "
        statStrength = " "+str(self.statStrength)+" "
        statT = " "+str(self.statToughess)+" "
        statAg = " "+str(self.statAgility)+" "
        statInt = "  "+str(self.statIntelligence)+" "
        statPer = "  "+str(self.statPerception)+" "
        statWp = " "+str(self.statWillPower)+" "
        statFel = "  "+str(self.statFellowship)+" "
        statFate = "  "+str(self.statFate)+ " "
        if len(str(self.statCorruption)) == 1:
            statCorr = "  "+str(self.statCorruption)+ "  "
        elif len(str(self.statCorruption)) > 2:
            statCorr = 'ERROR '
        else:
            statIns = " "+str(self.statCorruption)+ "  "
        if len(str(self.statInsanity)) == 1:
            statIns = "  "+str(self.statInsanity)+ "  "
        elif len(str(self.statInsanity)) >= 3:
            statIns = 'ERROR '
        else:
            statIns = " "+str(self.statInsanity)+ " "
        if len(str(self.statPsy)) == 2:
            statPsy = "  "+str(self.statPsy)+"  "
        elif len(str(self.statPsy)) > 2:
            statPsy = "ERROR"
        else:
            statPsy = "  "+str(self.statPsy)+"  "
        if len(self.statRace.name) > 7:
            statRace = self.statRace.name[:6]
        else:
            statRace = self.statRace.name+(" "*(7-len(self.statRace.name)))
        #print('break_01:'+str(break_01))
        print(side+' '*break_01+name+' '*break_01+side)
        print(side+' '*break_02+char+' '+' '*break_02+side)
        print(divider)
        print(CharacteristicsHeaderLine)
        print(side+statRace+side+statWeaponSkill+side+statBallisticSkill+side+statStrength+side+statT+side+statAg+side+statInt+side\
        +statPer+side+statWp+side+statFel+side+statFate+side+statCorr+side+statIns+side+statPsy+side)
        print(divider)
        print(SkillsHeaderLine)
        print(divider)
        print(side+(" "*(width-2))+side)
        print(divider)
        print(AbilitiesHeaderLine)
        print(divider)
        print(side+(" "*(width-2))+side)
        print(divider)    
        print(SkillsHeaderLine)
        print(divider)
        print(side+(" "*(width-2))+side)
        print(header)


