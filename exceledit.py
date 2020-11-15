from openpyxl import load_workbook

workbook=load_workbook(filename='graduateshotline_word_list.xlsx')
sheet=workbook.active
val=sheet["A6"].value
for i in range(6,1313):
    sheet[f"A{i}"].value=f'"{sheet[f"A{i}"].value}",'
    print(sheet[f"A{i}"].value)


