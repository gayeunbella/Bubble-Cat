import Image
from tkinter import *
from time import *
from PIL import Image, ImageTk
from random import *
#from mathproblems import mathlist
root = Tk()
root.geometry("270x480")
root.title('hannaxia')
s = Canvas(root, width = 270, height = 480, bg='#FFF7EB')
s.pack(fill = BOTH, expand=True)

bg = ImageTk.PhotoImage(file = 'image/bg.png')
logo = ImageTk.PhotoImage(file = 'image/logo.png')
s.create_image(130, 140, image = (logo), anchor= CENTER)

def home():
	global startBtn, HTPBtn
	
	startBtn = Button(root, text = "Start", command = game, bg="#93AAE8", font="Arial 10", anchor = CENTER)
	startBtn.pack()
	startBtn.place(x=135, y=300,height=21,width=150,anchor=CENTER)

	HTPBtn = Button(root, text = "How to Play", command = howToPlay, bg="#DB889F", font="Arial 10", anchor = CENTER)
	HTPBtn.pack()
	HTPBtn.place(x=135, y=270,height=21,width=150,anchor=CENTER)

	#design
	wave3 = s.create_polygon(-50, 435, 0, 435, 75, 450, 125, 400, 155, 380, 200, 360, 280, 380, 400, 380, -50, 450, smooth = True, fill = "#516ab0")
	wave1 = s.create_polygon(-100, 400, 0, 600, 300, 480, 350, 450, 135, 400, 60, 380, smooth = TRUE, fill = "#93AAE8")
	wave2 = s.create_polygon(-100, 350, 0, 600, 300, 480, 350, 330, 75, 450, smooth = TRUE, fill = "#627ABD")

	bubble1 = s.create_oval(0, 400, 50, 450, fill = "", outline = "white")


def howToPlay():
	global startBtn, HTPBtn
	s.delete("all")
	startBtn.destroy()
	HTPBtn.destroy()

	wave3 = s.create_polygon(-50, 435, 0, 435, 75, 450, 125, 400, 155, 380, 200, 360, 280, 380, 400, 380, -50, 450, smooth = True, fill = "#516ab0")
	wave1 = s.create_polygon(-100, 400, 0, 600, 300, 480, 350, 450, 135, 400, 60, 380, smooth = TRUE, fill = "#93AAE8")
	wave2 = s.create_polygon(-100, 350, 0, 600, 300, 480, 350, 330, 75, 450, smooth = TRUE, fill = "#627ABD")

	HTPtab = s.create_polygon(30, 100, 30, 250, 240, 250, 240, 100, fill = "white", outline = "black")
	HTPobjective = s.create_text(135, 115, text = "objective", font = "arial 20", anchor = CENTER, fill = "black")
	HTPobjectiveText = s.create_text(40, 135, text = "The objective of the game is to pop as \nmany bubbles as possible! \n\nWhen you select a bubble, a fun math \nproblem will appear. Once you've \nsolved the problem correctly, the bubble \nwill pop. \n\n As you pop more bubbles, a mystery cat\n will reward you!", anchor = NW, fill = "black", font = "arial 7")
	#HTPpointform1 = s.create_oval()
  
	WEPtab = s.create_polygon(40, 270, 230, 270, 230, 320, 40, 320, fill = "white", outline = "black")
	WEPtext = s.create_text(50, 280, text = "Bubble Cat will motivate you into \npracticing math - - because we recognize \nthe struggles of high school math.", font = "arial 6", fill = "black", anchor = NW)

	WCTtab = s.create_polygon(40, 350, 230, 350, 230, 390, 40, 390, fill = "white", outline = "black")
	WCTtext = s.create_text(55, 360, text = "Bubble Cat was created by Elaine Zhu, \nBella Kim, Amy Zhou and Jasmine Xu!", anchor = NW, fill = "black", font = "arial 6")

# def giveQuestion():
#   question = random.choice(mathproblems)
#   print (question)

def game():
	global startBtn, HTPBtn
	s.delete("all")
	startBtn.destroy()
	HTPBtn.destroy()
	
	s.create_image(0, 0, image = (bg), anchor= NW)
	trigBtn = Button(root, text = "Trignometry", command = trig, bg="#a5b8ed", font="Arial 10", anchor = CENTER)
	trigBtn.pack()
	trigBtn.place(x=135, y=270, height=21, width=150, anchor=CENTER)
	
def trig():
	trigquestions = ["In triangle PQR, PR = 20 cm, < Q = 90°, < R = 41°. Find RQ to the narest tenth of a cm", "From the top of a tower, the angle of depression to the tip of the tower's shadow is 88°. The shadow is 19.5m long. How tall is the tower?(m)"]
	triganswers = ["13.1", "558.4"]
	randomnum = randint(0, 1)
	trigq = trigquestions[randomnum]
	triga = triganswers[randomnum]

	trigbox = s.create_polygon(50, 280, 220, 280, 220, 340, 50, 340, width = 15, fill = "Brown", outline = "Yellow")
	question = s.create_text(80, 290, text = trigq, anchor = NW, fill = "Black", font = "arial 8")

	answer = Entry(root, font=("Helvetica", 25), width=17, fg="#000000", borderwidth=0)
	answer.insert(0, "enter your answer here")
	answerWindow = s.create_window(110, 100, anchor="nw", window=answer)
	game()
def quad():
	return
def exponents():
	return

'''
replRatioBox = Entry(root, font=("Helvetica", 25), width=17, fg="#000000", borderwidth=0)
replRatioBox.insert(0, "ratio (ex: 1:1 or N/A)")
replRatioBoxWindow = s.create_window(110, 820, anchor="nw", window=replRatioBox)
'''

spacing = 25

for x in range(0, 800, spacing): 
	s.create_line(x, 25, x, 600, fill="white")
	s.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "black")

for y in range(0, 600, spacing):
	s.create_line(25, y, 800, y, fill="white")
	s.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "black")

home()
s.update()