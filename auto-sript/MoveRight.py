import xlrd
import xlwt
from xlutils.copy import copy
import os.path
import os
import shutil

workbook = xlrd.open_workbook(r"W:/GamePython/Lighter/test2.xlsx")
conc = workbook.sheet_by_name('dialogue')

rb = xlrd.open_workbook(r"W:/GamePython/Lighter/script2.xlsx")
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
sheet = wb.get_sheet(0)

w_row = 0

voice_target = "W:/GamePython/Lighter/game/voiceUnFinished/"
voice_final = "W:/GamePython/Lighter/game/voiceTemp/"

file_n = conc.row_values(0)[3]

for i in range(0,2569):
    '''character = conc.row_values(i)[1]
    if character != "" and character != "narrator":
        voice = conc.row_values(i)[0]+".wav"
        try:
            shutil.move(voice_target+voice,voice_final+voice)
            print "succeed"
        except:
            for n in range(0,4):
                sheet.write(w_row,n,conc.row_values(i)[n])
                wb.save(r"W:/GamePython/Lighter/script2.xlsx")
            print w_row
            w_row += 1
    '''
    voice = conc.row_values(i)[0]+".wav"
    try:
        shutil.move(voice_target+voice,voice_final+voice)
        print "succeed"
    except:
        for n in range(0,4):
            sheet.write(w_row,n,conc.row_values(i)[n])
            wb.save(r"W:/GamePython/Lighter/script2.xlsx")
        print w_row
        w_row += 1
