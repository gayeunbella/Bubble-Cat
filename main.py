import Image
from tkinter import *
from time import *
from PIL import Image, ImageTk
from random import *
#from mathproblems import mathlist
root = Tk()
root.geometry("270x480")
root.title('Bubble Cat')
s = Canvas(root, width = 270, height = 480, bg='#FFF7EB')
s.pack(fill = BOTH, expand=True)

retryInt = 0

wrong = ImageTk.PhotoImage(file = 'image/wrong.png')
bg = ImageTk.PhotoImage(file = 'image/bg.png')
retryBg = ImageTk.PhotoImage(file = 'image/congrats+retry.png')
logo = ImageTk.PhotoImage(file = 'image/logo.png')
s.create_image(130, 140, image = (logo), anchor = CENTER)

point = 0

def home():
	global startBtn, HTPBtn, point, retryBtn
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

	startBtn = Button(root, text = "Start", command = game, bg="#93AAE8", font="Arial 10", anchor = CENTER)
	startBtn.pack()
	startBtn.place(x=135, y=400,height=21,width=150,anchor=CENTER)
	

def game():
	global startBtn, HTPBtn, trigBtn, quadBtn, point, retryBtn, multiBtn, exponentsBtn, factoringBtn, rootsBtn, retryInt
	point = 0
	s.delete("all")
	startBtn.destroy()
	startBtn.destroy()
	HTPBtn.destroy()

	if retryInt == 1:
		retryBtn.destroy()

	s.create_image(0, 0, image = (bg), anchor= NW)
	
	spacing = 25

	for x in range(0, 800, spacing): 
		s.create_line(x, 25, x, 600, fill="white")
		s.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "black")
	
	for y in range(0, 600, spacing):
		s.create_line(25, y, 800, y, fill="white")
		s.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "black")

	trigBtn = Button(root, text = "Trignometry", command = trig, bg="#a5b8ed", font="Arial 7", anchor = CENTER)
	trigBtn.pack()
	trigBtn.place(x=70, y=160, height=21, width=75, anchor=CENTER)

	quadBtn = Button(root, text = "Quadratics", command = quad, bg="#6c86cf", font="Arial 7", anchor = CENTER)
	quadBtn.pack()
	quadBtn.place(x=175, y=215, height=21, width=75, anchor=CENTER)

	multiBtn = Button(root, text = "Multiplication", command = multiplication, bg="#c3cff6", font="Arial 7", anchor = CENTER)
	multiBtn.pack()
	multiBtn.place(x=187, y=425, height=21, width=75, anchor=CENTER)

	exponentsBtn = Button(root, text = "Exponents", command = exponents, bg="#859fe8", font="Arial 7", anchor = CENTER)
	exponentsBtn.pack()
	exponentsBtn.place(x=70, y=410, height=21, width=75, anchor=CENTER)

	# factoringBtn = Button(root, text = "Factoring", command = exponents, bg="#c3cff6", font="Arial 7", anchor = CENTER)
	# factoringBtn.pack()
	# factoringBtn.place(x=215, y=120, height=21, width=70, anchor=CENTER)

	rootsBtn = Button(root, text = "Roots", command = roots, bg="#a5b8ed", font="Arial 7", anchor = CENTER)
	rootsBtn.pack()
	rootsBtn.place(x=80, y=280, height=21, width=75, anchor=CENTER)

def trig():
	global answer, answerWindow, triga, point, enterBtn, retryBtn, retryInt

	if point < 3:
		s.delete("all")
		quadBtn.destroy()
		trigBtn.destroy()
		startBtn.destroy()
		multiBtn.destroy()
		exponentsBtn.destroy()
		rootsBtn.destroy()

		if retryInt == 1:
			retryBtn.destroy()

		trigquestions = ["In triangle PQR, PR = 20 cm, \n< Q = 90°, < R = 41°. \nFind RQ to the nearest cm", "From the top of a tower, the \nangle of depression to the tip \nof the tower's shadow is 88°. \nThe shadow is 19.5m long. \nHow tall is the tower?\n(nearest m)", "A road has a 10% gradient,\nmeaning it rises 10m for \nevery 100m of horizontal \ndistance. What is the angle of \ninclination of the road, \nto the nearest degree?", "A 25 foot tall flagpole casts a \n42 foot shadow. What is the \nangle that the sun hits the \nflagpole?(Round to nearest \nangle)"]
		triganswers = [13, 558, 6, 59]
		randomnum = randint(0, 3)
		trigq = trigquestions[randomnum]
		triga = triganswers[randomnum]
	
		treasurechestbot = s.create_polygon(50, 260, 220, 260, 220, 360, 50, 360, width = 15, fill = "#75421d", outline = "#fedd54")
		question = s.create_text(64, 275, text = trigq, anchor = NW, fill = "white", font = "arial 7")
	
		treasurechesttop = s.create_polygon(50, 260, 220, 260, 190, 210, 80, 210, width = 15, fill = "#75421d", outline = "#fedd54")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 230, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, triga, point, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == triga:
				point += 1
				enterBtn.destroy()
				trig()
			
		enterBtn = Button(root, text = "🔍", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=230, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

def quad():
	global answer, answerWindow, quada, quadaa ,point, enterBtn, retryBtn, retryInt

	if point < 3:
		s.delete("all")
		quadBtn.destroy()
		trigBtn.destroy()
		startBtn.destroy()
		multiBtn.destroy()
		exponentsBtn.destroy()
		rootsBtn.destroy()

		if retryInt == 1:
			retryBtn.destroy()

		
		quadquestions = ["Two consecutive integers are \nadded. The square of their sum is 361. What is the sum of the integers", "The area of a rectangle is \n36cm2. The side lenghts are (x-5) and (x). What is one of the sides dimensions?", "If -3 is one root of the equation 3x^2 + mx + 3 = 0, what is the value of m.", "a^2 - 8a + 16 = 0"]
		quadanswers = [19, 4, 10, 4]
		quadanswers2 = [19, 9, 10, 4]
		quadrandomnum = randint(0, 3)
		quadq = quadquestions[quadrandomnum]
		quada = quadanswers[quadrandomnum]
		quadaa = quadanswers2[quadrandomnum]
	
		treasurechestbot = s.create_polygon(50, 260, 220, 260, 220, 360, 50, 360, width = 15, fill = "#75421d", outline = "#fedd54")
		question = s.create_text(64, 275, text = quadq, anchor = NW, fill = "white", font = "arial 7")
	
		treasurechesttop = s.create_polygon(50, 260, 220, 260, 190, 210, 80, 210, width = 15, fill = "#75421d", outline = "#fedd54")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 230, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, quadq, point, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == quada or int(answerUser) == quadaa:
				point += 1
				enterBtn.destroy()
				quad()

	
		enterBtn = Button(root, text = "🔍", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=230, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

	
def multiplication():
	global answer, answerWindow, point, enterBtn, retryBtn, multiBtn, multiplyanswer, retryInt

	if point < 3:
		s.delete("all")
		quadBtn.destroy()
		trigBtn.destroy()
		startBtn.destroy()
		multiBtn.destroy()
		exponentsBtn.destroy()
		rootsBtn.destroy()

		if retryInt == 1:
			retryBtn.destroy()

		a = randint(-100, 200)
		b = randint(-100, 200)

		multiplyanswer = a * b

	
		treasurechestbot = s.create_polygon(50, 260, 220, 260, 220, 360, 50, 360, width = 15, fill = "#75421d", outline = "#fedd54")
		question = s.create_text(70, 300, text = "(" + (str(a) + ") * (" + str(b)) + ")", anchor = NW, fill = "white", font = "arial 15")
	
		treasurechesttop = s.create_polygon(50, 260, 220, 260, 190, 210, 80, 210, width = 15, fill = "#75421d", outline = "#fedd54")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 230, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, multiplyanswer, point, multiBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == multiplyanswer:
				point += 1
				enterBtn.destroy()
				multiplication()

	
		enterBtn = Button(root, text = "🔍", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=230, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

def exponents():
	global answer, answerWindow, point, enterBtn, retryBtn, exponentsBtn, exponentans, retryInt

	if point < 3:
		s.delete("all")
		quadBtn.destroy()
		trigBtn.destroy()
		startBtn.destroy()
		multiBtn.destroy()
		exponentsBtn.destroy()
		rootsBtn.destroy()

		if retryInt == 1:
			retryBtn.destroy()

		a = randint(-10, 10)
		b = randint(0, 6)

		exponentans = a ** b

	
		treasurechestbot = s.create_polygon(50, 260, 220, 260, 220, 360, 50, 360, width = 15, fill = "#75421d", outline = "#fedd54")
		question1 = s.create_text(160, 300, text = "(" + str(a) + ")", anchor = NE, fill = "white", font = "arial 15")
		question2 = s.create_text(160, 300, text = str(b), anchor = NW, fill = "white", font = "arial 10")
	
		treasurechesttop = s.create_polygon(50, 260, 220, 260, 190, 210, 80, 210, width = 15, fill = "#75421d", outline = "#fedd54")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 230, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, exponentans, point, exponentsBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == exponentans:
				point += 1
				enterBtn.destroy()
				exponents()

	
		enterBtn = Button(root, text = "🔍", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=230, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

def roots():
	global answer, answerWindow, point, enterBtn, retryBtn, rootsBtn, retryInt, o

	if point < 3:
		s.delete("all")
		quadBtn.destroy()
		trigBtn.destroy()
		startBtn.destroy()
		multiBtn.destroy()
		exponentsBtn.destroy()
		rootsBtn.destroy()

		if retryInt == 1:
			retryBtn.destroy()

		o = randint(0, 10)

		squareroot = o*o

	
		treasurechestbot = s.create_polygon(50, 260, 220, 260, 220, 360, 50, 360, width = 15, fill = "#75421d", outline = "#fedd54")
		question = s.create_text(70, 300, text = "√" +  str(squareroot), anchor = NW, fill = "white", font = "arial 15")
	
		treasurechesttop = s.create_polygon(50, 260, 220, 260, 190, 210, 80, 210, width = 15, fill = "#75421d", outline = "#fedd54")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 230, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, o, point, rootsBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == o:
				point += 1
				enterBtn.destroy()
				roots()

			

		enterBtn = Button(root, text = "🔍", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=230, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

def retry():
	global retryBtn, retryInt
	
	s.delete("all")
	s.create_image(0, 0, image = (retryBg), anchor = NW)
	retryBtn = Button(root, text = "Retry?", command = game, bg="white", font="Helvetica 10", anchor = CENTER)
	retryBtn.pack()
	retryBtn.place(x=140, y=420, height = 30, width = 170, anchor = CENTER)
	retryInt = 1

home()
s.update()