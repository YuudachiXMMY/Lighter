import xlrd
import xlwt
from xlutils.copy import copy
import os.path
import os
import shutil

workbook = xlrd.open_workbook(r"W:/GamePython/Lighter/dlc1.xlsx")
conc = workbook.sheet_by_name('dialogue')

rb = xlrd.open_workbook(r"W:/GamePython/Lighter/dlc1w.xlsx")
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
sheet = wb.get_sheet(0)

w_row = 0

voice_target = "W:/GamePython/Lighter/game/125/"
voice_final = "W:/GamePython/Lighter/game/temp/"

file_n = conc.row_values(0)[3]

for i in range(0,2569):
    character = conc.row_values(i)[1]
    if character != "" and character != "nvl_narrator"and character != "w_nvl":
        voice = conc.row_values(i)[0]+".wav"
        try:
            shutil.move(voice_target+voice,voice_final+voice)
            print "succeed"
        except:
            for n in range(0,4):
                sheet.write(w_row,n,conc.row_values(w_row)[n])
                wb.save(r"W:/GamePython/Lighter/dlc1w.xlsx")
                print w_row
                
w_row += 1
