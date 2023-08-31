import openpyxl
  
workbook = openpyxl.load_workbook("aa.xlsx")
  
sheet = workbook.worksheets[0]
  
urls = []
  
for i, row in enumerate(sheet):
    if i == 0:
        continue
    name = row[2].value
    urls.append(name)
  
print(urls)