import tkinter as tk

Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R       Э  K  O  H  O  M  K  A...')
Bild = tk.PhotoImage(file='Phoenixx.png')
Okno.iconphoto(False, Bild)
Okno.geometry("800x615+300+120")
Okno.resizable(False, False)


frame_Head_1 = tk.Frame(Okno, width=800, height=50,)
frame_Head = tk.Frame(Okno, width=800,height=265, bg='grey')
frame_Body = tk.Frame(Okno, width=400,height=300, bg='red')
frame_Button = tk.Frame(Okno, width=400, height=300, bg='blue')

frame_Head_1.grid(row=0, column=0, columnspan=2)
frame_Head.grid(row=1, column=0, columnspan=2)
frame_Body.grid(row=2, column=0, stick='nw')
frame_Button.grid(row=2, column=1, stick='en')


Title = tk.Label(frame_Head_1, text=' Э  K  O  H  O  M  K  A ',fg='red',bg='#DADADA',font='Alial 35 bold').grid(row=0,column=0)




Okno.mainloop()