import tkinter as tk
from tkinter import ttk
#import Logika as log


Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R       Э  K  O  H  O  M  K  A...')
Bild = tk.PhotoImage(file='Phoenixx.png')
Okno.iconphoto(False, Bild)
Okno.geometry("800x615+300+120")
Okno.resizable(False, False)



frame_Futter = tk.Frame(Okno, height=25, width=800, bg='yellow')
frame_Head = tk.Frame(Okno, height=285, width=800, bg='green')
frame_Body = tk.Frame(Okno, height=300, width=400,  bg='red')
frame_Button = tk.Frame(Okno, height=300, width=400,  bg='blue')

frame_Futter.pack(side='bottom', expand=True)
frame_Head.pack(side='top', expand=True)
frame_Body.pack(side='left', expand=True)
frame_Button.pack(side='right', expand=True)


Title = tk.Label(frame_Futter, text=' Э  K  O  H  O  M  K  A ',fg='red',bg='#DADADA',font='Alial 35 bold').grid(row=0,column=0)

Stat_summa = tk.Label(frame_Button,text='Chashe Vsego', font='Arial 15').grid(row=0,column=0, stick='w', padx=10, pady=10)
#Stat_summa_tekst = tk.Label(frame_Button,text=log.get_nachtochashe(), font='Arial 15 bold').grid(row=0,column=1, stick='e', padx=10, pady=10)
Stat_kategor = tk.Label(frame_Button,text='Bolshe Vsego', font='Arial 15').grid(row=1,column=0, stick='w', padx=10, pady=10)
#Stat_kategor_tekst = tk.Label(frame_Button,text=log.get_kakoyden(), font='Arial 15 bold').grid(row=1,column=1, stick='e', padx=10, pady=10)
Stat_Den = tk.Label(frame_Button,text='Samuy dorogoy den', font='Arial 15').grid(row=2,column=0, stick='w', padx=10, pady=10)
#Stat_Den_tekst = tk.Label(frame_Button,text=log.get_kakoyden(), font='Arial 15 bold').grid(row=2,column=1, stick='e', padx=10, pady=10)
Stat_Mesyac = tk.Label(frame_Button,text='Ssamuy dorogey mesyac', font='Arial 15 ').grid(row=3,column=0, stick='w', padx=10, pady=10)
#Stat_Mesyac_tekst = tk.Label(frame_Button,text=log.get_kakoymesyac(), font='Arial 15 bold').grid(row=3,column=1, stick='e', padx=10, pady=10)


list = [
    (1,'fff','fsfbsb',33),
    (2,'fff','fsfbsb',33),
    (3,'fff','fsfbsb',33),
    (4,'fff','fsfbsb',33),
    (5,'fff','fsfbsb',33),
]

title = ['id', 'Сумма', 'Дата платежа', 'Тип платежа']
tablica = ttk.Treeview(frame_Head)
#tablica['displaycolumns'] = ['Сумма','Тип платежа','Дата платежа','id']

tablica['columns'] = [0, 1 ,2, 3]
for row in list:
    tablica.insert('',tk.END, values=row)

for titles in title:
    tablica.heading(titles, text=titles, anchor='center')
    tablica.column(titles, anchor= 'center')


prokrutka = ttk.Scrollbar(frame_Head, command=tablica.yview())
prokrutka.pack(side=tk.RIGHT, fill=tk.Y)
tablica.pack(expand=tk.YES, fill=tk.BOTH)


Okno.mainloop()