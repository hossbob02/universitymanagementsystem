from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
import datetime
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
