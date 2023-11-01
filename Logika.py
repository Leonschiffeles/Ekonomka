import tkinter as tk
#from tkinter import messagebox as mb
import json

Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R  lern und Spaß...')
Okno.geometry("620x490+400+200")
Okno.resizable(False, False)


frame_Head = tk.Frame(Okno,width=620,height=75,bg='grey')
frame_Body = tk.Frame(Okno,width=620,height=275,bg='red')
frame_Footer = tk.Frame(Okno,width=620,height=100,bg='#FFFFFF')
frame_Button = tk.Frame(Okno,width=620,height=40,bg='#008FCD')


frame_Head.pack(side='top',fill='x')
frame_Body.pack(fill='x')
frame_Button.pack(side='bottom',fill='x')
frame_Footer.pack(side='bottom',fill='x')



btn_w = tk.Button(frame_Button,text='Viktorina',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=0)
btn_k = tk.Button(frame_Button, text='Kartochki',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=1)
btn_pass = tk.Button(frame_Button,text='Ekonomka',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=2)
btn_q= tk.Button(frame_Button, text='Quele',width=14, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=3)


with open("woprosu.json", encoding="utf-8") as reader:   #OH I DOLGO JE YA S ETOY STROKOY NAMUCHILSYA...
    pokazat = json.load(reader)
wopros = (pokazat['Woprosu'])
wariant = (pokazat['Wariantu'])
otvet = (pokazat['Otwetu'])



class Wiktorina:
    def __init__(self):
        self.nw = 0
        self.war_otweta = tk.IntVar()
        self.woprosss = self.wopros(self.nw)
        self.waeriant = self.radiobottonns()
        self.pokazat_wariant(self.nw)

    def wopros(self, nw):
       Otobrazitwopros = tk.Label(frame_Head, text='WIKTORINA', fg= 'red',bg='grey', width=40 , font=( 'times' , 30, 'bold')).pack()
       nw = tk.Label(frame_Body,text=wopros[nw], width=40 , font=( 'times' , 20, 'bold'), anchor="w").pack(side='top')
       np = tk.Label(frame_Body, text='wopros[nw]', width=40, font=('times', 15, 'bold'), anchor="w").pack(side='right')
       return nw

    def radiobottonns(self):
        val = 0
        kn = []
        while val < 4:
            knop = tk.Radiobutton(frame_Body, text="", variable=self.war_otweta, value=val+1, font=("times", 14)).pack(side='bottom')
            kn.append(knop)
            val += 1
        return kn

    def pokazat_wariant(self, nw):
        znach = 0
        self.war_otweta.set(0)
        self.woprosss['text'] = wopros[nw]  # Pochemu to self.woprosss NONE...
        for warotw in wariant[nw]:
            self.waeriant[znach]['text'] = warotw
            znach += 1






wi = Wiktorina()
Okno.mainloop()