import tkinter as tk
import json

Okno = tk.Tk()
Okno.geometry("800x500")
Okno.title('D O C T O R  lern und Spaß...')
with open("woprosu.json", encoding="utf-8") as reader:   #OH I DOLGO JE YA S ETOY STROKOY NAMUCHILSYA...
    pokazat = json.load(reader)
wopros = (pokazat['Woprosu'])
wariant = (pokazat['Wariantu'])
otvet = (pokazat['Otwetu'])
print(wopros)
print(wariant)
print(wariant)

Okno.mainloop()

