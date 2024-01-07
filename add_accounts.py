from tkinter import *
from pymysql import *
from tkinter import messagebox

class add_acc_admin:
    def __init__(self):
        self.acc_win1 = Toplevel()
        self.acc_win1.focus_force()
        self.acc_win1.wm_resizable(0, 0)
        self.acc_win1.title("ADD ADMIN")
        self.acc_win1.wm_iconbitmap("hospital.ico")
        self.acc_win1.geometry("400x500+450+100")
        self.acc_win1.focus_force()
        bg_pic = PhotoImage(file="sign.png")
        self.canv1 = Canvas(self.acc_win1, highlightbackground="white")
        self.canv1.pack(expand=YES, fill=BOTH)
        self.canv1.create_image(200, 250, image=bg_pic)
        self.canv1.create_text(200, 50, text="Create a Account", font=("algerian", 32, "bold", "italic"), fill="white")

        # entry and labels for information
        self.canv1.create_text(80, 145, text="Name", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e1 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.place(x=150, y=130)

        self.canv1.create_text(80, 195, text="User Name", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e2 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.place(x=150, y=180)

        self.canv1.create_text(80, 245, text="Password", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e3 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e3.bind("<FocusIn>", lambda e: self.remtext("e3"))
        self.e3.bind("<FocusOut>", lambda e: self.deftext("e3"))
        self.e3.place(x=150, y=230)

        self.canv1.create_text(80, 295, text="Retype", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e4 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.place(x=150, y=280)

        btn = Button(self.canv1, text="Add Account", bd=5, font=("algerian", 15, "bold", "italic"), bg="purple", fg="white"
                     , command=self.savedata)
        btn.place(x=150, y=330)

        # lets give it a note
        self.canv1.create_text(190, 450, text="(Note: This account will be used\n\t\t as your main admin.)", fill="red"
                               , font=("algerian", 13, "bold", "italic"))
        # some imp stuff
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()

        self.acc_win1.bind("<Enter>", lambda e: self.showtext())

        self.acc_win1.mainloop()

    def showtext(self):

        if not self.t1.get():
            self.acc_win1.focus_set()
            self.t1.set("Enter Your Name")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.acc_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if self.t2.get() == "eg: ram21":
            self.acc_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.acc_win1.focus_set()
            self.t3.set("Create A Strong Password")
            self.e3.config(textvariable=self.t3, fg="grey")
        if not self.t4.get():
            self.acc_win1.focus_set()
            self.t4.set("Retype Your Password")
            self.e4.config(textvariable=self.t4, fg="grey")

    def remtext(self, name):

        if name == "e1":
            if self.t1.get() == "Enter Your Name":
                self.t1.set("")
            else:
                self.t1.set(self.e1.get())
            self.e1.config(textvariable=self.t1, fg="black")
        if name == "e2":
            if self.t2.get() == "Create UserName To Login Later":
                self.t2.set("eg: ram21")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black")
        elif name == "e3":
            if self.t3.get() == "Create A Strong Password":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", show="*")
        elif name == "e4":
            if self.t4.get() == "Retype Your Password":
                self.t4.set("")
            else:
                self.t4.set(self.e4.get())
            self.e4.config(textvariable=self.t4, fg="black", show="*")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="sky blue")
        elif name == "e2":
            self.e2.config(bg="sky blue")
        elif name == "e3":
            self.e3.config(bg="sky blue")
        elif name == "e4":
            self.e4.config(bg="sky blue")

    def savedata(self):
        if self.e3.get() == self.e4.get():
            try:
                d1 = Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc.execute("insert into login values(%s,%s,%s,%s)",
                               (self.e1.get(), self.e2.get(), self.e3.get(), "admin"))
                    d1.commit()
                    a = messagebox.askquestion("ADDED SUCCESSFULLY", "Do you want to add another account?")
                    if a == "yes":
                        self.e1.delete(0, END)
                        self.e2.delete(0, END)
                        self.e3.delete(0, END)
                        self.e4.delete(0, END)
                    else:
                        self.acc_win1.destroy()
                except Exception as e:
                    messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.acc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.acc_win1)
        else:
            messagebox.showerror("ERROR", "Your Passwords Don't Match")
            self.e3.delete(0, END)
            self.e4.delete(0, END)

class add_acc_user:
    def __init__(self):
        self.acc_win1 = Toplevel()
        self.acc_win1.focus_force()
        self.acc_win1.wm_resizable(0, 0)
        self.acc_win1.title("ADD USER")
        self.acc_win1.wm_iconbitmap("hospital.ico")
        self.acc_win1.geometry("400x500+450+100")
        self.acc_win1.focus_force()
        bg_pic = PhotoImage(file="sign.png")
        self.canv1 = Canvas(self.acc_win1, highlightbackground="white")
        self.canv1.pack(expand=YES, fill=BOTH)
        self.canv1.create_image(200, 250, image=bg_pic)
        self.canv1.create_text(200, 50, text="Create a Account", font=("algerian", 32, "bold", "italic"), fill="white")

        # entry and labels for information
        self.canv1.create_text(80, 145, text="Name", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e1 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.place(x=150, y=130)

        self.canv1.create_text(80, 195, text="User Name", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e2 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.place(x=150, y=180)

        self.canv1.create_text(80, 245, text="Password", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e3 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e3.bind("<FocusIn>", lambda e: self.remtext("e3"))
        self.e3.bind("<FocusOut>", lambda e: self.deftext("e3"))
        self.e3.place(x=150, y=230)

        self.canv1.create_text(80, 295, text="Retype", font=("algerian", 15, "bold", "italic"), fill="black")
        self.e4 = Entry(self.canv1, width=25, bg="sky blue", font=("algerian", 12, "italic", "bold"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.place(x=150, y=280)

        btn = Button(self.canv1, text="Add Account", bd=5, font=("algerian", 15, "bold", "italic"), bg="purple", fg="white"
                     , command=self.savedata)
        btn.place(x=150, y=330)

        # lets give it a note
        self.canv1.create_text(190, 450, text="(Note: This account will be used\n\t\t without special permissions.)", fill="red"
                               , font=("algerian", 13, "bold", "italic"))
        # some imp stuff
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()

        self.acc_win1.bind("<Enter>", lambda e: self.showtext())

        self.acc_win1.mainloop()

    def showtext(self):

        if not self.t1.get():
            self.acc_win1.focus_set()
            self.t1.set("Enter Your Name")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.acc_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if self.t2.get() == "eg: ram21":
            self.acc_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.acc_win1.focus_set()
            self.t3.set("Create A Strong Password")
            self.e3.config(textvariable=self.t3, fg="grey")
        if not self.t4.get():
            self.acc_win1.focus_set()
            self.t4.set("Retype Your Password")
            self.e4.config(textvariable=self.t4, fg="grey")

    def remtext(self, name):

        if name == "e1":
            if self.t1.get() == "Enter Your Name":
                self.t1.set("")
            else:
                self.t1.set(self.e1.get())
            self.e1.config(textvariable=self.t1, fg="black")
        if name == "e2":
            if self.t2.get() == "Create UserName To Login Later":
                self.t2.set("eg: ram21")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black")
        elif name == "e3":
            if self.t3.get() == "Create A Strong Password":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", show="*")
        elif name == "e4":
            if self.t4.get() == "Retype Your Password":
                self.t4.set("")
            else:
                self.t4.set(self.e4.get())
            self.e4.config(textvariable=self.t4, fg="black", show="*")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="sky blue")
        elif name == "e2":
            self.e2.config(bg="sky blue")
        elif name == "e3":
            self.e3.config(bg="sky blue")
        elif name == "e4":
            self.e4.config(bg="sky blue")

    def savedata(self):
        if self.e3.get() == self.e4.get():
            try:
                d1 = Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc.execute("insert into login values(%s,%s,%s,%s)",
                               (self.e1.get(), self.e2.get(), self.e3.get(), "user"))
                    d1.commit()
                    a = messagebox.askquestion("ADDED SUCCESSFULLY", "Do you want to add another account?")
                    if a == "yes":
                        self.e1.delete(0, END)
                        self.e2.delete(0, END)
                        self.e3.delete(0, END)
                        self.e4.delete(0, END)
                    else:
                        self.acc_win1.destroy()
                except Exception as e:
                    messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.acc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.acc_win1)
        else:
            messagebox.showerror("ERROR", "Your Passwords Don't Match")
            self.e3.delete(0, END)
            self.e4.delete(0, END)