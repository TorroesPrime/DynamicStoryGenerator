import textwrap
from strings import width, header, divider, side, SkillsHeaderLine, AbilitiesHeaderLine, SkillName, skills

class Skill:
    def __init__(self, name, prereq, descrip, benefit, level):
        self.name =name
        self.prereq = prereq
        self.descrip = descrip
        self.benefit = benefit
        self.trainingLevel = level

    def SkillSheet(self):
        print(header)
        print(SkillName)
        print(side+" "+self.name+(" "*(int(width/2)-int(len(self.name))-3))+side+" "+self.prereq+(" "*(int(width/4)-int(len(self.prereq))+1))+side)
        print(divider)
        description = textwrap.TextWrapper(width = 76)
        word_list = description.wrap(text=self.descrip)
        for element in word_list:
            print("| "+element)
        print(divider)

        