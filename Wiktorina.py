import json
import Logika as logk


with open('woprosu.json', encoding="utf-8") as wikt:   #Ох и долго же я с этой строкой мучился......
    data = json.load(wikt)
question = (data['wopros'])
options = (data['wariant'])
answer = (data['otwet'])


class Wiktorina:
    def __init__(self):
        self.w_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = logk.tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0

    def display_title(self):
        title = logk.tk.Label(logk.frame_Body, text="  W  I  K  T  O  R  I  N  A  ",
        width=50, bg="grey", fg="red", font=('times' , 20, 'bold')).pack()
    def display_question(self):
            w_no = logk.tk.Label(logk.frame_Body, text=question[self.w_no], width=60,
            font=('times' , 20, 'bold')).pack(side='top')
    def radio_buttons(self):
        q_list = []
        while len(q_list) < 4:
            radio_btn = logk.tk.Radiobutton(logk.frame_Body, text=" ", variable=self.opt_selected,
            value=len(q_list) + 1, font=('times', 15))
            q_list.append(radio_btn)
            radio_btn.pack()
        return q_list
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.w_no]:
            self.opts[val]['text'] = option
            val += 1
    def buttons(self):
        next_button = logk.tk.Button(logk.frame_Body, text="next", command=self.next_btn,
        width=10, bg="#003C80", fg="#FFFFFF", font=('times' , 12, 'bold')).pack()
    def check_ans(self, w_no):
        if self.opt_selected.get() == answer[w_no]:
            return True
    def next_btn(self):

        if self.check_ans(self.w_no):
            self.correct += 1
        self.w_no += 1

        if self.w_no == self.data_size:
            self.display_result()
            frame_Body.destroy()
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

