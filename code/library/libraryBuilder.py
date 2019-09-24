import xlrd
fileNames = ['human_male_names.txt',
'human_female_names.txt',
'human_last_names.txt',
'human_titles.txt',
'blood_angles_names.txt',    
'blood_angles_titles.txt',
'dark_angles_names.txt',
'dark_angles_titles.txt',
'space_wolves_names.txt',
'space_wolves_titles.txt',
'ultramarine_names.txt',
'ultramarine_titles.txt',
'black_templar_names.txt',
'black_templar_titles.txt',
'iron_hanes_names.txt',
'salamander_names.txt',
'raven_guard_names.txt',
'white_scar_names.txt',
'races.txt',
'death_world_names.txt',
'void_born_names.txt',
'forge_world_names.txt',
'hive_world_names.txt',
'imperial_world_names.txt',
'noble_born_names.txt']

workbook = xlrd.open_workbook("library.xlsx")
worksheet = workbook.sheet_by_name("names")
total_rows = worksheet.nrows
col = 0
while col <= 25:
    for name in fileNames:
        libFile = open(name, "a")
        row = 1
        while row < total_rows:
            j = worksheet.cell(row,col).value
            if j != "":
                content = j+'\n'
                libFile.write(content)
                print("col: "+str(col)+", row: "+str(row))
                print(content)
            else:
                pass
            row += 1
        libFile.close()
    col += 1    