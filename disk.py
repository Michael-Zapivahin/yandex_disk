import tkinter as tk
import openpyxl
from tkinter import filedialog
import requests

googleDriveStartPath = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id='
yandexPrefix = 'https://getfile.dokpub.com/yandex/get/'

# Колонка, в которую сохраняются ссылки через запятую
targetColumnNumber = 2
# Колонки со ссылками
linksColumnsNumbers = [1]

def get_link_from_value(itemLink):
    if itemLink is None or itemLink == '':
        return ''
    if 'drive.google' in itemLink:
        return googleDriveStartPath + itemLink.split('/')[5]
    elif 'disk.yandex' in itemLink:
        return yandexPrefix + itemLink
    else:
        return ''


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[
        ("Excel Files", "*.xlsx *.xls"),
        ("CSV Files", "*.csv")])

    wb = openpyxl.load_workbook(filepath)
    sheet_names = wb.sheetnames
    sheet = wb[sheet_names[0]]

    for row in range(2, sheet.max_row + 1):
        directLinks = ''
        for columnNumber in linksColumnsNumbers:
            itemLink = sheet.cell(row, columnNumber).value
            directLink = get_link_from_value(itemLink)
            if directLink is not None and directLink != '':
                directLinks = directLinks + directLink + ' , '

        sheet.cell(row, targetColumnNumber).value = directLinks
        directLinks = ''

    wb.save(filepath.replace('.xlsx', '-copy.xlsx'))
    print('Success')


if __name__ == "__main__":
    root = tk.Tk()
    open_button = tk.Button(root, text="Открыть файл", command=open_file)
    open_button.pack()
    root.mainloop()