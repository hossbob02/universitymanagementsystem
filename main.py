import datetime
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkcalendar import Calendar

class Infouni:
    def __init__(self, cf):
        self.universityInfo = Frame(cf, pady=10, padx=10)
        self.universityInfo.grid(row=0, column=0, sticky='senw')
        self.img = Image.open('university.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.universityInfo, image=self.new_img, padx=10, pady=10)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.universityInfo, command=self.openinfowindow, font=('tahoma', 10, 'bold'),
                                       text='About University', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonUniversity.pack()

    def openinfowindow(self):
        info = InfoWindow()


class InfoWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Info')
        self.master.geometry("1200x800+0+0")
        self.TitleLabel = Label(self.master, text='Faculté Des Sciences De Monastir', bg='#1b9ea4', pady=100,
                                fg='white', font=('Tahoma', 30, 'bold'))
        self.TitleLabel.pack(fill=X)
        self.txt = StringVar()
        self.Message = Message(self.master, textvariable=self.txt, justify=CENTER, font=('tahoma', 10))
        self.Message.pack()
        self.txt.set(
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.")


class Staff:
    def __init__(self, cf):
        self.staffFrame = Frame(cf, pady=10, padx=10)
        self.staffFrame.grid(row=0, column=2, sticky='senw')
        self.img3 = Image.open('staff.png')
        self.img3.thumbnail((200, 200))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.staffFrame, image=self.new_img3, padx=10, pady=10)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.staffFrame, command=self.openstaffwindow, font=('tahoma', 10, 'bold'),
                                  text='Staff Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonStaff.pack()

    def openstaffwindow(self):
        stdw = StaffWindow()


class StaffWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Staff Management System')
        self.master.geometry("1200x600+0+0")
        #########################################################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.firstName = Label(self.frameleft, text='Firstname:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.firstName.place(x=10, y=20, width=100, height=40)
        self.lastName = Label(self.frameleft, text='Lastname:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.lastName.place(x=10, y=70, width=100, height=40)
        self.CIN = Label(self.frameleft, text='CIN:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.CIN.place(x=10, y=120, width=100, height=40)
        self.Email = Label(self.frameleft, text='Email:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Email.place(x=10, y=170, width=100, height=40)
        self.Phone = Label(self.frameleft, text='Phone:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Phone.place(x=10, y=220, width=100, height=40)
        self.Job = Label(self.frameleft, text='Job:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.Job.place(x=10, y=290, width=100, height=40)
        self.name = StringVar()
        self.last = StringVar()
        self.email = StringVar()
        self.cin = StringVar()
        self.phone = StringVar()
        self.job = StringVar()
        self.firstNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.name)
        self.firstNameEntry.place(x=120, y=20, width=200, height=40)
        self.lastNameEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.last)
        self.lastNameEntry.place(x=120, y=70, width=200, height=40)
        self.CINentry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.cin)
        self.CINentry.place(x=120, y=120, width=200, height=40)
        self.EmailEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.email)
        self.EmailEntry.place(x=120, y=170, width=200, height=40)
        self.PhoneEntry = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.PhoneEntry.place(x=120, y=220, width=200, height=40)
        self.JobEntry = ttk.Combobox(self.frameleft, values=["", "Employee", "Professor", "Technician"],
                                     state='readonly', textvariable=self.job)
        self.JobEntry.place(x=120, y=290, width=200, height=40)

        self.buttonAdd = Button(self.frameleft, text="ADD", command=self.add, font=('tahoma', 10, 'bold'))
        self.buttonAdd.place(x=20, y=400, width=60, height=60)
        self.buttonUpdate = Button(self.frameleft, command=self.update, text="UPDATE", font=('tahoma', 10, 'bold'))
        self.buttonUpdate.place(x=100, y=400, width=60, height=60)
        self.buttonDelete = Button(self.frameleft, command=self.delete, text="DELETE", font=('tahoma', 10, 'bold'))
        self.buttonDelete.place(x=180, y=400, width=60, height=60)
        self.buttonRead = Button(self.frameleft, command=self.read, text="SHOW", font=('tahoma', 10, 'bold'))
        self.buttonRead.place(x=260, y=400, width=60, height=60)
        self.buttonReset = Button(self.frameleft, command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        self.buttonReset.place(x=340, y=400, width=60, height=60)

        ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)
        ############################# right frame end here ######################"""

        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)

        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop, command=self.search, text='Search', fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView = Frame(self.frameright, bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar = Scrollbar(self.frameView, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameView,
                                  columns=("ID", "Firstname", "Lastname", "CIN", "Email", "Phone", "Job"),
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("CIN", text="CIN")
        self.table.heading("Email", text="Email")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Job", text="Job")

        self.table.column("ID", anchor=W, width=7)
        self.table.column("Firstname", anchor=W, width=60)
        self.table.column("Lastname", anchor=W, width=60)
        self.table.column("CIN", anchor=W, width=60)
        self.table.column("Email", anchor=W, width=60)
        self.table.column("Phone", anchor=W)
        self.table.column("Job", anchor=W)
        self.read()
        self.table.bind("<ButtonRelease>", self.show)

    def add(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = "insert into staff(Firstname,Lastname,CIN,Email,Phone,Job) values (%s,%s,%s,%s,%s,%s)"
        if (len(self.firstNameEntry.get()) == 0 or len(self.PhoneEntry.get()) == 0 or len(
                self.JobEntry.get()) == 0 or len(self.lastNameEntry.get()) == 0 or len(self.CINentry.get()) == 0 or len(
                self.EmailEntry.get()) == 0):
            mb.showerror('Error', 'all data should be required')
        else:
            val = (self.firstNameEntry.get(), self.lastNameEntry.get(), self.CINentry.get(), self.EmailEntry.get(),
                   self.PhoneEntry.get(), self.JobEntry.get())
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully', parent=self.master)
            self.reset()
            self.read()

    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = "select * from staff"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for res in myresults:
            self.table.insert('', 'end', iid=res[0], values=res)
            mydb.commit()
        mydb.close()

    def show(self, ev):
        self.iid = self.table.focus()
        alldata = self.table.item(self.iid)
        val = alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.email.set(val[4])
        self.phone.set(val[5])
        self.job.set(val[6])

    def reset(self):
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.CINentry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.PhoneEntry.delete(0, 'end')
        self.JobEntry.current(0)

    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from staff where id=" + self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete', 'this student deleted', parent=self.master)
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
        sql = ("update staff set Firstname=%s,Lastname=%s,CIN=%s,Email=%s,Phone=%s,Job=%s where id=%s")
        val = (
        self.name.get(), self.last.get(), self.cin.get(), self.email.get(), self.phone.get(), self.job.get(), self.iid)
        mycursor.execute(sql, val)
        mydb.commit()
        mb.showinfo('update', 'this student is updated', parent=self.master)
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
        sql = ("select * from staff where id=" + self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        # print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()

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

class Library:
    def __init__(self,bf):
        self.libraryFrame = Frame(bf, pady=10, padx=50)
        self.libraryFrame.grid(row=1, column=0, sticky='senw')
        self.img4 = Image.open('open-book.png')
        self.img4.thumbnail((200, 200))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image=self.new_img4, padx=10, pady=10)
        self.imgLibrary.pack()

        self.buttonLibrary = Button(self.libraryFrame, command=self.openlibrarywindow, font=('tahoma', 10, 'bold'),
                                    text='Library Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonLibrary.pack()
    def openlibrarywindow(self):
        lib = LibraryWindow()

class LibraryWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.iconbitmap('swim_ring_icon_183313.ico')
        self.master.title('Library Management System')
        self.master.geometry("1200x800+0+0")
        #########################################################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.nameLabel=Label(self.frameleft,text='Student Name:',fg='#4F4F4F',font=('tahoma',12,'bold'))
        self.nameLabel.place(x=15,y=20,width=120,height=40)
        self.phoneLabel = Label(self.frameleft, text='Phone:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.phoneLabel.place(x=10, y=80, width=120, height=40)
        self.NameBookLabel = Label(self.frameleft, text='Book Name:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.NameBookLabel.place(x=10, y=140, width=120, height=40)
        self.datedLabel = Label(self.frameleft, text='Delivery Date:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.datedLabel.place(x=15, y=200, width=120, height=40)
        self.daterLabel = Label(self.frameleft, text='Return Date:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.daterLabel.place(x=15, y=450, width=120, height=40)
        self.name=StringVar()
        self.phone = StringVar()
        self.book = StringVar()
        self.delivery=StringVar()
        self.returnn = StringVar()


        self.nameStudent = Entry(self.frameleft,fg='#4F4F4F',font=('tahoma',12,'bold'),textvariable=self.name)
        self.nameStudent.place(x=170,y=20,width=200,height=40)
        self.phoneStudent = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.phone)
        self.phoneStudent.place(x=170, y=80, width=200, height=40)
        self.bookname = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.book)
        self.bookname.place(x=170, y=140, width=200, height=40)
        self.DeliveryDate=Calendar(self.frameleft,year = 2021,textvariable=self.delivery,mindate=datetime.date.today())
        self.DeliveryDate.place(x=170, y=200,width=200,height=200)
        self.ReturnDate = Calendar(self.frameleft,year = 2021,textvariable=self.returnn)
        self.ReturnDate.place(x=170, y=450, width=200, height=200)



        self.buttonAdd=Button(self.frameleft,text="ADD", command=self.add ,font=('tahoma',10,'bold'))
        self.buttonAdd.place(x=20,y=700,width=60,height=60)
        self.buttonUpdate = Button(self.frameleft,command=self.update, text="UPDATE",font=('tahoma',10,'bold'))
        self.buttonUpdate.place(x=100, y=700,width=60,height=60)
        self.buttonDelete = Button(self.frameleft,command=self.delete, text="DELETE",font=('tahoma',10,'bold'))
        self.buttonDelete.place(x=180, y=700,width=60,height=60)
        self.buttonRead = Button(self.frameleft, command=self.read, text="SHOW", font=('tahoma', 10, 'bold'))
        self.buttonRead.place(x=260, y=700, width=60, height=60)
        self.buttonReset = Button(self.frameleft,command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        self.buttonReset.place(x=340, y=700, width=60, height=60)






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
        self.table=ttk.Treeview(self.frameView,columns=("ID","Name","Phone","Book","Delivery Date","Return Date"),show='headings',yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Phone", text="Phone")
        self.table.heading("Book", text="Book")
        self.table.heading("Delivery Date", text="Delivery Date")
        self.table.heading("Return Date", text="Return Date")

        self.table.column("ID", anchor=W,width=7)
        self.table.column("Name", anchor=W)
        self.table.column("Phone",anchor=W)
        self.table.column("Book", anchor=W)
        self.table.column("Delivery Date",anchor=W)
        self.table.column("Return Date",anchor=W)
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
        sql="insert into library(Studentname,Phone,Book,DeliveryDate,ReturnDate) values (%s,%s,%s,%s,%s)"
        if (len(self.nameStudent.get())==0 or len(self.phoneStudent.get())==0 or len(self.bookname.get())==0 or len(self.DeliveryDate.get_date())==0 or  len(self.ReturnDate.get_date())==0 ) :
            mb.showerror('Error', 'all data should be required')
        else:
            val=(self.nameStudent.get(),self.phoneStudent.get(),self.bookname.get(),self.DeliveryDate.get_date(),self.ReturnDate.get_date())
            mycursor.execute(sql,val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully',parent=self.master)
            self.nameStudent.delete(0,'end')
            self.phoneStudent.delete(0, 'end')
            self.bookname.delete(0, 'end')
            self.DeliveryDate.selection_clear()
            self.ReturnDate.selection_clear()
            self.read()
    def read(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor=mydb.cursor()
        sql="select * from library"
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
        self.phone.set(val[2])
        self.book.set(val[3])
        self.delivery.set(val[4])
        self.returnn.set(val[5])
    def reset(self):
        self.nameStudent.delete(0, 'end')
        self.phoneStudent.delete(0, 'end')
        self.bookname.delete(0, 'end')
        self.DeliveryDate.selection_clear()
        self.ReturnDate.selection_clear()


    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from library where id="+self.iid)
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
        sql = ("update library set Studentname=%s,Phone=%s,Book=%s,DeliveryDate=%s,ReturnDate=%s where id=%s")
        val=(self.name.get(),self.phone.get(),self.book.get(),self.DeliveryDate.get_date(),self.ReturnDate.get_date(),self.iid)
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
        sql = ("select * from library where id="+self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        #print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()

class Exam:
    def __init__(self,bf):
        self.examFrame = Frame(bf, pady=10, padx=50)
        self.examFrame.grid(row=1, column=1, sticky='senw')
        self.img5 = Image.open('exam.png')
        self.img5.thumbnail((200, 200))
        self.new_img5 = ImageTk.PhotoImage(self.img5)
        self.imgExam = Label(self.examFrame, image=self.new_img5, padx=10, pady=10)
        self.imgExam.pack()
        self.buttonExam = Button(self.examFrame, command=self.openExamWindow, font=('tahoma', 10, 'bold'),
                                 text='Exam Management', bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonExam.pack()

    def openExamWindow(self):
        lib = ExamWindow()


class ExamWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.iconbitmap('swim_ring_icon_183313.ico')
        self.master.title('Exam Management System')
        self.master.geometry("1200x800+0+0")
        #########################################################
        self.frameleft = Frame(self.master, width=400)
        self.frameleft.pack(side=LEFT, fill=BOTH)
        #########################################################
        self.nameLabel = Label(self.frameleft, text='Name of Group:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.nameLabel.place(x=15, y=20, width=120, height=40)
        self.phoneLabel = Label(self.frameleft, text='ClassRoom:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.phoneLabel.place(x=10, y=80, width=120, height=40)
        self.NameBookLabel = Label(self.frameleft, text='Professor:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.NameBookLabel.place(x=10, y=140, width=120, height=40)
        self.datedLabel = Label(self.frameleft, text='Date:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.datedLabel.place(x=15, y=200, width=120, height=40)
        self.daterLabel = Label(self.frameleft, text='Time:', fg='#4F4F4F', font=('tahoma', 12, 'bold'))
        self.daterLabel.place(x=15, y=430, width=120, height=40)
        self.group = StringVar()
        self.classe = StringVar()
        self.professor = StringVar()
        self.dexam = StringVar()
        self.timeExam=StringVar()

        self.GroupName = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.group)
        self.GroupName.place(x=170, y=20, width=200, height=40)
        self.classRoom = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.classe)
        self.classRoom.place(x=170, y=80, width=200, height=40)
        self.Professor = Entry(self.frameleft, fg='#4F4F4F', font=('tahoma', 12, 'bold'), textvariable=self.professor)
        self.Professor.place(x=170, y=140, width=200, height=40)
        self.DateExam = Calendar(self.frameleft, year=2021, textvariable=self.dexam,
                                     mindate=datetime.date.today())
        self.DateExam.place(x=170, y=200, width=200, height=200)
        self.TimeEntry = ttk.Combobox(self.frameleft, values=["", "8:00", "9:00", "10:00","11:00","12:00","14:00","15:00","16:00","17:00"],
                                     state='readonly', textvariable=self.timeExam)
        self.TimeEntry.place(x=170, y=450, width=200)

        self.buttonAdd = Button(self.frameleft, text="ADD", command=self.add, font=('tahoma', 10, 'bold'))
        self.buttonAdd.place(x=20, y=700, width=60, height=60)
        self.buttonUpdate = Button(self.frameleft, command=self.update, text="UPDATE", font=('tahoma', 10, 'bold'))
        self.buttonUpdate.place(x=100, y=700, width=60, height=60)
        self.buttonDelete = Button(self.frameleft, command=self.delete, text="DELETE", font=('tahoma', 10, 'bold'))
        self.buttonDelete.place(x=180, y=700, width=60, height=60)
        self.buttonRead = Button(self.frameleft, command=self.read, text="SHOW", font=('tahoma', 10, 'bold'))
        self.buttonRead.place(x=260, y=700, width=60, height=60)
        self.buttonReset = Button(self.frameleft, command=self.reset, text="RESET", font=('tahoma', 10, 'bold'))
        self.buttonReset.place(x=340, y=700, width=60, height=60)

        ############################# right frame start here ######################"""
        self.frameright = Frame(self.master, width=800)
        self.frameright.pack(side=LEFT, fill=Y)
        ############################# right frame end here ######################"""

        self.framerighttop = Frame(self.frameright, height=50, pady=5, padx=5)

        self.searchstudent = Entry(self.framerighttop, fg='#4F4F4F', font=('tahoma', 12, 'bold'), width=110)
        self.searchstudent.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.framerighttop, command=self.search, text='Search', fg='#4F4F4F',
                                   font=('tahoma', 12, 'bold'), width=50)
        self.buttonsearch.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)

        self.framerighttop.grid_columnconfigure(0, weight=1)
        self.framerighttop.grid_columnconfigure(1, weight=1)

        self.framerighttop.pack(fill=X)

        ################################# Frame Tree View ######################################"

        self.frameView = Frame(self.frameright, bg='blue')
        self.frameView.pack(fill=Y)
        self.scrollbar = Scrollbar(self.frameView, orient=VERTICAL)
        self.table = ttk.Treeview(self.frameView,
                                  columns=("ID","GroupeName","ClassRoom","Professor","Date Exam","Time"),
                                  show='headings', yscrollcommand=self.scrollbar.set,height=300)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("ID", text="ID")
        self.table.heading("GroupeName", text="GroupeName")
        self.table.heading("ClassRoom", text="ClassRoom")
        self.table.heading("Professor", text="Professor")
        self.table.heading("Date Exam", text="Date Exam")
        self.table.heading("Time", text="Time")

        self.table.column("ID", anchor=W, width=7)
        self.table.column("GroupeName", anchor=W,width=100)
        self.table.column("ClassRoom", anchor=W,width=100)
        self.table.column("Professor", anchor=W,width=100)
        self.table.column("Date Exam", anchor=W,width=100)
        self.table.column("Time", anchor=W)
        self.read()
        self.table.bind("<ButtonRelease-1>", self.show)

    def add(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = "insert into Exam(GroupName,ClassRoom,Professor,DateExam,Time) values (%s,%s,%s,%s,%s)"
        if (len(self.GroupName.get()) == 0 or len(self.classRoom.get()) == 0 or len(
                self.Professor.get()) == 0 or len(self.DateExam.get_date()) == 0 or len(
                self.timeExam.get()) == 0):
            mb.showerror('Error', 'all data should be required')
        else:
            val = (self.GroupName.get(), self.classRoom.get(), self.Professor.get(), self.DateExam.get_date(),
                   self.timeExam.get())
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            mb.showinfo('Successfully added', 'Data inserted Successfully', parent=self.master)
            self.reset()
            self.read()

    def read(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='university'
            )
            mycursor = mydb.cursor()
            sql = "select * from Exam"
            mycursor.execute(sql)
            myresults = mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for res in myresults:
                self.table.insert('', 'end', iid=res[0], values=res)
                mydb.commit()
            mydb.close()
        except:
            mb.showerror('Failed connection', 'please open your xampp server')
    def show(self, ev):
        self.iid = self.table.focus()
        alldata = self.table.item(self.iid)
        val = alldata['values']
        self.group.set(val[1])
        self.classe.set(val[2])
        self.professor.set(val[3])
        self.dexam.set(val[4])
        self.timeExam.set(val[5])

    def reset(self):
        self.GroupName.delete(0, 'end')
        self.classRoom.delete(0, 'end')
        self.Professor.delete(0, 'end')
        self.DateExam.selection_clear()
        self.TimeEntry.current(0)

    def delete(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
        )
        mycursor = mydb.cursor()
        sql = ("delete from Exam where id=" + self.iid)
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete', 'this student deleted', parent=self.master)
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
        sql = ("update Exam set GroupName=%s,ClassRoom=%s,Professor=%s,DateExam=%s,Time=%s where id=%s")
        val = (
        self.group.get(), self.classe.get(), self.professor.get(), self.DateExam.get_date(), self.timeExam.get(),
        self.iid)
        mycursor.execute(sql, val)
        mydb.commit()
        mb.showinfo('update', 'this student is updated', parent=self.master)
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
        sql = ("select * from Exam where id=" + self.searchstudent.get())
        mycursor.execute(sql)
        myresults = mycursor.fetchone()
        self.table.delete(*self.table.get_children())
        # print(myresults)
        self.table.insert('', 'end', iid=myresults[0], values=myresults)
        mydb.commit()
        mydb.close()


class University:
    def __init__(self, window):
        self.master = window
        self.master.title("University Management System")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width, h=self.height))
        self.master.state('zoomed')
        ################# Frame Top Start Here ########################
        self.frametop = Frame(self.master, bg='#1b9ea4', height=150)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop, text='University Management System', bg='#1b9ea4', fg='white',
                         font=('tahoma', 50), pady=50)
        self.sms.pack()
        self.buttonLogout = Button(self.frametop, text='logout', command=self.logout)
        self.buttonLogout.pack()
        ################# Frame Top End Here ##########################

        ################# Frame Center Start Here ########################

        self.centerFrame = Frame(self.master)
        self.centerFrame.pack(fill=X)
        ######Frame University info #####
        inf = Infouni(self.centerFrame)
        ##### Frame Student Frame ####
        std = Student(self.centerFrame)
        #####Frame Staff info ######
        stf = Staff(self.centerFrame)

        ################# Frame Center End Here ########################

        ################# Bottom Frame Start Here ########################
        self.bottomFrame = Frame(self.master, height=200)
        self.bottomFrame.pack(fill=X)
        ####### Library Frame ######
        lib = Library(self.bottomFrame)
        ######### Exam Frame ########
        exa = Exam(self.bottomFrame)
        ################# Bottom Frame End Here ########################
        self.centerFrame.grid_columnconfigure(0, weight=1)
        self.centerFrame.grid_columnconfigure(1, weight=1)
        self.centerFrame.grid_columnconfigure(2, weight=1)

        self.bottomFrame.grid_columnconfigure(0, weight=1)
        self.bottomFrame.grid_columnconfigure(1, weight=1)

    def logout(self):
        self.master.destroy()


class Login:
    def __init__(self, window):
        self.master = window
        self.master.title("Login System")
        self.master.geometry("500x500+150+150")
        self.img = Image.open('loginImage.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgStudent = Label(self.master, image=self.new_img)
        self.imgStudent.pack()
        self.frameLogin = Frame(self.master)
        self.frameLogin.pack()
        self.labelUser = Label(self.frameLogin, text='Username', pady=10, padx=10, font=('tahoma', 10, 'bold'))
        self.labelUser.grid(row=0, column=0)
        self.labelPass = Label(self.frameLogin, text='Password', pady=10, padx=10, font=('tahoma', 10, 'bold'))
        self.labelPass.grid(row=1, column=0)
        self.username = Entry(self.frameLogin, font=('tahoma', 10, 'bold'))
        self.username.grid(row=0, column=1, pady=10, padx=10)
        self.password = Entry(self.frameLogin, font=('tahoma', 10, 'bold'), show="*")
        self.password.grid(row=1, column=1, pady=10, padx=10)
        self.LoginButton = Button(self.frameLogin, command=self.login, text='Login', font=('tahoma', 10, 'bold'),
                                  bg='#1b9ea4', fg='white', cursor='cross')
        self.LoginButton.grid(row=2, column=0, columnspan=2, sticky='snew', pady=10, padx=10)

    def login(self):
            mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
            )

            mycursor = mydb.cursor()
            sql = "select * from loginadmin where Username='" + self.username.get() + "' and Password='" + self.password.get() + "'"
            mycursor.execute(sql)
            res = mycursor.fetchone()
            if (res == None):
                mb.showerror('Failed Login', 'Invalid Username and Password ! please Try again')
            else:
                win = Toplevel()
                win.iconbitmap('swim_ring_icon_183313.ico')
                window = University(win)









if (__name__ == '__main__'):
    window = Tk()
    window.iconbitmap('swim_ring_icon_183313.ico')
    std = Login(window)

    mainloop()
