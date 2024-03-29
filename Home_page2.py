from tkinter import *
from tkinter.messagebox import *

from Home_page_mainframe2 import MainFrame
from Quick_navigation_panel2 import navigator
from add_appointment import add_app
from add_patient import add_pat
from calculator import calculator
from delete_appointment import del_app
from delete_patient import del_pat
from upd_app import upd_app
from upd_pat import upd_pat
from vei_app import vei_app
from vei_doc import vei_doc
from vei_nur import vei_nur
from vei_pat import vei_pat
from payments import bill_desk

class Homepage:

    def __init__(self):
        self.home = Toplevel()
        self.home.focus_force()
        self.home.title("HOSPITAL MANAGEMENT SYSTEMS")

        maxheight = self.home.winfo_screenheight()
        maxwidth = self.home.winfo_screenwidth()
        self.home.geometry("%dx%d+%d+%d" % (maxwidth - 15, maxheight - 15, 0, 0))
        # self.home.wm_minsize(maxwidth,maxheight)
        # it will only work if given after config window size
        self.home.wm_iconbitmap("hospital.ico")
        c1 = Canvas(self.home,width=300, height=200, bg='white')
        c1.pack(expand=YES, fill=BOTH)


        self.frame_a = Frame(c1, height=maxheight, width=300, bg="grey")
        self.frame_a.place(x=0, y=80)

        self.frame_b = Frame(c1, height=maxheight, width=maxwidth-300, bg="white")
        self.frame_b.place(x=300, y=80)

        logo = PhotoImage(file="name.png").subsample(4,4)
        img1 = PhotoImage(file="logout.png").subsample(4,4)
        c1.create_image(170, 40, image=logo)

        main_menu = Menu(self.home)

        self.home.config(menu=main_menu)
        self.home.option_add("*tearOff",False)

        hom = Menu(main_menu)
        pat = Menu(main_menu)
        apm = Menu(main_menu)
        pay = Menu(main_menu)
        viw = Menu(main_menu)
        log = Menu(main_menu)
        qui = Menu(main_menu)

        main_menu.add_cascade(label="HOME", menu=hom)
        main_menu.add_cascade(label="PATIENT", menu=pat)
        main_menu.add_cascade(label="APPOINTMENT", menu=apm)
        main_menu.add_cascade(label="PAYMENT", menu=pay)
        main_menu.add_cascade(label="VIEW", menu=viw)
        main_menu.add_cascade(label="ACCOUNT", menu=log)
        main_menu.add_cascade(label="QUIT", menu=qui)

        # add,remove,update images
        img_1 = PhotoImage(file="add.png").subsample(20,20)
        img_2 = PhotoImage(file="update.png").subsample(100,100)
        img_3 = PhotoImage(file="delete.png").subsample(20,20)
        img_4 = PhotoImage(file="cal.png").subsample(6, 6)
        img_5 = PhotoImage(file="bill.png").subsample(15, 15)
        img_6 = PhotoImage(file="view.png").subsample(10, 10)
        dashboard = PhotoImage(file="dashboard.png").subsample(9,9)

        # setting default as homepage
        MainFrame(self.frame_b, 20, 40)
        navigator(self.frame_a, self.frame_b, self.home)

        # adding commands to home
        hom.add_command(label="  Homepage", image=dashboard, compound=LEFT, command= lambda : MainFrame(self.frame_b, 20, 40))
        # adding commands to patients
        pat.add_command(label="Add Patients", image=img_1, compound=LEFT, command=lambda: add_pat(self.frame_b, 20, 40))
        pat.add_command(label="Update Patients", image=img_2, compound=LEFT,command=lambda: upd_pat(self.frame_b, 20, 40))
        pat.add_command(label="Remove Patient", image=img_3, compound=LEFT, command=lambda: del_pat(self.frame_b, 20, 40))
        # adding commands to appointments
        apm.add_command(label="Add Appointment", image=img_1, compound=LEFT, command=lambda: add_app(self.frame_b, 20, 40))
        apm.add_command(label="Update Appointment", image=img_2, compound=LEFT, command=lambda: upd_app(self.frame_b, 20, 40))
        apm.add_command(label="Cancel Appointment", image=img_3, compound=LEFT, command=lambda: del_app(self.frame_b, 20, 40))
        # adding commands to payments
        pay.add_command(label="Open Calculator", image=img_4, compound=LEFT, command=lambda: calculator(self.frame_b, 20, 40))
        pay.add_command(label="Billing Desk", image=img_5, compound=LEFT, command=lambda: bill_desk(self.frame_b, 20, 40))
        # adding commands to view
        viw.add_command(label="View Doctors", image=img_6, compound=LEFT, command=lambda: vei_doc(self.frame_b, 20, 40))
        viw.add_command(label="View Nurses", image=img_6, compound=LEFT, command=lambda: vei_nur(self.frame_b, 20, 40))
        viw.add_command(label="View Appointments", image=img_6, compound=LEFT, command=lambda: vei_app(self.frame_b, 20, 40))
        viw.add_command(label="View Patients", image=img_6, compound=LEFT, command=lambda: vei_pat(self.frame_b, 20, 40))
        # adding commands to account
        log.add_command(label="Sign Out", image=img1, compound=LEFT, command=lambda :self.sign_out())
        # adding commands to quit
        qui.add_command(label="Quit", image=img1, compound=LEFT, command=lambda :self.quitter())



        self.home.mainloop()
    def quitter(self):
        a = askquestion("QUIT APPLICATION","ARE YOU SURE YOU WANT TO QUIT")
        if a == 'yes':
            self.home.destroy()
        else:
            pass

    def sign_out(self):
        a = askquestion("SIGN OUT", "ARE YOU SURE YOU WANT TO SIGN OUT")
        if a == 'yes':
            self.home.destroy()
            self.home.tk_focusPrev()
        else:
            self.home.focus_force()

def main():
    Homepage()


if __name__ == '__main__':
    main()
