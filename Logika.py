import tkinter as tk
import Wiktorina as wk

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


wilk = tk.Label(frame_Head, text="  D o c t o r  lern und spaß ",
        width=50, bg="grey", fg="red", font=('times' , 20, 'bold')).pack()
btn_w = tk.Button(frame_Button,text='Viktorina',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold'), command= lambda : wk.Wiktorina()).grid(row=0,column=0)
btn_k = tk.Button(frame_Button, text='Kartochki',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=1)
btn_pass = tk.Button(frame_Button,text='Ekonomka',width=12, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=2)
btn_q= tk.Button(frame_Button, text='Quele',width=14, bg='#003C80',fg='#FFFFFF',font=('Arial', 14,'bold')).grid(row=0,column=3)


Okno.mainloop()