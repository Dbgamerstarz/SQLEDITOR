#tkinter and sql
import tkinter as tk
from tkinter import *
import sqlite3
#connect to db and make cursor for actions
class sqlstuff():
    def __init__(self):
        self.sql=sqlite3.connect("data.db")
        self.c=self.sql.cursor()
        self.rows=[]
        self.res = self.sql.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #
        
        self.tables=[]
        for name in self.res:
            print(name[0])
            self.tables.append(name[0])
        self.change()
    def run(self):
        cursor = self.sql.execute('select * from '+self.table)
        self.names = [description[0] for description in cursor.description]
        print(self.names)
        
    def close(self):
        self.sql.close()#close database
    def create_table(self):
        name=input(">")
        data=input("data>")
        self.c.execute("CREATE TABLE "+name+data)#create table
        self.sql.commit()#commit changes
        
    def read_table(self):
        self.rows=[]
        for row in self.c.execute("SELECT * FROM "+self.table):
            
            self.rows.append(row)
        showall()
    def change(self):
        ii=tk.Tk()
        for f in self.tables:
            print(f)
            tk.Label(ii,text=f).pack()
        tk.Label(ii,text="Enter table to use:").pack()
        self.ent=tk.Entry(ii)
        self.ent.pack()
        
        tk.Button(ii,text="Save",command=self.changed).pack()
        
    def changed(self):
        self.table=self.ent.get()
        print(self.table)
        self.run()
##    def add_things(self):
##        inp=input("Movie:")
##        ip=input("Sales:")
##        self.c.execute("INSERT INTO stuff VALUES(?,?)",(inp,ip))
##        self.sql.commit()
    def delete(self):
        ii=tk.Tk()
        tk.Label(ii,text="Movie:").pack()
        self.ent=tk.Entry(ii)
        self.ent.pack()
        tk.Button(ii,text="Save",command=self.deleteit).pack()
    def add_things(self):
        ii=tk.Tk()
        tk.Label(ii,text="Movie:").pack()
        self.ent=tk.Entry(ii)
        self.ent.pack()
        tk.Label(ii,text="Sales (bn $):").pack()
        self.ent2=tk.Entry(ii)
        self.ent2.pack()
        tk.Button(ii,text="Save",command=self.saveit).pack()
    def saveit(self):
        mov=self.ent.get()
        sal=self.ent2.get()
        self.c.execute("INSERT INTO "+self.table+" VALUES(?,?)",(mov,sal))
        self.sql.commit()
    def deleteit(self):
        mov=self.ent.get()
        
        self.c.execute("DELETE FROM "+self.table+" WHERE movie=?",(mov,))
        self.sql.commit()
root=tk.Tk()
s=sqlstuff()
stuff=[]
def showall():
    tf.t.delete("1.0","end")
    showrest()

def showrest():
    pp=""
    for n in s.names:
        pp=pp+n+"   "
    s.rows.insert(0,pp)
    n=0
    for st in s.rows:
        if n==0:
             tf.t.insert("1.0",st+"\n")
             tf.t.insert(END,"__________________________\n")
       
        else:
            tf.t.insert(END,st[0]+"  "+st[1]+"\n")
        n+=1
class tkb():
    def __init__(self,master):
        self.t=tk.Text(master)
        self.t.pack()

        self.menu=tk.Menu(master)
        fmenu=tk.Menu(self.menu)
        fmenu.add_command(label="Read",command=s.read_table)
        fmenu.add_command(label="Add",command=s.add_things)
        fmenu.add_command(label="Delete",command=s.delete)
        fmenu.add_command(label="Change Table",command=s.change)
        fmenu.add_command(label="Create",command=s.create_table)
##        fmenu.add_command(label="Close",command=s.close)
        self.menu.add_cascade(label="Commands",menu=fmenu)
tf=tkb(root)
root.config(menu=tf.menu)
root.mainloop()
