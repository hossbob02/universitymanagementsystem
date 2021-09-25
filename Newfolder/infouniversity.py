
from tkinter import *
from PIL import Image,ImageTk

class Infouni:
    def __init__(self,cf):
        self.universityInfo = Frame(cf, pady=10, padx=10)
        self.universityInfo.grid(row=0, column=0, sticky='senw')
        self.img = Image.open('university.png')
        self.img.thumbnail((200, 200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.universityInfo, image=self.new_img, padx=10, pady=10)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.universityInfo,command=self.openinfowindow, font=('tahoma', 10, 'bold'), text='About University',bg='#1b9ea4', fg='white', padx=10, pady=10)
        self.buttonUniversity.pack()

    def openinfowindow(self):
       info=InfoWindow()



class InfoWindow:
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Info')
        self.master.geometry("1200x800+0+0")
        self.TitleLabel=Label(self.master,text='Faculté Des Sciences De Monastir',bg='#1b9ea4',pady=100,fg='white',font=('Tahoma',30,'bold'))
        self.TitleLabel.pack(fill=X)
        self.txt=StringVar()
        self.Message=Message(self.master,textvariable=self.txt,justify=CENTER,font=('tahoma',10))
        self.Message.pack()
        self.txt.set("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.It has survived not only five centuries, but also the leap into electronic typesetting, \n remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset \n sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus \n PageMaker including versions of Lorem Ipsum.")