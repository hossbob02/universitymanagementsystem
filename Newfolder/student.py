from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
class Student:
    def __init__(self,cf):
        self.studentFrame = Frame(cf, pady=10, padx=10)
        self.studentFrame.grid(row=0, column=1, sticky='senw')
        self.img2 = Image.open('studenticon.png')
        self.img2.thumbnail((200, 200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.studentFrame, image=self.new_img2, padx=10, pady=10)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.studentFrame, command=self.openstudentwindow, font=('tahoma', 10, 'bold'),text='Student Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonStudent.pack()


    def openstudentwindow(self):
       stdw=StudentWindow()


class StudentWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.master.geometry("1200x600+0+0")
        #########################################################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.firstName=Label(self.frameleft,text='Firstname:',fg='#4F4F4F',font=('tahoma',12,'bold'))
        self.firstName.place(x=10,y=20,width=100,height=40)
        self.lastName = Label(self.frameleft, text='Lastname:',fg='#4F4F4F',font=('tahoma',12,'bold'))
        self.lastName.place(x=10,y=70,width=100,height=40)
        self.CIN = Label(self.frameleft, text='CIN:',fg='#4F4F4F',font=('tahoma',12,'bold'))
        self.CIN.place(x=10,y=120,width=100,height=40)
        self.Email = Label(self.frameleft, text='Email:',fg='#4F4F4F',font=('tahoma',12,'bold'))
        self.Email.place(x=10,y=170,width=100,height=40)
        self.name=StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.cin = StringVar()

        self.firstNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.name)
        self.firstNameEntry.place(x=120,y=20,width=200,height=40)
        self.lastNameEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.last)
        self.lastNameEntry.place(x=120,y=70,width=200,height=40)
        self.CINentry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.cin)
        self.CINentry.place(x=120,y=120,width=200,height=40)
        self.EmailEntry = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.email)
        self.EmailEntry.place(x=120,y=170,width=200,height=40)



        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.add ,font=('tahoma',10,'bold'))
        self.buttonAdd.place(x=20,y=300,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10,'bold'))
        self.buttonUpdate.place(x=100, y=300,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10,'bold'))
        self.buttonDelete.place(x=180, y=300,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.read, text="SHOW", font=('tahoma', 10, 'bold'))
        self.buttonRead.place(x=260, y=300, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        self.buttonReset.place(x=340, y=300, width=60, height=60)






    ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)
    ############################# right frame end here ######################"""

        self.framerighttop=Frame(self.frameright,height=50,pady=5,padx=5)


        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop,command=self.search, text='Search', fg='#4F4F4F', font=('tahoma', 12, 'bold'),width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView=Frame(self.frameright,bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar=Scrollbar(self.frameView,orient=VERTICAL)
        self.table=ttk.Treeview(self.frameView,columns=("ID","Firstname","Lastname","CIN","Email"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("Firstname", anchor=W)
        self.table.column("Lastname",anchor=W)
        self.table.column("CIN",anchor=W)
        self.table.column("Email",anchor=W)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)
    def add(self):
        mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="insert into student(Firstname,Lastname,CIN,Email) values (%s,%s,%s,%s)"
        if (len(self.firstNameEntry.get())==0 or len(self.lastNameEntry.get())==0 or len(self.CINentry.get())==0 or len(self.EmailEntry.get())==0 ) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.firstNameEntry.get(),self.lastNameEntry.get(),self.CINentry.get(),self.EmailEntry.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.firstNameEntry.delete(0,'end')
            self.lastNameEntry.delete(0, 'end')
            self.CINentry.delete(0, 'end')
            self.EmailEntry.delete(0, 'end')
            self.read()
    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from student"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('','end',iid=res[0],values=res)
            mydb.commit()
        mydb.close()
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
    def reset(self):
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.CINentry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')

    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from student where id="+self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete','this student deleted',parent=self.master)
        self.read()
        self.reset()
    def update(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("update student set Firstname=%s,Lastname=%s,CIN=%s,Email=%s where id=%s")
        val=(self.name.get(),self.last.get(),self.cin.get(),self.email.get(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update','this student is updated',parent=self.master)
        self.read()
        self.reset()
    def search(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        print(self.searchstudent.get())
        sql = ("select * from student where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        #print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()







