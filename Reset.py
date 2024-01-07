import os

from pymysql import *
from tkinter import messagebox

class clear_data:
    def __init__(self):
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
               messagebox.showinfo("RESET", "Data Deleted Successfully")
           except Exception as e:
               messagebox.showerror("ERROR", "Error in creation" + str(e))
       except Exception as e:
           messagebox.showerror("ERROR", "Error in Connection" + str(e))