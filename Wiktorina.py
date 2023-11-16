from tkinter import messagebox as mb
import json
import Logika as logk


with open('woprosu.json',encoding="utf-8") as wikt:   #Ох и долго же я с этой строкой мучился...
    data = json.load(wikt)
question = (data['wopros'])
options = (data['wariant'])
answer = (data['otwet'])


class Wiktorin:
    def __init__(self):
        self.w_no = 0
        self.label = logk.tk.Label(logk.frame_Body, text="", width=50,
            font=('times', 20, 'bold'))
        self.display_title()
        self.display_question()
        self.opt_selected = logk.tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def display_title(self):
         logk.tk.Label(logk.frame_Body, text="  W  I  K  T  O  R  I  N  A  ",
         width=50, bg="grey", fg="red", font=('times' , 20, 'bold')).pack(side='top')
    def display_question(self):
            self.label.pack(pady='40')
            self.label.config(text = question[self.w_no])
    def radio_buttons(self):
        w_spisok = []
        while len(w_spisok) < 4:
            radio_btn = logk.tk.Radiobutton(logk.frame_Body, text=" ", variable=self.opt_selected,
            value=len(w_spisok) + 1, font=('times', 15))
            w_spisok.append(radio_btn)
            radio_btn.pack(side='bottom')
        return w_spisok
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.w_no]:
            self.opts[val]['text'] = option
            val += 1
    def buttons(self):
        logk.tk.Button(logk.frame_Footer, text="next", command=self.next_btn,
        width=11, bg='#003C80',fg='#FFFFFF',activebackground='red',activeforeground='#003C80',highlightcolor='grey',font=('Arial', 14,'bold')).pack()
    def check_ans(self, w_no):
        if self.opt_selected.get() == answer[w_no]:
            return True
    def next_btn(self):

        if self.check_ans(self.w_no):
            self.correct += 1
        self.w_no += 1

        if self.w_no == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

