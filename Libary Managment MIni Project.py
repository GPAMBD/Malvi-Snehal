from tkinter import *
from tkinter import ttk
import sqlite3
from  tkinter import messagebox
base=Tk()
base.title("Libaray Management System")
base.geometry("1200x680")
f=("Arial",15)
lab1=Label(base,font=("Arial",25),text="   Library Management System  ",bg="dark orange",fg="white",height=1,width=100,anchor="w")
lab1.place(x=0,y=0)
con9 = sqlite3.connect("student.db")
quary = "select * from student_info"
cur = con9.cursor()
cur.execute(quary)
d1 = cur.fetchall()
endr = []
sna=[]
for ls in d1:
    endr.append(ls[0])
    sna.append(ls[1])
bna=[]
bti=[]
allBid=[]
con8 = sqlite3.connect("books.db")
quary2 = "select * from books_info"
cur2 = con8.cursor()
cur2.execute(quary2)
d2 = cur2.fetchall()
for ls1 in d2:
    bna.append(ls1[0])
    allBid.append(ls1[0])
    bti.append(ls1[1])


def addstudent():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Add Student ", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Endrollment No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    l2 = Label(panal1, text="Student Name : ",font=("Arial",13))
    l2.place(x=50, y=120)
    l4 = Label(panal1, text="Email Id : ", font=("Arial", 13))
    l4.place(x=50, y=160)
    l5 = Label(panal1, text="Student Phone : ", font=("Arial", 13))
    l5.place(x=450, y=80)
    l6 = Label(panal1, text="Student Class: ", font=("Arial", 13))
    l6.place(x=450, y=120)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=180, y=80)
    t2 = Entry(panal1, width=25,font=("Arial",13))
    t2.place(x=180, y=120)
    t3 = Entry(panal1, width=25, font=("Arial", 13))
    t3.place(x=180, y=160)
    t4 = Entry(panal1, width=25, font=("Arial", 13))
    t4.place(x=600, y=80)
    state_list = (" - Select - ", "CO-1I", "CO-2I", "CO-3I", "CO-4I", "CO-5I", "CO-6I")
    comb = ttk.Combobox(panal1, width=20, values=state_list, font=("Arial", 13))
    comb.place(x=600, y=120)
    comb.current(0)

    def method1():
        s1=t1.get()
        s2=t2.get()
        s3=t3.get()
        s4=t4.get()
        s5=comb.get()
        con = sqlite3.connect("student.db")
        con.commit()
        q="insert into student_info(enroll, sname, semail, sphone, sclass) values('{0}','{1}','{2}','{3}','{4}')".format(s1,s2,s3,s4,s5)
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Message","Data Saved...")
        print("Data saved...")

    def reset():
        t1.delete(0,END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        comb.current(0)

    b1 = Button(panal1,text=" Add Student ",font=("Arial Bold",14),command=method1)
    b1.place(x=50, y=220)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=reset)
    b2.place(x=240, y=220)

def searchstudent():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text="Search Student", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Endrollment No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=180, y=80)
    def resrt():
        t1.delete(0,END)
    def search():
        s1=t1.get()
        con = sqlite3.connect("student.db")
        quary="select * from student_info"
        cur=con.cursor()
        cur.execute(quary)
        if int(s1) not in endr:
            panal2 = PanedWindow(bd=4, relief="raised", width=900, height=300)
            panal2.place(x=260, y=300)
            l32 = Label(panal2, text="Student Not found....", font=("Arial", 12), fg="red")
            l32.place(x=50, y=30)
        while True:
            d=cur.fetchone()
            if d == None:
                break
            if str(s1)==str(d[0]):
                panal2 = PanedWindow(bd=4, relief="raised", width=900, height=300)
                panal2.place(x=260, y=300)
                l32 = Label(panal2, text="Student found....", font=("Arial",12),fg="red")
                l32.place(x=50, y=30)
                l12 = Label(panal2, text="Endrollment No : ", font=("Arial", 13))
                l12.place(x=50, y=80)
                l22 = Label(panal2, text="Student Name : ", font=("Arial", 13))
                l22.place(x=50, y=120)
                l42 = Label(panal2, text="Email Id : ", font=("Arial", 13))
                l42.place(x=50, y=160)
                l52 = Label(panal2, text="Student Phone : ", font=("Arial", 13))
                l52.place(x=450, y=80)
                l62 = Label(panal2, text="Student Class: ", font=("Arial", 13))
                l62.place(x=450, y=120)
                st1=d[0]
                st2=d[1]
                st3=d[2]
                st4=d[3]
                st5=d[4]
                t12 = Entry(panal2, width=25, font=("Arial", 13))
                t12.place(x=180, y=80)
                t22 = Entry(panal2, width=25, font=("Arial", 13))
                t22.place(x=180, y=120)
                t32 = Entry(panal2, width=25, font=("Arial", 13))
                t32.place(x=180, y=160)
                t42 = Entry(panal2, width=25, font=("Arial", 13))
                t42.place(x=600, y=80)
                t52 = Entry(panal2, width=25, font=("Arial", 13))
                t52.place(x=600, y=120)
                t12.insert(0,st1)
                t22.insert(0,st2)
                t32.insert(0,st3)
                t42.insert(0,st4)
                t52.insert(0,st5)
        con.close()
    b1 = Button(panal1,text=" Search Student ",font=("Arial Bold",14),command=search)
    b1.place(x=50, y=140)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=resrt)
    b2.place(x=260, y=140)

def studenthistroy():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Student History", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Endrollment No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=180, y=80)
    b1 = Button(panal1,text=" Search Student history",font=("Arial Bold",12))
    b1.place(x=50, y=140)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",12))
    b2.place(x=260, y=140)

def removestudent():
    panal1 = PanedWindow(bd=4, relief="raised", width=1000, height=1000)
    panal1.place(x=230, y=47)
    l3 = Label(panal1, text=" Remove Student ", font=("Arial Bold", 20), fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Endrollment No : ", font=("Arial", 13))
    l1.place(x=50, y=80)
    l2 = Label(panal1, text="Student Name : ", font=("Arial", 13))
    l2.place(x=50, y=130)
    t1 = Entry(panal1, width=25, font=("Arial", 13))
    t1.place(x=190, y=80)
    t2 = Entry(panal1, width=25, font=("Arial", 13))
    t2.place(x=190, y=130)
    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
    def remove():
        s1=t1.get()
        s2=t2.get()
        if int(s1) in endr and str(s2) in sna:
            con = sqlite3.connect("student.db")
            cur = con.cursor()
            quary = "DELETE from student_info where enroll='" + s1 + "'"
            cur.execute(quary)
            con.commit()
            messagebox.showinfo("Message", "Data Deleted")
        else:
            messagebox.showinfo("Message","Check your ENROLMENT number")


    b1 = Button(panal1, text=" Remove Student ", font=("Arial Bold", 13),command=remove)
    b1.place(x=50, y=190)
    b2 = Button(panal1, text=" Reset ", font=("Arial Bold", 13),command=reset)
    b2.place(x=270, y=190)

def issuebook():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Issue Book ", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=10)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=60)
    l2 = Label(panal1, text="Book Title : ",font=("Arial",13))
    l2.place(x=50, y=110)
    l4 = Label(panal1, text="Student Endrollment Number : ",font=("Arial",13))
    l4.place(x=450, y=60)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=150, y=60)
    t2 = Entry(panal1, width=25,font=("Arial",13))
    t2.place(x=150, y=110)
    t3 = Entry(panal1, width=25, font=("Arial", 13))
    t3.place(x=680, y=60)
    def issue():

        global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

        bid = t1.get()
        issueto = t2.get()
        con = sqlite3.connect("books.db")
        extractBid = "select s1 from books_info "
        if(bid) in bna and issueto in bti :
            cur.execute(extractBid)
            con.commit()
            for i in cur:
                allBid.append(i[0])

            if bid in allBid:
                checkAvail = "select status from books_info  where bid = '" + bid + "'"
                cur.execute(checkAvail)
                con.commit()
                for i in cur:
                    check = i[0]

                if check == 'avail':
                    status = True
                else:
                    status = False
            else:
                messagebox.showinfo("Error", "Book ID not present")



        issueSql = "insert into  issueTable  values ('" + bid + "','" + issueto + "')"
        show = "select * from  issueTable "

        updateStatus = "update books_info  set status = 'issued' where bid = '" + bid + "'"
        if bid in allBid and status == True:
                cur.execute(issueSql)
                con.commit()
                cur.execute(updateStatus)
                con.commit()
                messagebox.showinfo('Success', "Book Issued Successfully")

        else:
                allBid.clear()
                messagebox.showinfo('Success', "Book Issued Successfully")

                return

        print(bid)
        print(issueto)

        allBid.clear()

    def resert():
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)

    def displybook():
        panal2 = Frame(bd=4, relief=RIDGE, width=900, height=400,bg="crimson")
        panal2.place(x=280, y=260)
        scrollx=Scrollbar(panal2,orient=HORIZONTAL)
        scrolly=Scrollbar(panal2,orient=VERTICAL)
        table=ttk.Treeview(panal2,columns=("bnum","bnam","baut","btyp","byer"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=table.xview)
        scrolly.config(command=table.yview)
        table.heading("bnum",text="Book No")
        table.heading("bnam", text="Book Title")
        table.heading("baut", text="Book Author")
        table.heading("btyp", text="Book Type")
        table.heading("byer", text="Publish Year")
        table['show']='headings'
        table.column("bnum",width=150)
        table.column("bnam", width=150)
        table.column("baut", width=200)
        table.column("btyp", width=200)
        table.column("byer", width=150)
        table.pack(fill=BOTH,expand=2)
    b1 = Button(panal1,text=" Issue Book ",font=("Arial Bold",14),command=issue)
    b1.place(x=50, y=160)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=resert)
    b2.place(x=200, y=160)
    b3 = Button(panal1, text=" Display Books ", font=("Arial Bold", 14),command=displybook)
    b3.place(x=300, y=160)

def returnbook():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Return Book ", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    l2 = Label(panal1, text="Book Title : ",font=("Arial",13))
    l2.place(x=50, y=130)
    l4 = Label(panal1, text="Student Endrollment Number : ", font=("Arial", 13))
    l4.place(x=450, y=60)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=150, y=80)
    t2 = Entry(panal1, width=25,font=("Arial",13))
    t2.place(x=150, y=130)
    t3 = Entry(panal1, width=25, font=("Arial", 13))
    t3.place(x=680, y=60)
    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
    def retur():
        s1=t1.get()
        s2=t1.get()
        s3=t3.get()
    b1 = Button(panal1,text=" Return Book ",font=("Arial Bold",14))
    b1.place(x=50, y=190)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=reset)
    b2.place(x=220, y=190)

def addbook():
    global books_info
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Add New book to Libaray ", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    l2 = Label(panal1, text="Book Name : ",font=("Arial",13))
    l2.place(x=50, y=120)
    l4 = Label(panal1, text="Author Name : ", font=("Arial", 13))
    l4.place(x=50, y=160)
    l5 = Label(panal1, text="Book Type : ", font=("Arial", 13))
    l5.place(x=450, y=80)
    l6 = Label(panal1, text="Book Publish Year: ", font=("Arial", 13))
    l6.place(x=450, y=120)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=180, y=80)
    t2 = Entry(panal1, width=25,font=("Arial",13))
    t2.place(x=180, y=120)
    t3 = Entry(panal1, width=25, font=("Arial", 13))
    t3.place(x=180, y=160)
    booktype = (" - Select - ", "Coading Book", "Theory Book", "Novel", "Motivational Book", "Reference Book", "Conceptual Book","Action and Adventure book","Basic Starting Book","Suspense Book","Anthology")
    comb1 = ttk.Combobox(panal1, width=25, values=booktype, font=("Arial", 13))
    comb1.place(x=630, y=80)
    comb1.current(0)
    state_list = (" - Select - ", "2020", "2019", "2018", "2017", "2016", "2015")
    comb = ttk.Combobox(panal1, width=25, values=state_list, font=("Arial", 13))
    comb.place(x=630, y=120)
    comb.current(0)

    def method1():
        s1=t1.get()
        s2=t2.get()
        s3=t3.get()
        s4=str(comb1.get())
        s5=str(comb.get())
        con = sqlite3.connect("books.db")
        q = "insert into  books_info   values ('"+s1+"','"+s2+"','"+s3+"','"+s4+"','"+s5+"')"
        con.execute(q)
        con.commit()
        con.close()
        messagebox.showinfo("Message" , " Data Saved...")
        print("Data saved...")

    def reset():
        t1.delete(0,END)
        t2.delete(0, END)
        t3.delete(0, END)
        comb.current(0)
        comb1.current(0)
    b1 = Button(panal1,text=" Add Book ",font=("Arial Bold",14),command=method1)
    b1.place(x=50, y=220)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=reset)
    b2.place(x=240, y=220)

def searchbook():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text="Search Book", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=150, y=80)

    def reset():
        t1.delete(0, END)
    def search():
        s1=t1.get()
        if int(s1) not in bna:
            panal2 = PanedWindow(bd=4, relief="raised", width=900, height=300)
            panal2.place(x=260, y=300)
            l32 = Label(panal2, text="Book Not found....", font=("Arial", 12), fg="red")
            l32.place(x=50, y=30)
        con = sqlite3.connect("books.db")
        quary="select * from books_info"
        cur=con.cursor()
        cur.execute(quary)
        while True:
            d21=cur.fetchone()
            if d21 == None:
                break
            if str(s1)==str(d21[0]):
                panal2 = PanedWindow(bd=4, relief="raised", width=900, height=300)
                panal2.place(x=260, y=300)
                l32 = Label(panal2, text="Book found....", font=("Arial",12),fg="red")
                l32.place(x=50, y=30)
                l12 = Label(panal2, text="Book Number : ", font=("Arial", 13))
                l12.place(x=50, y=80)
                l22 = Label(panal2, text="Book Title : ", font=("Arial", 13))
                l22.place(x=50, y=120)
                l42 = Label(panal2, text="Author Name : ", font=("Arial", 13))
                l42.place(x=50, y=160)
                l52 = Label(panal2, text="Book Type : ", font=("Arial", 13))
                l52.place(x=450, y=80)
                l62 = Label(panal2, text="Book Publish Year: ", font=("Arial", 13))
                l62.place(x=450, y=120)
                st1=d21[0]
                st2=d21[1]
                st3=d21[2]
                st4=d21[3]
                st5=d21[4]
                t12 = Entry(panal2, width=25, font=("Arial", 13))
                t12.place(x=180, y=80)
                t22 = Entry(panal2, width=25, font=("Arial", 13))
                t22.place(x=180, y=120)
                t32 = Entry(panal2, width=25, font=("Arial", 13))
                t32.place(x=180, y=160)
                t42 = Entry(panal2, width=25, font=("Arial", 13))
                t42.place(x=600, y=80)
                t52 = Entry(panal2, width=25, font=("Arial", 13))
                t52.place(x=600, y=120)
                t12.insert(0,st1)
                t22.insert(0,st2)
                t32.insert(0,st3)
                t42.insert(0,st4)
                t52.insert(0,st5)
        con.close()
    b1 = Button(panal1,text=" Search Book ",font=("Arial Bold",14),command=search)
    b1.place(x=50, y=140)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=reset)
    b2.place(x=220, y=140)

def removebook():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Remove Book", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    l2 = Label(panal1, text="Book Title : ",font=("Arial",13))
    l2.place(x=50, y=130)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=150, y=80)
    t2 = Entry(panal1, width=25,font=("Arial",13))
    t2.place(x=150, y=130)
    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
    def remove1():
        s1=t1.get()
        s2=t2.get()
        if int(s1) in bna and str(s2) in bti:
            con1 = sqlite3.connect("books.db")
            quary = "DELETE from books_info where b_num='" + s1 + "'"
            cur = con1.cursor()
            cur.execute(quary)
            con1.commit()
            messagebox.showinfo("Message", "Book Removed.")

        else:
            messagebox.showinfo("Message","Check your book number and title")

    b1 = Button(panal1,text=" Remove Book ",font=("Arial Bold",14),command=remove1)
    b1.place(x=50, y=190)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14),command=reset)
    b2.place(x=220, y=190)

def bookhistory():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text="Book History"  , font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Book No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=150, y=80)
    b1 = Button(panal1,text=" Search Book History ",font=("Arial Bold",12))
    b1.place(x=50, y=140)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",12))
    b2.place(x=260, y=140)

def notreturnbook():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Not Return Book ", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    l1 = Label(panal1, text="Endrollment No : ",font=("Arial",13))
    l1.place(x=50, y=80)
    t1 = Entry(panal1, width=25,font=("Arial",13))
    t1.place(x=200, y=80)
    b1 = Button(panal1,text=" Search  ",font=("Arial Bold",14))
    b1.place(x=50, y=130)
    b2 = Button(panal1,text=" Reset ",font=("Arial Bold",14))
    b2.place(x=220, y=130)

def sendreminder():
    panal1=PanedWindow(bd=4,relief="raised",width=1000,height=1000)
    panal1.place(x=230,y=47)
    l3 = Label(panal1, text=" Send Reminder to send for Return the Book", font=("Arial Bold", 20),fg="magenta2")
    l3.place(x=50, y=30)
    b2 = Button(panal1,text=" Send ",font=("Arial Bold",14))
    b2.place(x=50, y=80)

def exit():
    base.destroy()
lab2=Button(base,text="Add Student ",font=f,bg="orange",fg="black",height=1,width=20,command=addstudent)
lab2.place(x=0,y=47)
lab3=Button(base,text="Search Student ",font=f,bg="orange",fg="black",height=1,width=20,command=searchstudent)
lab3.place(x=0,y=90)
lab4=Button(base,text="Student History ",font=f,bg="orange",fg="black",height=1,width=20,command=studenthistroy)
lab4.place(x=0,y=133)
lab5=Button(base,text="Remove Student ",font=f,bg="orange",fg="black",height=1,width=20,command=removestudent)
lab5.place(x=0,y=176)
lab6=Button(base,text="Issue Book ",font=f,bg="orange",fg="black",height=1,width=20,command=issuebook)
lab6.place(x=0,y=219)
lab7=Button(base,text="Return Book ",font=f,bg="orange",fg="black",height=1,width=20,command=returnbook)
lab7.place(x=0,y=262)
lab8=Button(base,text="Add Book ",font=f,bg="orange",fg="black",height=1,width=20,command=addbook)
lab8.place(x=0,y=305)
lab9=Button(base,text="Search Book ",font=f,bg="orange",fg="black",height=1,width=20,command=searchbook)
lab9.place(x=0,y=348)
lab10=Button(base,text="Remove Book",font=f,bg="orange",fg="black",height=1,width=20,command=removebook)
lab10.place(x=0,y=391)
lab11=Button(base,text="Book History ",font=f,bg="orange",fg="black",height=1,width=20,command=bookhistory)
lab11.place(x=0,y=434)
lab12=Button(base,text="Not Return Books",font=f,bg="orange",fg="black",height=1,width=20,command=notreturnbook)
lab12.place(x=0,y=477)
lab13=Button(base,text="Send Return Reminders",font=f,bg="orange",fg="black",height=1,width=20,command=sendreminder)
lab13.place(x=0,y=520)
lab14=Button(base,text=" Exit ",font=f,bg="orange",fg="black",height=1,width=20,command=exit)
lab14.place(x=0,y=563)

lab15=Label(base,text=" Welcome to Libary Managment System ",font=("Arial Bold",16),bg="black",fg="IndianRed1",height=2,width=40)
lab15.place(x=300,y=200)
#print(endr)
#print(type(sna[0]))
base.mainloop(