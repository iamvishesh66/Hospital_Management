from tkinter import *

class calculator:

    def __init__(self, parent, a, b):
        global operator
        from payments import bill_desk
        cal = parent

        self.f1 = Frame(cal, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)

        self.f2 = Frame(cal, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        btn = Button(self.f1, text="PAYMENTS-->", command=lambda: bill_desk(cal, 20, 40),
                           font=("arial", 14, "bold"), bd=5, bg="lawn green")
        btn.place(x=800, y=500)

        title = Label(self.f2, text="CALCULATOR", font=("algerian", 20, "bold", "underline"),
                      fg="dodger blue3"
                      , bg="white").place(x=350, y=0)

        operator = ""
        text_input = StringVar()

        def btnclick(number):
            global operator
            operator = operator + str(number)
            text_input.set(operator)
        def btnclick1(e):
            global operator
            number = e.keysym
            if number.isdigit():
                operator = operator + str(number)
                text_input.set(operator)
            elif number == "plus":
                operator = operator + str("+")
                text_input.set(operator)
            elif number == "minus":
                operator = operator + str("-")
                text_input.set(operator)
            elif number == "asterisk":
                operator = operator + str("*")
                text_input.set(operator)
            elif number == "slash":
                operator = operator + str("/")
                text_input.set(operator)
            elif number == "BackSpace":
                operator = ""
                text_input.set(operator)
            elif number == "Return":
                a = str(eval(operator))
                text_input.set(a)
                operator = ""
        def clsbutton():
            global operator
            operator = ""
            text_input.set(operator)

        def eqlbutton():
            global operator
            a = str(eval(operator))
            text_input.set(a)
            operator = ""

        self.dis = Entry(cal, font=("arial", 20, "bold"), bd=30, textvariable=text_input, justify="right", state="readonly")
        self.dis.place(x=300, y=50)
        self.dis.bind("<Key>", btnclick1)
        self.dis.focus()

        self.btn7 = Button(cal, padx=6, pady=6, text="7", bg="powder blue", font=("arial", 20, "bold"), bd=20, command=lambda:btnclick(7))
        self.btn7.place(x=300, y=150)
        self.btn8 = Button(cal, padx=6, pady=6, text="8", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(8))
        self.btn8.place(x=390, y=150)
        self.btn9 = Button(cal, padx=6, pady=6, text="9", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(9))
        self.btn9.place(x=480, y=150)
        self.add = Button(cal, padx=6, pady=6, text="+", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick('+'))
        self.add.place(x=570, y=150)

        self.btn4 = Button(cal, padx=6, pady=6, text="4", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(4))
        self.btn4.place(x=300, y=250)
        self.btn5 = Button(cal, padx=6, pady=6, text="5", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(5))
        self.btn5.place(x=390, y=250)
        self.btn6 = Button(cal, padx=6, pady=6, text="6", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(6))
        self.btn6.place(x=480, y=250)
        self.sub = Button(cal, padx=10, pady=6, text="-", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick('-'))
        self.sub.place(x=570, y=250)

        self.btn1 = Button(cal, padx=6, pady=6, text="1", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(1))
        self.btn1.place(x=300, y=350)
        self.btn2 = Button(cal, padx=6, pady=6, text="2", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(2))
        self.btn2.place(x=390, y=350)
        self.btn3 = Button(cal, padx=6, pady=6, text="3", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(3))
        self.btn3.place(x=480, y=350)
        self.mul = Button(cal, padx=9, pady=6, text="*", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick('*'))
        self.mul.place(x=570, y=350)

        self.btn0 = Button(cal, padx=6, pady=6, text="0", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick(0))
        self.btn0.place(x=300, y=450)
        self.cls = Button(cal, padx=6, pady=6, text="c", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=clsbutton)
        self.cls.place(x=390, y=450)
        self.eql = Button(cal, padx=6, pady=6, text="=", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=eqlbutton)
        self.eql.place(x=480, y=450)
        self.div = Button(cal, padx=10, pady=6, text="/", bg="powder blue", font=("arial", 20, "bold"), bd=20,command=lambda:btnclick('/'))
        self.div.place(x=570, y=450)
        cal.mainloop()

def main():
    pass


if __name__ == '__main__':
    main()
