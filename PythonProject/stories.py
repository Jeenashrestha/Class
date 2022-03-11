import sys
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk
from text_to_speech import *

class Stories:
    def __init__(self, win):
        self.mainStories = win
        load = Image.open("images/story1.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.mainStories, image=render)
        img.image = render
        img.place(x=10, y=110)
        story1Title= Label(self.mainStories, text="Lion King", bg="black", fg="white", font=30). place(x=80,y=100)
        desc1= "The Lion King tells the story of Simba,\na young lion who is to succeed his \nfather, Mufasa as King of the Pride Lands."
        story1Description= Label(self.mainStories, text=desc1, fg="white", bg="black", justify= LEFT).place(x=80, y=125)
        play1Btn= Button(self.mainStories, text="Play", command=self.playLionKing).place(x=325, y=130)
        #downloadBtn = Button(self.mainStories, text="Download", command=self.download).place(x=325, y=150)
        browseStoryBtn = Button(self.mainStories, text = "Browse on computer", font=40, command=self.browseStories).place(x=150, y=300)
        writeStoryBtn = Button(self.mainStories, text="Write your own story", font=40, command=self.writeStory).place(x=150,y=350)


    # def loadPlayer(self):
    #     self.player= Toplevel()
    #     self.player.configure(height=500, width=400)
    #     bg = PhotoImage(file="D:/PythonClass/Class/PythonProject/images/calculator.png")
    #     label1 = Label(self.player, text="MP3",bg="black", fg="White", font=200)
    #     label1.place(x=100, y=100)
    #     self.playBtn= Button(self.player, text="Play", command=self.play).place(x=120, y=450)
    #     self.stopBtn = Button(self.player, text="Close", command=self.stop).place(x=170, y=450)


    def browseStories(self):
        Tk().withdraw()
        filename = askopenfilename()
        storyfile = open(filename, "r")
        if storyfile is None:
            return
        else:
            self.story = storyfile.read()
            self.play()

    def writeStory(self):
        storyWin= Toplevel()
        storyWin.configure(bg="black", width=414, height=500)
        writeLbl= Label(storyWin, text="Write your story", bg= "Black", fg="pink", font=40).place(x=10, y=10)
        self.storytextArea= Text(storyWin, width=40, height=10)
        self.storytextArea.place(x=40,y=50)
        saveTextBtn = Button(storyWin, text="Save As Text", command=self.saveText). place(x=100, y= 300)
        play = Button(storyWin, text="Play", command=self.playWritten).place(x=200, y=300)
        saveAudioBtn = Button(storyWin, text="Save As Audio", command=self.saveAudio). place(x=250, y= 300)


    def playWritten(self):
        self.story=self.storytextArea.get("1.0", "end-1c")
        self.play()

    def saveAudio(self):
       self.story= self.storytextArea.get("1.0", "end-1c")
       speak(self.story, "en", save=True)

    def saveText(self):
        try:
            story=self.storytextArea.get("1.0", "end")
            storyFile = asksaveasfile(mode='w', defaultextension=".txt")
            if storyFile is None:
                return
            text2save = str(story)
            storyFile.write(text2save)
            storyFile.close()

        except:
           messagebox.showinfo("Error",sys.exc_info()[0])

    def play(self):
        try:
            speak(self.story, "en", save=False)
        except:
           messagebox.showinfo("Error", "No text to read")

    def stop(self):
        self.player.destroy()

    def playLionKing(self):
        storyfile = open("D:/file/lion.txt", "r")
        self.story = storyfile.read()
        self.play()









root= Tk()
root.geometry("414x500")
root.title("Stories")
root.configure(background="black")
root.resizable(False, False)
frame= Stories(root)
root.mainloop()




