from tkinter.ttk import Combobox
from pymysql import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import time

class add_app:

    def __init__(self, parent, a, b):

        self.revisit = []

        self.doc_win1 = parent

        self.f1 = Frame(self.doc_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.doc_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="SCHEDULE APPOINTMENT", font=("algerian",20,"bold","underline"), fg="dodger blue3"
                      , bg="white").place(x=350,y=0)

        l1 = Label(self.f1, text="Id", background="gray95", font=("arial", 16)).place(x=0, y=5)
        l2 = Label(self.f1, text="Name", background="gray95", font=("arial", 16)).place(x=0, y=70)
        l3 = Label(self.f1, text="Gender", background="gray95", font=("arial", 16)).place(x=0, y=120)
        l4 = Label(self.f1, text="Phone Number", background="gray95", font=("arial", 16)).place(x=0, y=170)
        l5 = Label(self.f1, text="Reason for visit", background="gray95", font=("arial", 16)).place(x=0, y=220)
        l6 = Label(self.f1, text="Date", background="gray95", font=("arial", 16)).place(x=0, y=320)
        l7 = Label(self.f1, text="Time", background="gray95", font=("arial", 16)).place(x=0, y=390)
        l8 = Label(self.f1, text="Doctor Provided", background="gray95", font=("arial", 16)).place(x=0, y=450)

        self.t1 = StringVar()
        self.t2 = StringVar()
        self.t3 = StringVar()
        self.t4 = StringVar()
        self.t5 = StringVar()

        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.e1 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext("e1"))
        self.e1.bind("<FocusOut>", lambda e: self.deftext("e1"))
        self.e1.bind("<Down>", lambda e: self.lower("e1"))
        self.e1.bind("<Up>", lambda e: self.up("e1"))
        self.e1.place(x=200, y=5)

        # calling on start func
        self.onstart()


        self.e2 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e2.bind("<FocusIn>", lambda e: self.remtext("e2"))
        self.e2.bind("<FocusOut>", lambda e: self.deftext("e2"))
        self.e2.bind("<Down>", lambda e: self.lower("e2"))
        self.e2.bind("<Up>", lambda e: self.up("e2"))
        self.e2.place(x=200, y=70)

        self.e3 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e3.bind("<FocusIn>", lambda e: self.remtext("e3"))
        self.e3.bind("<FocusOut>", lambda e: self.deftext("e3"))
        self.e3.bind("<Down>", lambda e: self.lower("e3"))
        self.e3.bind("<Up>", lambda e: self.up("e3"))
        self.e3.place(x=200, y=170)

        self.e4 = Text(self.f1, width=20, height=3, bg="white", font=("arial", 14, "italic"))
        self.e4.bind("<FocusIn>", lambda e: self.remtext("e4"))
        self.e4.bind("<FocusOut>", lambda e: self.deftext("e4"))
        self.e4.bind("<Down>", lambda e: self.lower("e4"))
        self.e4.bind("<Up>", lambda e: self.up("e4"))
        self.e4.place(x=200, y=220)

        self.e5 = DateEntry(self.f1, width=50, font=("arial", 12,"italic"), normalbackground="white"
                            , normalforeground="dodger blue3", background="dodger blue3", foreground="white")
        self.e5.bind("<Down>", lambda e: self.lower("e5"))
        self.e5.bind("<Up>", lambda e: self.up("e5"))
        self.e5.place(x=200, y=320)

        self.e6 = Entry(self.f1, width=50, bg="white", font=("arial", 14, "italic"))
        self.e6.bind("<FocusIn>", lambda e: self.remtext("e6"))
        self.e6.bind("<FocusOut>", lambda e: self.deftext("e6"))
        self.e6.bind("<Down>", lambda e: self.lower("e6"))
        self.e6.bind("<Up>", lambda e: self.up("e6"))
        self.e6.place(x=200, y=390)

        self.v1 = StringVar()
        self.v1.set(" ")

        self.r1 = Radiobutton(self.f1, text="Male", variable=self.v1, value="Male", font=("arial", 14))
        self.r1.place(x=200, y=120)
        self.r2 = Radiobutton(self.f1, text="Female", variable=self.v1, value="Female", font=("arial", 14))
        self.r2.place(x=400, y=120)

        self.v2 = StringVar()
        self.v2.set("Choose Speciality")

        self.doc_list1 = []
        self.doc_list = []
        self.fetch_doc()

        self.c1 = Combobox(self.f1, value=self.doc_list1, textvariable=self.v2, state="readonly",
                           font=("arial", 14, "italic"))
        self.c1.bind("<<ComboboxSelected>>",lambda e: self.fetcher())
        self.c1.place(x=200, y=450)

        self.btn1 = Button(self.f1, text="SCHEDULE", command=self.savedata, font=("arial",14,"bold"), bd=5)
        self.btn1.place(x=700, y=500)

        self.btn2 = Button(self.f1, text="REFRESH", command=lambda :add_app(self.doc_win1, 20, 40), font=("arial", 14, "bold"), bd=5)
        self.btn2.place(x=850, y=500)

        self.f1.mainloop()

    def showtext(self):

        # if not self.t1.get():
        #     self.f1.focus_set()
        #     self.t1.set("Enter Unique Id")
        #     self.e1.config(textvariable=self.t1, fg="grey")
        if not self.t2.get():
            self.f1.focus_set()
            self.t2.set("Enter Patient's Name")
            self.e2.config(textvariable=self.t2, fg="grey")
        if not self.t3.get():
            self.f1.focus_set()
            self.t3.set("Enter Patient's Phone Number")
            self.e3.config(textvariable=self.t3, fg="grey")
        if not self.t4.get():
            self.f1.focus_set()
            self.t4.set("Select Date")
            self.e5.config(textvariable=self.t4)
        if not self.t5.get():
            self.f1.focus_set()
            self.t5.set(str(time.ctime()))
            self.e6.config(textvariable=self.t5, fg="grey")

    def remtext(self, name):

        # if name == "e1":
        #     if self.t1.get() == "Enter Unique Id":
        #         self.t1.set("")
        #     else:
        #         self.t1.set(self.e1.get())
        #     self.e1.config(textvariable=self.t1, fg="black", bg="yellow")
        if name == "e2":
            if self.t2.get() == "Enter Patient's Name":
                self.t2.set("")
            else:
                self.t2.set(self.e2.get())
            self.e2.config(textvariable=self.t2, fg="black", bg="yellow")
        elif name == "e3":
            if self.t3.get() == "Enter Patient's Phone Number":
                self.t3.set("")
            else:
                self.t3.set(self.e3.get())
            self.e3.config(textvariable=self.t3, fg="black", bg="yellow")
        elif name == "e4":
            self.e4.config(fg="black", bg="yellow")
        elif name == "e6":
            if self.t5.get() == str(time.ctime()):
                self.t5.set("")
            else:
                self.t5.set(self.e6.get())
            self.e6.config(textvariable=self.t5, fg="black", bg="yellow")

    def deftext(self, name):

        if name == "e1":
            self.e1.config(bg="white")
        elif name == "e2":
            self.e2.config(bg="white")
        elif name == "e3":
            self.e3.config(bg="white")
        elif name == "e4":
            self.e4.config(bg="white")
        elif name == "e6":
            self.e6.config(bg="white")

    def lower(self, name):

        if name == "e1":
            self.e2.focus_set()
        elif name == "e2":
            self.e3.focus_set()
        elif name == "e3":
            self.e4.focus_set()
        elif name == "e4":
            self.e5.focus_set()
        elif name == "e5":
            self.e6.focus_set()
        elif name == "e6":
            self.e1.focus_set()

    def up(self, name):

        if name == "e1":
            self.e6.focus_set()
        elif name == "e2":
            self.e1.focus_set()
        elif name == "e3":
            self.e2.focus_set()
        elif name == "e4":
            self.e3.focus_set()
        elif name == "e5":
            self.e4.focus_set()
        elif name == "e6":
            self.e5.focus_set()

    def savedata(self):
        self.revisit.append(self.e5.get())

        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc1 = d1.cursor()
                dc.execute("INSERT INTO appointment VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(self.e1.get(),self.e2.get(),self.v1.get()
                                                                                  ,self.e3.get(),self.e4.get("1.0", END)
                                                                                   ,self.v3.get(),self.e5.get_date()
                                                                                   ,self.e6.get()))
                d1.commit()
                dc1.execute("INSERT INTO revisit VALUES(%s,%s,%s)",(self.e1.get(),self.e2.get(), self.revisit[0]))
                d1.commit()
                messagebox.showinfo("SAVE", "Appointment Saved Successfully", parent=self.doc_win1)
                add_app(self.doc_win1, 20, 40)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def fetch_doc(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT speciality FROM doctor")
                f = dc.fetchall()
                for i in f:
                    for j in i:
                        self.doc_list1.append(j)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def fetcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT name FROM doctor where speciality=%s",self.v2.get())
                f = dc.fetchall()
                for i in f:
                    for j in i:
                        self.doc_list.append(j)
                self.v3 = StringVar()
                self.v3.set("Choose Doctor")

                self.c2 = Combobox(self.f1, value=self.doc_list, textvariable=self.v3, state="readonly",
                                   font=("arial", 14, "italic"))
                self.c2.place(x=600, y=450)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def onstart(self):
        try:
            current_id = 0
            var = IntVar()
            d1 = connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT id FROM appointment")
                f = dc.fetchall()
                for i in f:
                    for j in i:
                        current_id = j
                current_id += 1
                self.e1.config(textvariable=var, state="disabled")
                var.set(current_id)
            except Exception:
                self.e1.config(textvariable=var, state="disabled")
                var.set(1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)




def main():
    pass


if __name__ == '__main__':
    main()