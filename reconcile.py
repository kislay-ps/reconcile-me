import os, openpyxl, Levenshtein as lev
from fuzzywuzzy import fuzz, process




dataSet1 = openpyxl.load_workbook('dataSet1.xlsx')
sheet1= dataSet1['Sheet1']
dataSet2 = openpyxl.load_workbook('dataSet2.xlsx')
sheet2 = dataSet2['Sheet1']


for data1 in sheet1['A']:
    for data2 in sheet2['A']:
        #Ratio = fuzz.ratio(str(data1),str(data2))
        #Partial_Ratio = fuzz.partial_ratio(str(data1),str(data2))
        #Token_Sort_Ratio = fuzz.token_sort_ratio(str(data1),str(data2))
        #Token_Set_Ratio = fuzz.token_set_ratio(str(data1),str(data2))
        highest = process.extractOne(str(data1),str(data2))
        #print(Ratio)
        #print(Partial_Ratio)
        #print(Token_Sort_Ratio)
        #print(Token_Set_Ratio)
        print(highest)
    print('---END--')




