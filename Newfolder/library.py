from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
import datetime
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
