import tkinter as tk

Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R       Э  K  O  H  O  M  K  A...')
Bild = tk.PhotoImage(file='Phoenixx.png')
Okno.iconphoto(False, Bild)
Okno.geometry("800x615+300+120")
Okno.resizable(False, False)

frame_Futter = tk.Frame(Okno, height=800, width=35)
frame_Head = tk.Frame(Okno, height=800, width=275, bg='grey')
frame_Body = tk.Frame(Okno, height=800, width=300,  bg='red')
frame_Button = tk.Frame(Okno, height=800, width=300,  bg='blue')

frame_Futter.pack(side='bottom')
frame_Head.pack()
frame_Body.pack(side='left')
frame_Button.pack(side='right')


Title = tk.Label(frame_Futter, text=' Э  K  O  H  O  M  K  A ',fg='red',bg='#DADADA',font='Alial 35 bold').grid(row=0,column=0)

Stat_summa = tk.Label(frame_Button,text='Summa trat', font='Arial 15').grid(row=0,column=0, stick='w', padx=10, pady=10)
Stat_summa_tekst = tk.Label(frame_Button,text='Summa trat', font='Arial 15 bold').grid(row=0,column=1, stick='e', padx=10, pady=10)
Stat_kategor = tk.Label(frame_Button,text='Na CHTO potratil', font='Arial 15').grid(row=1,column=0, stick='w', padx=10, pady=10)
Stat_kategor_tekst = tk.Label(frame_Button,text='Razvecheniya', font='Arial 15 bold').grid(row=1,column=1, stick='e', padx=10, pady=10)
Stat_Den = tk.Label(frame_Button,text='Ssamuy dorogey den', font='Arial 15').grid(row=2,column=0, stick='w', padx=10, pady=10)
Stat_Den_tekst = tk.Label(frame_Button,text='Subbota', font='Arial 15 bold').grid(row=2,column=1, stick='e', padx=10, pady=10)
Stat_Mesyac = tk.Label(frame_Button,text='Ssamuy dorogey mesyac', font='Arial 15 ').grid(row=3,column=0, stick='w', padx=10, pady=10)
Stat_Mesyac_tekst = tk.Label(frame_Button,text='Leto', font='Arial 15 bold').grid(row=3,column=1, stick='e', padx=10, pady=10)



Sta_summa = tk.Label(frame_Body,text='Summa trat', font='Arial 20 bold').grid(row=0,column=0)
Stt_summa_tekst = tk.Label(frame_Head,text='Summa trat', font='Arial 20 bold').grid(row=0,column=1)






Okno.mainloop()