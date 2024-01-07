from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

from Home_page2 import Homepage


class start_win2:
    def __init__(self):
        self.start_win1 = Toplevel()
        self.start_win1.wm_overrideredirect(True)
        self.start_win1.geometry("750x395+300+120")
        self.canv = Canvas(self.start_win1, highlightbackground="green")
        self.canv.pack(expand=YES, fill=BOTH)
        self.start_win1.Canvas = self.canv
        bg_pic1 = PhotoImage(file="cipher.png")
        self.canv.create_image(380,200,image=bg_pic1)
        s = ttk.Style()
        s.theme_use('xpnative')
        progress = Progressbar(self.canv, orient=HORIZONTAL, length=150, mode="determinate", style="Horizontal.TProgressbar")
        progress.place(x=20, y=350)
        progress.start(20)
        self.canv.create_text(80,340, text="Loading...", font=("arial",12,"italic","bold"), fill="white")
        self.canv.create_text(600, 80, text="Cipher VS\nSolutions", font=("algerian",40,"bold","italic"), fill="orange")
        self.canv.create_text(640, 340, text=" Thinking Innovative\n    Data Management", font=("algerian",15,"bold","italic"), fill="white")
        l1 = Label(self.start_win1)
        l1.after(2000, lambda: progress.stop())
        l1.after(2250, Homepage)
        l1.after(2500, lambda: self.start_win1.destroy())
        self.start_win1.mainloop()

def main():
    start_win2()
if __name__ == '__main__':
    main()