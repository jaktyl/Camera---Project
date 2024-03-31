from tkinter import *
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import os.path
from datetime import date
 
class App:
    
    def __init__(self):

        self.mainWindow = tk.Tk()

        self.mainWindow.title('Camera App')

        self.mainWindowIcon = tk.PhotoImage(file='camera.png')

        self.mainWindow.iconphoto(True, self.mainWindowIcon)
        
        self.bg = tk.PhotoImage(file='bg.png')

        self.myLabel=Label(self.mainWindow, image=self.bg)

        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.mainWindow.geometry('1000x700+400+150')

        self.takePhotoButton = Button.setButton(self.mainWindow, 'Take a Photo',  'black', 'white', 'white', 'orange', self.takePhoto, 10, 25, 'Arial' )

        self.displayPhotoCatalogButton = Button.setButton(self.mainWindow, 'Display Photo Catalog',  'black', 'white', 'white', 'blue', self.displayPhotoCatalog, 5, 25, 'Arial' )

        self.takePhotoButton.place(x=40, y=300)

        self.displayPhotoCatalogButton.place(x=40,y=500)

        self.webcamLabel = tk.Label(self.mainWindow)

        self.webcamLabel.place(x= 300, y= 100, height=505, width = 620)

        self.addWebcam(self.webcamLabel)

        self.dataBaseDirectory = './dataBaseDirectory'

        if not os.path.exists(self.dataBaseDirectory):  
            os.mkdir(self.dataBaseDirectory)

    def displayPhotoCatalog(self):
        os.startfile(r'C:\Users\Jakub\Desktop\Camera-project\dataBaseDirectory')

    def takePhoto(self):

        self.takePhotoWindow=tk.Toplevel(self.mainWindow)
        self.takePhotoWindow.geometry('1000x700+400+150')
        
        self.myLabel=Label(self.takePhotoWindow, image=self.bg)

        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.acceptButton = Button.setButton(self.takePhotoWindow, 'Accept',  'black', 'white', 'white', 'green', self.acceptPhoto, 10, 25, 'Arial' )

        self.tryAgainButton = Button.setButton(self.takePhotoWindow, 'Try again',  'black', 'white', 'white', 'red', self.tryAgain, 5, 25, 'Arial' )
        
        self.setDescriptionCaption= tk.Label(self.takePhotoWindow,height=2,width=20, text='Please, enter description:', background='orange')

        self.setDescriptionCaption.config(font=('Arial', 16), justify="center", foreground="white" )

        self.setDescriptionEntry=tk.Text(self.takePhotoWindow, height=4, width=20, font=("Arial", 16), background='orange' ) 

        self.setDescriptionCaption.place(x=40, y=100)

        self.setDescriptionEntry.place(x=40, y=170)

        self.pictureLabel = tk.Label(self.takePhotoWindow)
        self.pictureLabel.place(x= 300, y= 100, height=505, width = 620)

        self.acceptButton.place(x=40, y=300)
        self.tryAgainButton.place(x=40,y=500)

        self.addImageToLabel(self.pictureLabel)

    def addWebcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0) 

        self._label = label 
        self.processWebcam()


    def processWebcam(self):
       
        ret, frame = self.cap.read()
        self.mostRecentCaptureArr = frame

        img = cv2.cvtColor(self.mostRecentCaptureArr, cv2.COLOR_BGR2RGB)
        self.mostRecentCapturePil = Image.fromarray(img)

        imgTk = ImageTk.PhotoImage(image = self.mostRecentCapturePil )

        self._label.imgTk = imgTk

        self._label.configure(image = imgTk)

        self._label.after(20, self.processWebcam)


    def addImageToLabel(self, label):
        imgTk = ImageTk.PhotoImage(image = self.mostRecentCapturePil )
        label.imgTk = imgTk
        label.configure(image = imgTk)

        self.registerNewUserCapture = self.mostRecentCaptureArr.copy()

    def acceptPhoto(self):

        today = date.today()

        description = self.setDescriptionEntry.get(1.0, "end-1c")
        
        cv2.imwrite(os.path.join(self.dataBaseDirectory, '{}-{}.jpg'.format(description,today)), self.registerNewUserCapture) 

        messagebox.showinfo('Succes', 'The photo has been successfully added to the catalog')

        self.takePhotoWindow.destroy()

    def tryAgain(self):

        self.takePhotoWindow.destroy()
   
    def start(self):
       self.mainWindow.mainloop()


class Button:

    def setButton(window, text,  activebackground, activeforeground, fg, bg, command, height, width, font):  #proponuje konstruktor
         button = tk.Button(
                    window,
                    text=text,
                    activebackground=activebackground,
                    activeforeground=activeforeground,
                    fg = fg,
                    bg=bg,
                    command=command,
                    height= height,
                    width=width,
                    font= font
                    )

         return button



if __name__  == "__main__":

    app = App()
    app.start()