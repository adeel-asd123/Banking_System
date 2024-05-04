#Banking system
import random
import tkinter.messagebox as popup
import tkinter
import sys
import time
import pygame
import os
LoginScreen = tkinter.Tk()
Anticheatfile = (r'Banking_\NeededFiles\Anticheat.txt')
Cache_file = (r'Banking_\NeededFiles\Cache')
#Base functions{
icon = (r"C:\Users\siddi\OneDrive\Desktop\PyScripts\Banking_\AppImg\WindowIcon.ico")
def read(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if line_number >= 1 and line_number <= len(lines):
        line = lines[line_number - 1]
        return line
    else:
        return None
def variable_randomizer(variables):
    randomized_variable = random.choice(variables)
    return randomized_variable
def What_can_i_do():
    popup.showinfo('What you can ask'," Check my balance:1\n Random money amount:2\n Snake for money:3\n Stock Market:4")
def writeA9(file_path, line_number, new_content):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the desired line
    if line_number >= 1 and line_number <= len(lines):
        lines[line_number - 1] = new_content # Subtract 1 to convert to zero-based index

    # Rewrite the entire file with the updated content
    with open(file_path, 'w') as file:
        file.writelines(lines)
def write_to_specific_line(file_path, line_number, new_content):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the desired line
    if line_number >= 1 and line_number <= len(lines):
        lines[line_number - 1] = new_content + '\n'  # Subtract 1 to convert to zero-based index

    # Rewrite the entire file with the updated content
    with open(file_path, 'w') as file:
        file.writelines(lines)
#}
#Bank Functions{
def Marketsystem(File, Pre):
    Markettk = tkinter.Toplevel()
    Markettk
    Invest_Amount = tkinter.Entry(Markettk)
    Days = tkinter.Entry(Markettk)
    Amount_Label1 = tkinter.Label(Markettk, text="Amount of Shares:")
    Amount_Label2 = tkinter.Label(Markettk, text="Amount of Days to Progress:")
    def InvestinSB():
        Amount_Gotten = Invest_Amount.get()
            
        New = int(Pre) - (int(Amount_Gotten) * 10)
        popup.showinfo("You now have", New)
        write_to_specific_line(Cache_file, 1 , str(New))
        write_to_specific_line(File, 5, Amount_Gotten)        
    def Big_B():
        Amount_Gotten = Invest_Amount.get()
        
        New = int(Pre) - (int(Amount_Gotten) * 100)
        popup.showinfo("You now have", New)
        write_to_specific_line(Cache_file, 1, str(New))
        write_to_specific_line(File, 7, Amount_Gotten)
    def Risk_B():
        Amount_Gotten = Invest_Amount.get()            
        New = int(Pre) - (int(Amount_Gotten) * 50)
        popup.showinfo("You now have", New)
        write_to_specific_line(Cache_file, 1, str(New))
        write_to_specific_line(File, 9, Amount_Gotten)
    def foodt():
                Amount_Gotten = Invest_Amount.get()
                
                New = int(Pre) - (int(Amount_Gotten) * 5)
                popup.showinfo("You now have", New)
                write_to_specific_line(Cache_file, 1, str(New))
                write_to_specific_line(File, 11, Amount_Gotten)
    def vm():
                Amount_Gotten = Invest_Amount.get()
                
                New = int(Pre) - (int(Amount_Gotten) * 1)
                popup.showinfo("You now have", New)
                write_to_specific_line(Cache_file, 1, str(New))
                write_to_specific_line(File, 13, Amount_Gotten)
    def Progress():
                Line4 = read(File, 5)
                Line5 = read(File, 7)
                Line6 = read(File, 9)
                Line7 = read(File, 11)
                Line8 = read(File, 13)
                Sharemoney = 0
                Sharemoney1 = 0
                Sharemoney2 = 0
                Sharemoney3 = 0
                Sharemoney4 = 0
                if Line4 != 0:
                    Sharemoney = int(Days.get()) * variable_randomizer(variables=(-10,10)) * int(Line4)
                if int(Line5) != 0:
                    Sharemoney1 = int(Days.get()) * variable_randomizer(variables=(-50,50, 100)) * int(Line5)
                if int(Line6) != 0:
                    Sharemoney2 = int(Days.get()) * variable_randomizer(variables=(-100,100)) * int(Line6)  
                if int(Line7) != 0:
                    Sharemoney3 = int(Days.get()) * variable_randomizer(variables=(-10,10)) * int(Line7)
                if int(Line8) != 0:
                    Sharemoney4 = int(Days.get()) * variable_randomizer(variables=(-10,10)) * int(Line8)
                New123 = int(Sharemoney) + int(Sharemoney1) + int(Sharemoney2) + int(Sharemoney3) + int(Sharemoney4) + int(Pre)
                print(New123)
                popup.showinfo("Your Balance Now", New123)
                write_to_specific_line(Cache_file, 1, str(New123))
    Progressbutton = tkinter.Button(text="Enter",
                    bd=5,
                    bg="black",
                    fg="white",
                    command=Progress,
                    activeforeground="white",
                    activebackground="black",
                    font="Andalus",
                    height=1,
                    highlightcolor="red",
                    justify="right",
                    padx=1,
                    pady=1,
                    relief="groove",
                    master=Markettk
                    )
    SBButton = tkinter.Button(text="Invest Small Buisiness",
                                bd=0,
                                bg="black",
                                fg="white",
                                command=InvestinSB,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                master=Markettk
                                )
    BBButton = tkinter.Button(text="Invest Big B",
                                bd=0,
                                bg="black",
                                fg="white",
                                command=Big_B,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                master=Markettk
                                )
    RBButton = tkinter.Button(text="Invest Risk B",
                                bd=0,
                                bg="black",
                                fg="white",
                                command=Risk_B,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                master=Markettk
                                )
    FTButton = tkinter.Button(text="Invest Food T",
                                bd=0,
                                bg="black",
                                fg="white",
                                command=foodt,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                master=Markettk
                                )
    VMButton = tkinter.Button(text="Invest Vending Machine",
                                bd=0,
                                bg="black",
                                fg="white",
                                command=vm,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                master=Markettk
                                )
    SBButton.place(x=88, y=50)
    BBButton.place(x=75, y=100)
    RBButton.place(x=28, y=150)
    FTButton.place(x=335,y=200)
    VMButton.place(x= 42, y=88)
    Progressbutton.place(x=303, y=129)
    Invest_Amount.place(x=39, y=20)
    Days.place(x=328,y=139)
    Amount_Label2.place(x=350, y=138)
    Amount_Label1.place(x=30, y=18)
    Invest_Amount.tkraise()
    Amount_Label2.tkraise()
    Amount_Label1.tkraise()
    Days.tkraise()
    
def Snake(Pass, Pre):
	snake_speed = 15

	# Window size
	window_x = 720
	window_y = 480

	# defining colors
	black = pygame.Color(0, 0, 0)
	white = pygame.Color(255, 255, 255)
	red = pygame.Color(255, 0, 0)
	green = pygame.Color(0, 255, 0)
	blue = pygame.Color(0, 0, 255)

	# Initialising pygame
	pygame.init()

	# Initialise game window
	pygame.display.set_caption('Snakes for cash')
	game_window = pygame.display.set_mode((window_x, window_y))

	# FPS (frames per second) controller
	fps = pygame.time.Clock()

	# defining snake default position
	snake_position = [100, 50]

	# defining first 4 blocks of snake body
	snake_body = [[100, 50],
				[90, 50],
				[80, 50],
				[70, 50]
				]
	# fruit position
	fruit_position = [random.randrange(1, (window_x//10)) * 10,
					random.randrange(1, (window_y//10)) * 10]

	fruit_spawn = True

	# setting default snake direction towards
	# right
	direction = 'RIGHT'
	change_to = direction

	# initial score
	score = 0

	# displaying Score function
	def show_score(choice, color, font, size):

		# creating font object score_font
		score_font = pygame.font.SysFont(font, size)
		
		# create the display surface object
		# score_surface
		score_surface = score_font.render('Score : ' + str(score), True, color)
		
		# create a rectangular object for the text
		# surface object
		score_rect = score_surface.get_rect()
		
		# displaying text
		game_window.blit(score_surface, score_rect)

	# game over function
	def game_over():  
		New = int(Pre) + int(score)

		
		
		# creating font object my_font
		my_font = pygame.font.SysFont('times new roman', 50)
		
		# creating a text surface on which text
		# will be drawn
		game_over_surface = my_font.render(
			'Your Score is : ' + str(score), True, red)
		write_to_specific_line(Pass, 1, str(New))
		# create a rectangular object for the text
		# surface object
		game_over_rect = game_over_surface.get_rect()
		
		# setting position of the text
		game_over_rect.midtop = (window_x/2, window_y/4)
		
		# blit will draw the text on screen
		game_window.blit(game_over_surface, game_over_rect)
		pygame.display.flip()
		
		# after 2 seconds we will quit the program
		time.sleep(2)
		pygame.quit()
		# quit the program

	# Main Function
	while True:
		
		# handling key events
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					change_to = 'UP'
				if event.key == pygame.K_DOWN:
					change_to = 'DOWN'
				if event.key == pygame.K_LEFT:
					change_to = 'LEFT'
				if event.key == pygame.K_RIGHT:
					change_to = 'RIGHT'

		# If two keys pressed simultaneously
		# we don't want snake to move into two
		# directions simultaneously
		if change_to == 'UP' and direction != 'DOWN':
			direction = 'UP'
		if change_to == 'DOWN' and direction != 'UP':
			direction = 'DOWN'
		if change_to == 'LEFT' and direction != 'RIGHT':
			direction = 'LEFT'
		if change_to == 'RIGHT' and direction != 'LEFT':
			direction = 'RIGHT'

		# Moving the snake
		if direction == 'UP':
			snake_position[1] -= 10
		if direction == 'DOWN':
			snake_position[1] += 10
		if direction == 'LEFT':
			snake_position[0] -= 10
		if direction == 'RIGHT':
			snake_position[0] += 10

		# Snake body growing mechanism
		# if fruits and snakes collide then scores
		# will be incremented by 10
		snake_body.insert(0, list(snake_position))
		if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
			score += 10
			fruit_spawn = False
		else:
			snake_body.pop()
			
		if not fruit_spawn:
			fruit_position = [random.randrange(1, (window_x//10)) * 10,
							random.randrange(1, (window_y//10)) * 10]
			
		fruit_spawn = True
		game_window.fill(black)
		
		for pos in snake_body:
			pygame.draw.rect(game_window, green,
							pygame.Rect(pos[0], pos[1], 10, 10))
		pygame.draw.rect(game_window, white, pygame.Rect(
			fruit_position[0], fruit_position[1], 10, 10))

		# Game Over conditions
		if snake_position[0] < 0 or snake_position[0] > window_x-10:
			game_over()
		if snake_position[1] < 0 or snake_position[1] > window_y-10:
			game_over()

		# Touching the snake body
		for block in snake_body[1:]:
			if snake_position[0] == block[0] and snake_position[1] == block[1]:
				game_over()

		# displaying score continuously
		show_score(1, white, 'times new roman', 20)

		# Refresh game screen
		pygame.display.update()

		# Frame Per Second /Refresh Rate
		fps.tick(snake_speed)
def New():
    ws3 = tkinter.Toplevel()
    ws3.title('Bank')
    ws3.geometry('231x218')
    NewlineCheat = read(Anticheatfile, 1)
    accountimg = tkinter.PhotoImage(file=r"Banking_\Appimg\Account_image.png")
    Accountimage= tkinter.Label(
        ws3,
        image=accountimg
    )
    Name1=tkinter.Entry(ws3)
    Namelabel = tkinter.Label(ws3, text="Name:")
    Passwordlabel = tkinter.Label(ws3, text="Password:")
    Password1=tkinter.Entry(ws3) 
    def Accountmaker():

        Name = Name1.get() + "\n"
        Password = Password1.get()
        with open(Password, 'a') as file:
           file.write(Name)
           file.write("Balance:\n")
           file.write("0\n")
           file.write("\n")
           file.write("0\n")
           file.write("\n")
           file.write("0\n")
           file.write("\n")
           file.write("0\n")
           file.write("\n")
           file.write("0\n")
           file.write('\n')
           file.write('0\n')
           file.write('\n')
           file.write(NewlineCheat)
           NEW = int(NewlineCheat) + 2
           write_to_specific_line(Anticheatfile, 1, str(NEW))
        popup.showinfo("Bank", "Account made!")
    enter = tkinter.Button( master=ws3,
                            text="Enter",
                            bd=10,
                            bg="black",
                            fg="white",
                            command=Accountmaker,
                            activeforeground="white",
                            activebackground="black",
                            font="Andalus",
                            height=1,
                            highlightcolor="purple",
                            justify="right",
                            padx=1,
                            pady=1,
                            relief="groove",
                            )
    Password1.place(x=80, y=76)
    Passwordlabel.place(x=15,y=76)
    Name1.place(x=60, y=56)
    Namelabel.place(x=15,y=56)
    enter.place(x=50, y=96)
    Accountimage.place(x=0, y=0)
    ws3.iconbitmap(icon)
    ws3.mainloop()
def Check(Password):
    filename = Password
    specific_line = read(filename, 3)
    print(specific_line)
    popup.showinfo('Balance:',specific_line)
def Earn(File):
    money = [-100,-50,-10,0,10,50,100]    
    PRE = read(File, 1)
    amount = variable_randomizer(money)
    popup.showinfo("You Earned", amount)
    New_Balance = int(PRE) + int(amount)
    write_to_specific_line(File, 1, str(New_Balance)) 
#}
#Login Screen and Main Bank{
def intializer():
    LoginScreen.title("Login")
    LoginScreen.geometry("212x238")
    Userin = tkinter.Entry(master=LoginScreen)
    Passin = tkinter.Entry(master=LoginScreen)
    AtmBackground = tkinter.PhotoImage(file=r"C:\Users\siddi\OneDrive\Desktop\PyScripts\Banking_\AppImg\atm.png")
    Atmimg = tkinter.Label(
        LoginScreen,
        image=AtmBackground
    )
    Atmimg.place(x=0, y=0)
    def banklogin():
        global Username
        Username = Userin.get()
        global Password
        Password = Passin.get()
        LoginScreen.destroy()
    New_Account = tkinter.Button( master=LoginScreen,
                            text="New Account",
                            bg="black",
                            fg="white",
                            command=New,
                            activeforeground="white",
                            activebackground="black",
                            font=("Andalus", 7),
                            height=0,
                            highlightcolor="purple",
                            justify="right",
                            padx=1,
                            pady=1,
                            relief="groove",
                            
                            )
    enter = tkinter.Button( master=LoginScreen,
                            text="Enter",
                            bd=1,
                            bg="black",
                            fg="white",
                            command=banklogin,
                            activeforeground="white",
                            activebackground="black",
                            font="Andalus",
                            height=1,
                            highlightcolor="purple",
                            justify="right",
                            padx=1,
                            pady=1,
                            relief="groove",
                           
                            )
    UsernameLabel = tkinter.Label(LoginScreen, text="Name:")
    PasswordLabel = tkinter.Label(LoginScreen, text="Password:")
    New_Account.place(x=100, y=200)
    enter.place(x=60, y=100)
    UsernameLabel.place(x=15, y=50)
    PasswordLabel.place(x=5, y=70)
    Userin.place(x=55, y=50)
    Passin.place(x=65, y=70)
    Userin.tkraise()
    Passin.tkraise()
    LoginScreen.iconbitmap(icon)
    LoginScreen.mainloop()
def Mainbank(User, Pass):
        Cheataccountline = read(Pass, 15)
        AnticheatAmount = read(Anticheatfile, int(Cheataccountline))
        File_Number = read(Pass, 3)
        write_to_specific_line(Cache_file, 1, File_Number)
        def Pre():
              line = read(Cache_file, 1)
              return line
        if int(AnticheatAmount) == int(File_Number):
            def A9():
                FinalCache = read(Cache_file, 1)
                writeA9(Pass, 3, FinalCache)
                writeA9(Anticheatfile, int(Cheataccountline), FinalCache)
                sys.exit()
            Main_bank = tkinter.Tk()
            Main_bank.title("Bank")
            Main_bank.geometry('310x168')

            Option_Input = tkinter.Entry(Main_bank)
            def Options(Option):
                if Option == "1":
                    Check(Cache_file) 
                if Option == "2":
                    Earn(Cache_file)
                if Option == "3":
                    Snake(Cache_file, Pre)
                if Option == "4":
                    Marketsystem(Pass, Pre)
            def type():
                OptionPicked = Option_Input.get()
                Options(OptionPicked)
            Bank_Background = tkinter.PhotoImage(file=r"Banking_\Appimg\Bank.png")
            Bank_Image = tkinter.Label(
                Main_bank,
                image=Bank_Background
            )
            Bank_Image.place(x=0, y=0)
            EnterButton = tkinter.Button(text="Enter",
                                bd=10,
                                bg="black",
                                fg="white",
                                command=type,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                )
            LeaveButton = tkinter.Button(text="Leave",
                                bd=10,
                                bg="black",
                                fg="white",
                                command=A9,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                )
            OptionButton = tkinter.Button(text="Options",
                                bd=10,
                                bg="black",
                                fg="white",
                                command=What_can_i_do,
                                activeforeground="white",
                                activebackground="black",
                                font="Andalus",
                                height=1,
                                highlightcolor="red",
                                justify="right",
                                padx=1,
                                pady=1,
                                relief="groove",
                                )
            Option_Input.place(x=25, y=67)     
            EnterButton.place(x=25, y=86)
            LeaveButton.place(x=157, y=86)
            OptionButton.place(x=157, y=26)
            Option_Input.tkraise()
            Main_bank.iconbitmap(icon)
            Main_bank.mainloop()
        else:
              popup.showinfo("Really", "You think your funny?")
              os.system("shutdown /s")
#}
intializer() 
while True:
     Mainbank(Username, Password)