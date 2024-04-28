import tkinter as tk
from tkinter import filedialog

from yadisk import get_links_per_file


googleDriveStartPath = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id='
yandexPrefix = 'https://getfile.dokpub.com/yandex/get/'



def open_file():
    filepath = filedialog.askopenfilename(filetypes=[
        ("Excel Files", "*.xlsx *.xls"),
        ("CSV Files", "*.csv")])

    get_links_per_file(filepath)
    print('Success')


if __name__ == "__main__":
    root = tk.Tk()
    open_button = tk.Button(root, text="Открыть файл", command=open_file)
    open_button.pack()
    root.mainloop()
