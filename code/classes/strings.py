width = 80
header = "="*width
divider = '-'*width
char = "Characteristics"
side = "|"
charWs = " WS "
charBs = " BS "
charS = "  S "
charT = "  T "
charAg = " AG "
charInt = " Int "
charFel = " Fel "
charWp = " WP "
charPer = " Per "
charCorr = " Cor "
charIns = " Ins "
charPsy = " Psy "
charFate = " Ft "
charRace = " Race  "
skills = "Character Skills"
abilities = "Character Abilities"
name = "Name"
prereq = "Pre-Requisit"
CharacteristicsHeaderLine = side+charRace+side+charWs+side+charBs+side+charS+side+charT+side+charAg+side+charInt+side+charPer+side+charWp+side+charFel+side+charFate+side+charCorr+side+charIns+side+charPsy+side
SkillsHeaderLine = side+(" "*int(width/2-1-len(skills)/2))+skills+(" "*int(width/2-1-len(skills)/2))+side
AbilitiesHeaderLine = side+(" "*int(width/2-2-len(skills)/2))+abilities+(" "*int(width/2-3-len(skills)/2))+side
SkillName = side+" "+name+(" "*int(width/2-7))+side+prereq+(" "*int(width/2-13))+side