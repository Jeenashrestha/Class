import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from text_to_speech import speak

class Stories:
    def __init__(self, win):
        self.mainStories = win
        story1Image= PhotoImage(file="images/story1.png")
        story1Lbl = Label(self.mainStories, image=story1Image).place(x=10, y=115)
        story1Title= Label(self.mainStories, text="Lion King", bg="black", fg="white", font=30). place(x=80,y=100)
        desc1= "The Lion King tells the story of Simba,\na young lion who is to succeed his \nfather, Mufasa as King of the Pride Lands."
        story1Description= Label(self.mainStories, text=desc1, fg="white", bg="black", justify= LEFT).place(x=80, y=125)
        play1Btn= Button(self.mainStories, text="Play").place(x=325, y=115)
        downloadBtn = Button(self.mainStories, text="Download").place(x=325, y=150)
        browseStoryBtn = Button(self.mainStories, text = "Browse on computer", font=40, command=self.browseStories).place(x=150, y=300)
        writeStoryBtn = Button(self.mainStories, text="Write your own story", font=40).place(x=150,y=350)

    def browseStories(self):
        Tk().withdraw()
        filename = askopenfilename()
        storyfile= open(filename, "r")
        self.story= storyfile.read()
        self.player= Toplevel()
        self.player.configure(height=500, width=400)
        playerImg= PhotoImage("images/story1.png")
        imageFrame= Frame(self.player, height=400, width=400, bg="black").place(x=0, y=0)
        pauseBtn = Button(self.player, text="Pause").place(x=70, y=450)
        playBtn= Button(self.player, text="Play", command=self.play).place(x=120, y=450)
        stopBtn = Button(self.player, text="Stop").place(x=170, y=450)
        resumeBtn = Button(self.player, text="Resume").place(x=220, y=450)
        replayBtn = Button(self.player, text="Replay").place(x=290, y=450)

    def play(self):
        speak(self.story,'en', save=False)







root= Tk()
root.geometry("414x500")
root.title("Stories")
root.configure(background="black")
root.resizable(False, False)
frame= Stories(root)
root.mainloop()



# contentAppend= "Appended content"
# try:
#     h = open(completeName, "a")
#     h.write(contentAppend)
#     h.close
#
#     print ("*******After appending*******")
#
#     i = open("D:/file/myfile.txt", "r")
#     print(i.read())
#     i.close()
# except:
#     print("error: ", sys.exc_info())
# finally:
#     del filename
#     del path
#
