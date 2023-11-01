import tkinter as tk
import json
import Logika as log


Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R  lern und Spaß...')
Okno.geometry("600x490+400+200")
Okno.resizable(False, False)


frame_Head = tk.Frame(Okno,width=600,height=75,bg='grey')
frame_Body = tk.Frame(Okno,width=600,height=275,bg='red')
frame_Footer = tk.Frame(Okno,width=600,height=100,bg='#FFFFFF')
frame_Button = tk.Frame(Okno,width=600,height=40,bg='#008FCD')


frame_Head.pack(side='top',fill='x')
frame_Body.pack(fill='x')
frame_Button.pack(side='bottom',fill='x')
frame_Footer.pack(side='bottom',fill='x')



btn_w = tk.Button(frame_Button,text='Viktorina',width=11, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=0)
btn_k = tk.Button(frame_Button, text='Kartochki',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=1)
btn_pass = tk.Button(frame_Button,text='Pogoda',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=2)
btn_q= tk.Button(frame_Button, text='Quele',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=3)



Okno.mainloop()