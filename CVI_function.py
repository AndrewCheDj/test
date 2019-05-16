import os
import xlrd
FirstString=[]
SecondString=[]
b = 0 # переменная для счета файлов
z = 0 # переменная чтобы занять прогу


def false():  # функция сопоставления файлов и вывода повторяющихся строк
    for x in range(b, num):  # цикл открытия всех файлов
        a = xlrd.open_workbook('E:\code\Cvi\Cvi\\' + files[x], on_demand=True)

        # функция печати названия файла и доставания и печати данных из файлов (из нужных столбцов и строк, они указаны в row[5:41] и rownum

        sheet = a.sheet_by_index(0)  # назначения листа из файла
#        print(files[x])  # печать названия файла
        for rownum in range(sheet.nrows):  # извлечение данных из файла
            row = sheet.row_values(rownum)
            if rownum > 6:
                SecondString = row[5:41]
                if SecondString == FirstString:
                    print (' В файле ' + str(files[x]) + ' в строке ' + str(rownum+1) + ' замечен хуй из файла ' + str(files[i]) + ' строка ' + str(rownumGlobal+1))
                else:
                    z=1


# выбор директории для работы
files = os.listdir('E:\code\Cvi\Cvi') # создание списка из названий файлов
#for file in files:
#    print (file) # печать названий файлов


num = len(files) # количество файлов

# открытие файла excel, в []-кавычках номер файла excel

for i in range (num): # цикл открытия всех файлов
    a = xlrd.open_workbook('E:\code\Cvi\Cvi\\' + files[i], on_demand=True)
    b+=1

# функция печати названия файла и доставания и печати данных из файлов (из нужных столбцов и строк, они указаны в row[5:41] и rownum

    sheet = a.sheet_by_index(0) # назначения листа из файла
    for rownumGlobal in range(sheet.nrows): # цикл доставания данных из файла построчно
        row = sheet.row_values(rownumGlobal)
        if rownumGlobal > 6:
            FirstString = row[5:41]
            false()