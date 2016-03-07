import openpyxl
import os

os.chdir('/Users/leonardlabita/Desktop')

wb = openpyxl.Workbook()

wb.get_sheet_names()

sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'] = 42
sheet['A2'] = 'Hello'

wb.save('editExample.xlsx')