from strings import width, header, divider, char, side, CharacteristicsHeaderLine, SkillsHeaderLine, AbilitiesHeaderLine, SkillName

class Skill:
    def __init__(self, name, prereq,descrip,benefit):
        self.name =name
        self.prereq = prereq
        self.descrip = descrip
        self.benefit = benefit

    def SkillSheet(self):
        print(header)
        print(SkillName)
        