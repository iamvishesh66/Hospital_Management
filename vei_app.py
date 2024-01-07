from tkinter import *
from pymysql import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox

class vei_app:

    def __init__(self, parent, a, b):
        self.pat_win1 = parent

        self.f1 = Frame(self.pat_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.pat_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="VIEW APPOINTMENT", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)
        # display image
        img1 = PhotoImage(file="appointment_widget.png").subsample(14, 14)
        imglabel = Label(self.f1, borderwidth=2, text="", width=195, height=200,image=img1)
        imglabel.image = img1
        imglabel.place(x=-20, y=-20)

        self.f3 = Frame(self.f1, bg="gray95")
        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)
        self.table = Treeview(self.f3, columns=("id", "name", "gender", "phno", "reasonforvisit", "doctorprovided", "date", "time")
                              , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, height=17)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="NAME")
        self.table.heading("gender", text="GENDER")
        self.table.heading("phno", text="PHONE NUMBER")
        self.table.heading("reasonforvisit", text="REASON FOR VISIT")
        self.table.heading("doctorprovided", text="DOCTOR PROVIDED")
        self.table.heading("date", text="DATE")
        self.table.heading("time", text="TIME")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        self.table.column("#1", stretch=NO, minwidth=50, width=50)
        self.table.column("#2", stretch=NO, minwidth=100, width=100)
        self.table.column("#3", stretch=NO, minwidth=100, width=100)
        self.table.column("#4", stretch=NO, minwidth=110, width=110)
        self.table.column("#5", stretch=NO, minwidth=200, width=200)
        self.table.column("#6", stretch=NO, minwidth=150, width=150)
        self.table.column("#7", stretch=NO, minwidth=120, width=120)
        self.table.column("#8", stretch=NO, minwidth=150, width=150)

        self.table.pack()
        self.f3.place(x=0, y=150)
        self.v1 = StringVar()
        self.onstart()

        # Let's create some labels
        l1 = Label(self.f1, text="Filters", background="gray95", font=("arial", 16)).place(x=200, y=5)
        # Let's create some combobox and entry boxes
        self.t1 = StringVar()
        self.e1 = Entry(self.f1, bg="white", font=("arial", 14, "italic"))
        self.e1.bind("<FocusIn>", lambda e: self.remtext())
        self.e1.bind("<FocusOut>", lambda e: self.deftext())
        self.e1.place(x=600, y=5)
        self.f1.bind("<Enter>", lambda e: self.showtext())

        self.v1.set("Sort By")
        self.c1 = Combobox(self.f1, value=("Name","Ascending Order","Descending Order")
                           , textvariable=self.v1, state="readonly", font=("arial", 14))

        self.c1.place(x=300, y=5)
        # Let's create some buttons
        btn1 = Button(self.f1, text="Apply", font=("arial", 12, "bold"), bd=3, command=self.applyer)
        btn1.place(x=300, y=50)

        btn2 = Button(self.f1, text="Remove", font=("arial", 12, "bold"), bd=3, command=self.onstart)
        btn2.place(x=430, y=50)

        btn3 = Button(self.f1, text="Search", font=("arial", 11, "bold"), bd=3, command=self.searcher)
        btn3.place(x=850, y=0)

        btn4 = Button(self.f1, text="Revisit Records", font=("arial", 11, "bold"), bd=3, command=self.records)
        btn4.place(x=850, y=60)

        btn5 = Button(self.f1, text="Refresh", font=("arial", 11, "bold"), bd=3
                      , command=lambda :vei_app(self.pat_win1, 20, 40), fg="green")
        btn5.place(x=910, y=115)


    def records(self):
        self.a = Toplevel()
        self.a.title("REVISIT INFORMATION")
        self.a.wm_iconbitmap("hospital.ico")
        self.a.geometry("400x300+500+200")
        self.a.focus_force()
        self.l_1 = Label(self.a, text="REVISITING RECORDS!", font=("arial",20,"bold","italic"),fg="orange")
        self.l_1.place(x=50, y=10)

        self.f_1 = Frame(self.a)
        x = Scrollbar(self.f_1, orient=HORIZONTAL)
        y = Scrollbar(self.f_1, orient=VERTICAL)

        self.info = Treeview(self.f_1, columns=("ID","NAME","LIST"), xscrollcommand=x.set, yscrollcommand=y.set)

        x.config(command=self.table.xview)
        x.pack(side=BOTTOM, fill=X)
        y.config(command=self.table.yview)
        y.pack(side=RIGHT, fill=Y)

        self.info.heading("ID",text="ID")
        self.info.heading("NAME",text="NAME")
        self.info.heading("LIST",text="LIST OF DATES PATIENT VISITED")

        self.info.column("#0", stretch=NO, minwidth=0, width=0)
        self.info.column("#1", stretch=NO, minwidth=20, width=20)
        self.info.column("#2", stretch=NO, minwidth=80, width=80)
        self.info.column("#3", stretch=NO, minwidth=250, width=250)

        self.info.pack()
        self.f_1.place(x=20, y=50)
        self.rrs()

        self.a.mainloop()
    def showtext(self):
        if not self.t1.get():
            self.f1.focus_set()
            self.t1.set("Search in Name")
            self.e1.config(textvariable=self.t1, fg="grey")

    def remtext(self):
        if self.t1.get() == "Search in Name":
            self.t1.set("")
        else:
            self.t1.set(self.e1.get())
        self.e1.config(textvariable=self.t1, fg="black", bg="yellow")

    def deftext(self):
        self.e1.config(bg="white")

    def onstart(self):
        try:
            self.v1.set("Sort By")
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM appointment")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pat_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pat_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pat_win1)

    def applyer(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v1.get() == "Name":
                    dc.execute("SELECT * FROM appointment")
                elif self.v1.get() == "Ascending Order":
                    dc.execute("SELECT * FROM appointment ORDER BY id ASC")
                elif self.v1.get() == "Descending Order":
                    dc.execute("SELECT * FROM appointment ORDER BY id DESC")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pat_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pat_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pat_win1)

    def searcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM appointment WHERE name LIKE '%"+str(self.e1.get())+"%'")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pat_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pat_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pat_win1)

    def rrs(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                c = d1.cursor()
                c.execute("SELECT * FROM revisit")
                self.result = c.fetchall()
                for row in self.result:
                    self.info.insert("", END, values=row)
                if not self.result:
                    self.a.destroy()
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.pat_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.pat_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.pat_win1)



def main():
    pass

if __name__ == '__main__':
    main()