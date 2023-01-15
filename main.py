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
s.pack(fill = BOTH, expand=False)

retryInt = 0

bg = ImageTk.PhotoImage(file = 'image/bg.png')
retryBg = ImageTk.PhotoImage(file = 'image/congrats+retry.png')
HTPbg = ImageTk.PhotoImage(file = "image/HTP.png")
logo = ImageTk.PhotoImage(file = 'image/logo.png')
gameBg = ImageTk.PhotoImage(file = 'image/game.png')
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

def howToPlay():
	global startBtn, HTPBtn
	s.delete("all")
	startBtn.destroy()
	HTPBtn.destroy()

	wave3 = s.create_polygon(-50, 435, 0, 435, 75, 450, 125, 400, 155, 380, 200, 360, 280, 380, 400, 380, -50, 450, smooth = True, fill = "#516ab0")
	wave1 = s.create_polygon(-100, 400, 0, 600, 300, 480, 350, 450, 135, 400, 60, 380, smooth = TRUE, fill = "#93AAE8")
	wave2 = s.create_polygon(-100, 350, 0, 600, 300, 480, 350, 330, 75, 450, smooth = TRUE, fill = "#627ABD")

	s.create_image(0, 0, image = (HTPbg), anchor = NW)
	
	startBtn = Button(root, text = "Start", command = game, bg="#93AAE8", font="Arial 10", anchor = CENTER)
	startBtn.pack()
	startBtn.place(x=135, y=420, height=21,width=150,anchor=CENTER)
	

def game():
	global startBtn, HTPBtn, trigBtn, quadBtn, point, retryBtn, multiBtn, exponentsBtn, rootsBtn, retryInt, quadquestions, quadanswers, quadanswers2, trigquestions, triganswers
	quadquestions = ["Two consecutive integers are \nadded. The square of their \nsum is 361. What is the \nsum of the integers", "The area of a rectangle is \n36cm2. The side lenghts are \n(x-5) and (x). What is one \nof the sides dimensions?", "-3 is one root of the equation \n3x^2 + mx + 3 = 0, \nwhat is the value of m.", "a^2 - 8a + 16 = 0","Find the axis of symmetry for: \ny=2x^2-4x-1", "You have to close a retangular \nfield with only 600m of fencing. \nWhat are that is the maxium area \nof the field?"]
	quadanswers = [19, 4, 10, 4, 1, 22500]
	quadanswers2 = [19, 9, 10, 4, 1, 22500]

	trigquestions = ["In triangle PQR, PR = 20 cm, \n< Q = 90°, < R = 41°. \nFind RQ to the nearest cm", "From the top of a tower, the \nangle of depression to the tip \nof the tower's shadow is 88°. \nThe shadow is 19.5m long. \nHow tall is the tower?\n(nearest m)", "A road has a 10% gradient,\nmeaning it rises 10m for \nevery 100m of horizontal \ndistance. What is the angle of \ninclination of the road, \nto the nearest degree?", "A 25 foot tall flagpole casts a \n42 foot shadow. What is the \nangle that the sun hits the \nflagpole?(Round to nearest \nangle)", "Shannon's job is to measure \nproperties. For a triangluar \npiece of land, 2 sides measure \n4.9m and 5.8m and meet at a \ncommon point seperat by a \n35° angle. Find the total \nperimeter of the piece of land.", "The tower is approximately 179m \nin height and is approximately \n16.5m out of plumb. Find the angle \nat which it deviates from the \nvertical(nearest °)" ]
	triganswers = [13, 558, 6, 59, 14, 5]
	
	point = 0
	s.delete("all")
	startBtn.destroy()
	startBtn.destroy()
	HTPBtn.destroy()

	if retryInt == 1:
		retryBtn.destroy()

	s.create_image(0, 0, image = (bg), anchor= NW)

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

	rootsBtn = Button(root, text = "Roots", command = roots, bg="#a5b8ed", font="Arial 7", anchor = CENTER)
	rootsBtn.pack()
	rootsBtn.place(x=80, y=280, height=21, width=75, anchor=CENTER)

def trig():
	global answer, answerWindow, triga, point, enterBtn, retryBtn, retryInt, trigq, trigquestions, triganswers

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

		
		randomnum = randint(0, len(trigquestions)-1)
		trigq = trigquestions[randomnum]
		triga = triganswers[randomnum]

		trigquestions.remove(trigq)
		triganswers.remove(triga)
		
		s.create_image(0, 0, image = (gameBg), anchor = NW)
		question = s.create_text(64, 275, text = trigq, anchor = NW, fill = "white", font = "arial 7")
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 200, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, triga, point, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == triga:
				point += 1
				enterBtn.destroy()
				trig()
			
		enterBtn = Button(root, text = "✓", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=200, height = 16, width = 16, anchor = NW)

	else:
		enterBtn.destroy()
		retry()

def quad():
	global answer, answerWindow, quada, quadaa ,point, enterBtn, retryBtn, retryInt, quadquestions, quaadanswers, quadanswers2

	
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

		quadrandomnum = randint(0,len(quadquestions)-1)
		quadq = quadquestions[quadrandomnum]
		quada = quadanswers[quadrandomnum]
		quadaa = quadanswers2[quadrandomnum]

		quadquestions.remove(quadq) 
		quadanswers.remove(quada)
		quadanswers2.remove(quadaa)
	
		s.create_image(0, 0, image = (gameBg), anchor = NW)
		question = s.create_text(64, 275, text = quadq, anchor = NW, fill = "white", font = "arial 7")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 200, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, quadq, point, retryInt, quadquestions, quadanswers, quadanswers2
			answerUser = answer.get()
			
			if int(answerUser) == quada or int(answerUser) == quadaa:
				point += 1
				enterBtn.destroy()
				quad()
	
		enterBtn = Button(root, text = "✓", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=200, height = 16, width = 16, anchor = NW)

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

	
		s.create_image(0, 0, image = (gameBg), anchor = NW)
		question = s.create_text(70, 300, text = "(" + (str(a) + ") * (" + str(b)) + ")", anchor = NW, fill = "white", font = "arial 15")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 200, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, multiplyanswer, point, multiBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == multiplyanswer:
				point += 1
				enterBtn.destroy()
				multiplication()

	
		enterBtn = Button(root, text = "✓", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=200, height = 16, width = 16, anchor = NW)

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

		a = randint(-10, 20)
		b = randint(0, 6)

		exponentans = a ** b

	
		s.create_image(0, 0, image = (gameBg), anchor = NW)
		question1 = s.create_text(160, 300, text = "(" + str(a) + ")", anchor = NE, fill = "white", font = "arial 15")
		question2 = s.create_text(160, 300, text = str(b), anchor = NW, fill = "white", font = "arial 10")

		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 200, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, exponentans, point, exponentsBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == exponentans:
				point += 1
				enterBtn.destroy()
				exponents()

	
		enterBtn = Button(root, text = "✓", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=200, height = 16, width = 16, anchor = NW)

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

		o = randint(0, 25)

		squareroot = o*o

	
		s.create_image(0, 0, image = (gameBg), anchor = NW)
		question = s.create_text(70, 300, text = "√" +  str(squareroot), anchor = NW, fill = "white", font = "arial 15")
	
		answer = Entry(root, font=("Helvetica", 7), width=17, fg="#000000", borderwidth=0)
		answerWindow = s.create_window(80, 200, anchor="nw", window=answer)
	
		def check():
			global answer, answerWindow, o, point, rootsBtn, retryInt
			answerUser = answer.get()
			
			if int(answerUser) == o:
				point += 1
				enterBtn.destroy()
				roots()

			

		enterBtn = Button(root, text = "✓", command = check, bg="white", font="Helvetica 7", anchor = NE)
		enterBtn.pack()
		enterBtn.place(x=180, y=200, height = 16, width = 16, anchor = NW)

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