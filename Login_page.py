import os
from start_page import *
from pymysql import *
from tkinter import messagebox

from start_page2 import start_win2


class login_win1:
    def __init__(self):
        self.log_win1 = Tk()
        self.log_win1.focus_force()
        self.log_win1.wm_resizable(0, 0)
        self.log_win1.title("SIGN UP")
        self.log_win1.wm_iconbitmap("hospital.ico")
        self.log_win1.geometry("400x500+450+100")
        self.log_win1.focus_force()
        bg_pic = PhotoImage(file="sign.png")
        self.canv1 = Canvas(self.log_win1, highlightbackground="white")
        self.canv1.pack(expand=YES ,fill=BOTH)
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
        self.e4.bind("<Return>", lambda e: self.savedata())

        btn = Button(self.canv1, text="Sign Up", bd=5, font=("algerian", 15, "bold", "italic"), bg="purple", fg="white"
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

        self.log_win1.bind("<Enter>", lambda e: self.showtext())

        self.log_win1.mainloop()

    def showtext(self):

        if not self.t1.get():
            self.log_win1.focus_set()
            self.t1.set("Enter Your Name")
            self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.log_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if  self.t2.get() == "eg: ram21":
            self.log_win1.focus_set()
            self.t2.set("Create UserName To Login Later")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.log_win1.focus_set()
            self.t3.set("Create A Strong Password")
            self.e3.config(textvariable=self.t3, fg="grey")
        if not self.t4.get():
            self.log_win1.focus_set()
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
                d1=Connect(host="localhost", user="root", password="", db="hospital")
                try:
                    dc = d1.cursor()
                    dc.execute("insert into login values(%s,%s,%s,%s)",
                               (self.e1.get(),self.e2.get(),self.e3.get(), "admin"))
                    d1.commit()
                    messagebox.showinfo("RESTART", "Restart App To Login")
                    self.log_win1.destroy()
                except Exception as e:
                    messagebox.showerror("ERROR","Error in creation"+str(e), parent=self.log_win1)
            except Exception as e:
                messagebox.showerror("ERROR","Error in Connection"+str(e), parent=self.log_win1)
        else:
            messagebox.showerror("ERROR","Your Passwords Don't Match")
            self.e3.delete(0, END)
            self.e4.delete(0, END)


class login_win2:
    def __init__(self):
        self.log_win2 = Tk()
        self.log_win2.focus_force()
        self.log_win2.wm_resizable(0, 0)
        self.log_win2.title("Log In")
        self.log_win2.wm_iconbitmap("hospital.ico")
        self.log_win2.geometry("400x500+450+100")
        self.log_win2.focus_force()
        bg_pic = PhotoImage(file="sign.png")
        self.canv1 = Canvas(self.log_win2, highlightbackground="white")
        self.canv1.pack(expand=YES, fill=BOTH)
        self.canv1.create_image(200, 250, image=bg_pic)
        self.canv1.create_text(200, 50, text="Sign In To \n    Your Account"
                               , font=("algerian", 30, "bold", "italic"), fill="white")

        # entry and labels for information
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
        self.e3.bind("<Return>", lambda e: self.checklog())

        btn = Button(self.canv1, text="Sign In", bd=5, font=("algerian", 15, "bold", "italic")
                     , bg="purple", fg="white", command=self.checklog)
        btn.place(x=150, y=330)

        img = PhotoImage(file="settings.png").subsample(40,40)
        btn1 = Button(self.canv1, image=img, command=self.fac_reset_page)
        btn1.place(x=370, y=2)

        # lets give it a note
        self.canv1.create_text(200, 450, text="(Note: If using admin username you will be\n\t\tlogged in with special permissions.)", fill="red"
                               , font=("algerian", 11, "bold", "italic"))
        # some imp stuff
        self.t2 = StringVar()
        self.t3 = StringVar()

        self.log_win2.bind("<Enter>", lambda e: self.showtext())

        self.log_win2.mainloop()

    def showtext(self):
        if not self.t2.get():
            self.log_win2.focus_set()
            self.t2.set("Enter Your User Name")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.log_win2.focus_set()
            self.t3.set("Enter Your Password")
            self.e3.config(textvariable=self.t3, fg="grey")

    def remtext(self, name):
        if name == "e2":
            if self.t2.get() == "Enter Your User Name":
                self.t2.set("")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black")
        elif name == "e3":
            if self.t3.get() == "Enter Your Password":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", show="*")

    def deftext(self, name):
        if name == "e2":
            self.e2.config(bg="sky blue")
        elif name == "e3":
            self.e3.config(bg="sky blue")

    def checklog(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT type FROM login WHERE username=%s AND password=%s"
                           , (self.e2.get(), self.e3.get()))
                f1 = dc.fetchone()
                for j in f1:
                    if j == "admin":
                        self.log_win2.after(1, lambda: start_win1())
                        self.log_win2.after(2, lambda: self.e3.delete(0, END))
                        self.log_win2.after(2, lambda: self.e2.delete(0, END))
                        self.log_win2.after(2, lambda: self.t3.set(""))
                        self.log_win2.after(3, lambda: self.log_win2.state("iconic"))
                    elif j == "user":
                        self.log_win2.after(1, lambda: start_win2())
                        self.log_win2.after(2, lambda: self.e3.delete(0, END))
                        self.log_win2.after(2, lambda: self.e2.delete(0, END))
                        self.log_win2.after(2, lambda: self.t3.set(""))
                        self.log_win2.after(3, lambda: self.log_win2.state("iconic"))
                    else:
                        pass
            except Exception:
                messagebox.showerror("ERROR", "Wrong USERNAME/PASSWORD")
                self.e2.delete(0, END)
                self.e3.delete(0, END)
        except Exception as e:
            messagebox.showerror("ERROR","Error in Connection"+str(e), parent=self.log_win2)
    def fac_reset_page(self):
        self.fac = Toplevel()
        self.fac.focus_force()
        self.fac.wm_resizable(0, 0)
        self.fac.title("Factory Reset")
        self.fac.wm_iconbitmap("hospital.ico")
        self.fac.geometry("350x300+550+250")
        self.fac.focus_force()
        img1 = PhotoImage(file="black-background.png")
        canv1 = Canvas(self.fac, highlightbackground="white")
        canv1.pack(expand=YES, fill=BOTH)
        canv1.create_image(0,0,image=img1)
        canv1.image = img1

        canv1.create_text(60, 67, text="User Name", font=("algerian", 15, "bold", "italic"), fill="white")
        self.e1 = Entry(canv1, width=20, bg="white", font=("algerian", 12, "italic", "bold"))
        self.e1.place(x=150, y=55)
        self.e1.focus()

        canv1.create_text(60, 142, text="Password", font=("algerian", 15, "bold", "italic"), fill="white")
        self.e4 = Entry(canv1, width=20, bg="white", font=("algerian", 12, "italic", "bold"), show="*")
        self.e4.place(x=150, y=130)
        self.e4.bind("<Return>", lambda e: self.checklog1())

        btn = Button(canv1, text="Reset App", bd=5, font=("algerian", 15, "bold", "italic")
                     , bg="cyan", fg="black", command=self.checklog1)
        btn.place(x=120, y=200)

    def checklog1(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT type FROM login WHERE username=%s AND password=%s"
                           , (self.e1.get(), self.e4.get()))
                f1 = dc.fetchone()
                for j in f1:
                    if j == "admin":
                        self.fac_reset()
                    elif j == "user":
                        messagebox.showinfo("Access Denied", "Login using Admin Account")
                    else:
                        pass
            except Exception:
                messagebox.showerror("ERROR", "Wrong USERNAME or PASSWORD", parent=self.fac)
                self.e1.delete(0, END)
                self.e4.delete(0, END)
                self.e1.focus()
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.fac)

    def fac_reset(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                # deleting images doc
                dc.execute("SELECT img FROM doctor")
                res = dc.fetchall()
                for i in res:
                    for j in i:
                        path = os.path.join("docimages//", j)
                        os.remove(path)
                        if i != None:
                            continue
                # deleting images pat
                dc.execute("SELECT img FROM patient")
                res = dc.fetchall()
                for i in res:
                    for j in i:
                        path = os.path.join("patimages//", j)
                        os.remove(path)
                        if i != None:
                            continue
                # deleting images nur
                dc.execute("SELECT img FROM nurse")
                res = dc.fetchall()
                for i in res:
                    for j in i:
                        path = os.path.join("nurimages//", j)
                        os.remove(path)
                        if i != None:
                            continue
                dc.execute("DELETE FROM appointment")
                d1.commit()
                dc.execute("DELETE FROM doctor")
                d1.commit()
                dc.execute("DELETE FROM invoicecounter")
                d1.commit()
                dc.execute("DELETE FROM nurse")
                d1.commit()
                dc.execute("DELETE FROM patient")
                d1.commit()
                dc.execute("DELETE FROM payments")
                d1.commit()
                dc.execute("DELETE FROM revisit")
                d1.commit()
                dc.execute("DELETE FROM login")
                d1.commit()
                messagebox.showinfo("RESET", "Data Deleted Successfully", parent=self.fac)
                self.log_win2.destroy()
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e))
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e))

def raincheck():
    try:
        d1 = connect(host="localhost", user="root", password="", db="hospital")
        try:
            dc = d1.cursor()
            dc.execute("SELECT username FROM login")
            f = dc.fetchall()
            if f == ():
                login_win1()
            else:
                login_win2()
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Query" + str(e))
    except Exception as e:
        messagebox.showerror("ERROR", "Error in Connection" + str(e))

if __name__ == '__main__':
    raincheck()