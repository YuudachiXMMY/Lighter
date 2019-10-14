import xlrd
import xlwt
from xlutils.copy import copy
import os.path

from datetime import date,datetime

import numpy as np

import math

from numpy.linalg import lstsq

workbook = xlrd.open_workbook(r"W:\GamePython\Lighter\script2.xlsx")
conc = workbook.sheet_by_name('Sheet1')

rb1 = xlrd.open_workbook(r"W:\GamePython\Lighter\script2_cha.xlsx")
r_sheet1 = rb1.sheet_by_index(0)
wb1 = copy(rb1)
sheet1 = wb1.get_sheet(0)

rb2 = xlrd.open_workbook(r"W:\GamePython\Lighter\script2_other.xlsx")
r_sheet2 = rb2.sheet_by_index(0)
wb2 = copy(rb2)
sheet2 = wb2.get_sheet(0)

w_row1 = 0
w_row2 = 0

for i in range(1,2569):
    files_n = conc.row_values(i)[1]
    if files_n == 'w' or files_n == 'c' or files_n == 'y' or files_n == 'x' or files_n == 'l':
        for n in range(0,4):
            sheet1.write(w_row1,n,conc.row_values(i)[n])
            wb1.save(r"W:\GamePython\Lighter\script2_cha.xlsx")
        print 'row1:',w_row1
        w_row1 += 1

    else:
        for n in range(0,4):
            sheet2.write(w_row2,n,conc.row_values(i)[n])
            wb2.save(r"W:\GamePython\Lighter\script2_other.xlsx")
        print 'row2:',w_row2
        w_row2 += 1
