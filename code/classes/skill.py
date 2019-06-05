from strings import width, header, divider, side, SkillsHeaderLine, AbilitiesHeaderLine, SkillName

class Skill:
    def __init__(self, name, prereq,descrip,benefit, level):
        self.name =name
        self.prereq = prereq
        self.descrip = descrip
        self.benefit = benefit
        self.trainingLevel = level

    def SkillSheet(self):
        print(header)
        print(SkillName)
        