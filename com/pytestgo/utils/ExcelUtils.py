'''
Created on 2017年5月16日

@author: Administrator
'''
import xlrd

def readExcel(excel_path, sheet_name):
    result = []
    data = xlrd.open_workbook(excel_path)
    table = data.sheet_by_name(sheet_name)
    
    for row in range(1, table.nrows):
        if table.row_values(row)[8] != False:
            result.append(table.row_values(row))

        
    return result