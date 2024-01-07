from tkinter import *
from pymysql import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox

class vei_doc:

    def __init__(self, parent, a, b):
        self.doc_win1 = parent

        self.f1 = Frame(self.doc_win1, height=600, width=1000, bg="gray95")
        self.f1.place(x=a, y=b)
        self.f1.focus()

        self.f2 = Frame(self.doc_win1, height=40, width=1000, bg="white")
        self.f2.place(x=20, y=-7)

        title = Label(self.f2, text="VIEW DOCTOR", font=("algerian", 20, "bold", "underline"), fg="dodger blue3"
                      , bg="white").place(x=350, y=0)
        # label to display image
        self.imglabel = Label(self.f1, borderwidth=2, text="", width=195, height=200)
        self.imglabel.place(x=-10, y=-10)
        # lets create photo adder:
        self.canvas2 = Canvas(self.f1, height=160, width=170, bg="gray95", highlightbackground="gray95")
        self.canvas2.place(x=-10, y=-10)
        self.canvas2.create_oval(155, 155, 12, 12, fill="white", outline="black")

        self.img1 = PhotoImage(file="add_img.png").subsample(6, 6)

        self.canvas2.create_image(70, 60, image=self.img1)
        self.canvas2.create_text(85, 120, text="Select To See\n    Image", font=("arial", 12, "italic", "bold"))

        self.f3 = Frame(self.f1, bg="gray95")
        sc_x = Scrollbar(self.f3, orient=HORIZONTAL)
        sc_y = Scrollbar(self.f3, orient=VERTICAL)
        self.table = Treeview(self.f3, columns=("id", "name", "gender", "phno", "address", "speciality", "wing")
                              , xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, height=17)

        sc_x.config(command=self.table.xview)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.config(command=self.table.yview)
        sc_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="NAME")
        self.table.heading("gender", text="GENDER")
        self.table.heading("phno", text="PHONE NUMBER")
        self.table.heading("address", text="ADDRESS")
        self.table.heading("speciality", text="SPECIALITY")
        self.table.heading("wing", text="WING")
        self.table["show"] = "headings"

        self.table.column("#0", stretch=NO, minwidth=0, width=0)
        self.table.column("#1", stretch=NO, minwidth=70, width=70)
        self.table.column("#2", stretch=NO, minwidth=150, width=150)
        self.table.column("#3", stretch=NO, minwidth=150, width=150)
        self.table.column("#4", stretch=NO, minwidth=150, width=150)
        self.table.column("#5", stretch=NO, minwidth=150, width=150)
        self.table.column("#6", stretch=NO, minwidth=150, width=150)
        self.table.column("#7", stretch=NO, minwidth=160, width=160)

        self.table.bind("<ButtonRelease>", lambda e: self.inserter())

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

        btn4 = Button(self.f1, text="Refresh", font=("arial", 11, "bold"), bd=3
                      , command=lambda: vei_doc(self.doc_win1, 20, 40), fg="green")
        btn4.place(x=910, y=115)

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
                dc.execute("SELECT * FROM doctor")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.doc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def applyer(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                if self.v1.get() == "Name":
                    dc.execute("SELECT * FROM doctor")
                elif self.v1.get() == "Ascending Order":
                    dc.execute("SELECT * FROM doctor ORDER BY id ASC")
                elif self.v1.get() == "Descending Order":
                    dc.execute("SELECT * FROM doctor ORDER BY id DESC")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.doc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def searcher(self):
        try:
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT * FROM doctor WHERE name LIKE '%"+str(self.e1.get())+"%'")
                result = dc.fetchall()
                self.table.delete(*self.table.get_children())
                for row in result:
                    self.table.insert("", END, values=row)
                if not result:
                    messagebox.showinfo("INFO", "NO DATA FOUND", parent=self.doc_win1)
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)

    def inserter(self):
        try:
            currentItem = self.table.focus()
            contents = self.table.item(currentItem)
            selectedRow = contents['values']
            id = selectedRow[0]
            d1 = Connect(host="localhost", user="root", password="", db="hospital")
            try:
                dc = d1.cursor()
                dc.execute("SELECT img FROM doctor WHERE id=%s",id)
                res = dc.fetchone()
                for i in res:
                    self.del_img = i
                tkimage = PhotoImage(file="docimages//" + str(self.del_img))
                a = tkimage.height()
                b = tkimage.width()
                if a > 1000 and b > 1000:
                    p1 = tkimage.subsample(15, 15)
                    self.imglabel.config(image=p1)
                    self.imglabel.image = p1
                elif (a > 1000 and b < 1000) or (a < 1000 and b > 1000):
                    p2 = tkimage.subsample(10, 10)
                    self.imglabel.config(image=p2)
                    self.imglabel.image = p2
                elif (a > 500 and a < 1000) and (b > 500 and b < 1000):
                    p3 = tkimage.subsample(5, 5)
                    self.imglabel.config(image=p3)
                    self.imglabel.image = p3
                elif a < 500 and b < 500:
                    p4 = tkimage.subsample(2, 2)
                    self.imglabel.config(image=p4)
                    self.imglabel.image = p4
                else:
                    self.imglabel.config(image=tkimage)
                    self.imglabel.image = tkimage

                t1 = Label(self.f1, text="Doctor's Photo", font=("arial",10,"bold","italic","underline"),fg="purple").place(x=10,y=0)
                self.canvas2.destroy()
            except Exception as e:
                messagebox.showerror("ERROR", "Error in creation" + str(e), parent=self.doc_win1)
        except Exception as e:
            messagebox.showerror("ERROR", "Error in Connection" + str(e), parent=self.doc_win1)



def main():
    pass

if __name__ == '__main__':
    main()