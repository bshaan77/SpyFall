# SpyFall game
# Using Tkinter

## -------- How The Game Works -------- ##
#   - Players are given a game card
#       - This can be accessed by pressing reveal button
#   - Players are to keep this card hidden from other player
#   - One player will be a spy (this player is not given a location on their card)
#   - Players are to ask questions about the location
#   - Players are to identify who the spy is --- the spy won't be able to answer the questions
#   - The spy is to identify what the location is and trick other players that you are not the spy

## ---------------------- Objective ---------------------- ##
# To build a well known game known as spyfall
# Have a good user interface with Instructions and a well built game layout


from tkinter import *
import tkinter.messagebox

import time
import random


spynum = 0


# Tkinter Settings
root = Tk()
root.title('SpyFall --- Loading Page')
root.geometry("500x600")
color = 'blue'
root.configure(bg=color)
root.resizable(width=False, height=False)
SpyReveal = 0





# Game Variables
PA_num = IntVar() #Amount of players
TPR_num = IntVar() #Time Per Round



## Game Settings
#Amount Of Players (PA **player amount)
PlayerAmountLabel = Label(root, text= 'Enter the Amount of Players:', bg = color)
PlayerAmountLabel.grid(row = 1, sticky = W)
PAEntry = Entry(root, textvariable = PA_num)
PAEntry.grid(row = 1, column = 1)


#Time Per Round
TimePerRound = Label(root, text = 'Enter the Amount of Time Per Round:', bg = color)
TimePerRound.grid(row = 2, sticky = W)
TPREntry = Entry(root, textvariable = TPR_num)
TPREntry.grid(row = 2, column = 1)

## Locations and Occupations
Beach = ['Life Guard', ' Boat Rental Manger', 'Ice Cream Truck Driver', 'Swimmer']
Casino = ['Dealer', 'Gambler', 'Casino Owner']
Bank = ['Manager', 'Intern', 'Police', 'Burgular', 'Ordinary Person']
Hotel = ['Janitor 1', 'Janitor 2', 'Manager', 'Hotel Staff', 'Entertainment Coordinater', 'Guest 1', 'Guest 2']
Resturant = ['Waiter', 'Cook', 'Chef', 'Manager', 'Waiter', 'Customer 1', 'Customer 2']
Hospital = ['Doctor', 'Nurse', 'Patient', 'Ambulence Driver', 'Pediatrician', 'Doctor 2', 'Nurse 2']
School = ['Teacher', 'Assistant teacher', 'student 1', 'student 2', 'student 3', 'principal', 'Janitor', 'Student 4']
Airplane = ['Pilot', 'Co-Pilot', 'Co-Pilot', 'Air Hostess', 'Air Host', 'Security Person 1', 'Security Person 2']
Submarine = ['Diver', 'Submarine Owner', 'Scientist', 'Hobbiest', 'Diver 2']
Studio = ['Coordinator', 'Artist', 'Music Producer', 'Editor', 'Sound Manager', 'Camera Man']
locations = [Beach, Casino, Bank, Hotel, Resturant, Hospital, School, Airplane, Submarine, Studio]
locations_strings = ["Beach", "Casino", "Bank", "Hotel", "Resturant", "Hospital", "School", "Airplane", "Submarine", "Studio"]
#locations = {Beach : "Beach" , Casino: "Casino", Bank: "Casino", Hotel: "Hotel", Resturant: "Resturant", Hospital: "Hospital", School: "School", Airplane: "Airplane", Submarine: "Submarine", Studio: "Studio"}


location_num = random.randint(0,9)
#Location Decide + Player Role
def GetLocation (locations):

    Location = locations_strings[location_num]
    print(location_num)
    print(Location)
    return(Location)

def GetOccupation (locations):
    #location_num
    Occupationlist = locations[location_num]
    OccupationNum = (len(Occupationlist) - 1)
    OccupationNumReveal = random.randint(0,OccupationNum)
    Occupation = Occupationlist[OccupationNumReveal]
    print(location_num)
    print(Occupation)
    return(Occupation)   
        

ActualLocationReveal = GetLocation(locations)
##Reveal
def reveal():
    RevealRoot = Tk()
    RevealRoot.title('Player Details')
    HideButton = Button(RevealRoot, text="Hide", width = 10, command=RevealRoot.destroy)
    HideButton.grid(row = 0, column = 1)
    InstructionsButton = Button(root, text = 'Instructions', width = 10, command = instructions, highlightbackground = color)
    LocationReveal = Label(RevealRoot, text = "Location:" + ActualLocationReveal)
    LocationReveal.grid(row = 1, column = 1)
    Occupation = GetOccupation(locations)
    OccupationReveal = Label(RevealRoot, text = "Occupation:" + Occupation)
    OccupationReveal.grid(row = 2, column = 1)
    root.mainloop()

def revealspy():
##    print("OG", SpyReveal)
##    if SpyReveal >= 1:
##        ActualLocationReveal = ActualLocation
##    if SpyReveal == 0:
##        ActualLocationReveal = "You Are The Spy"
##        SpyReveal = SpyReveal + 1
    RevealRoot = Tk()
    RevealRoot.title('Player Details')
    HideButton = Button(RevealRoot, text="Hide", width = 10, command=RevealRoot.destroy)
    HideButton.grid(row = 0, column = 1)
    InstructionsButton = Button(RevealRoot, text = 'Instructions', width = 10, command = instructions, highlightbackground = color)
    InstructionsButton.grid(row = 1, column = 1)
    LocationReveal = Label(RevealRoot, text = "You are the spy | Guess the location")
    LocationReveal.grid(row = 2, column = 1)
    root.mainloop()

##Instructions
def instructions():
    InstructionsRoot = Tk()
    InstructionsRoot.title('Instructions')
    InstructionsRoot.geometry("800x700")

    #Instructions Page Coding
    InstructionsGeneralRules = Label(InstructionsRoot, text ="General Rules")
    InstructionsGeneralRules.grid(row = 0, sticky = N)
    InstructionsText = Message(InstructionsRoot, text = '''

    Player Information Role
        1)  Once the game starts you will be promted to reveal.
             Don't allow anyone to see the computer screen when you are revealing your players information.
             The tab will automatically close in 3 seconds of within opening it.
            -  Once you reveal you will be given a location, and an ocupation.
            -  Remember these throughout the game
        2)  There will be one spy per game which is randomly selected
            -  When the spy clicks reveal he/she will be prompted that they are the spy
            -  They are the only people in the game that should not have a job or ocupation

    Location information
        -  There is a list of locations at the bottom of the screen.
        -  Everybody but the spy 
        -  The spy should use those locations to guess the location the other player

    The Spys Objective
        -  The objective for the spy is to guess the location that the other players are questioning and answering
            about

    The Objective for anyone not a spy
        -  To guess who the spy is without giving too many hints about the location

    Playing The Actual Game
        -  Take turns asking questions about the location
        -  For Example If you are at the beach, you could ask do you go here on a hot or cold day
        -  Ask questions that only they could answer if they knew the location
        -  The person who can't answer is most likely the spy
        ''')
    InstructionsText.grid(row = 1, sticky = N)
    OtherInformation = Label(InstructionsRoot, text = "Other Information")
    OtherInformation.grid(row = 2, sticky = N)
    AmountOfPlayersInformation = Label(InstructionsRoot, text = "Minimum Amount of Player is 3, Maximum is 10")
    AmountOfPlayersInformation.grid(row = 3, column = 0)
    TimeInformation = Label(InstructionsRoot, text = "Suggested Round Time is 8 min")
    TimeInformation.grid(row = 4, column = 0)
    ExtraTimeInformation = Message(InstructionsRoot, text = '''
    Timing for Rounds can vary on personal preference and how the game is being played. If you have never played the game start off with 10 min. If yoy are an expert you can play at 6 or less minutes. Amount of players can also change how many minutes you should have. A large group of people means you should have longer rounds, and vice versa for a smaller group.''')
    ExtraTimeInformation.grid(row = 5, column = 0)

#Instructions Button
InstructionsButton = Button(root, text = 'Instructions', width = 10, command = instructions, highlightbackground = color)
InstructionsButton.grid(row = 0, column = 1)


#Start Game
############################### Start Game #################################
def StartGame ():
    PA = PA_num.get()
    TPR = TPR_num.get()
    PA = int(PA)
    TPR = int(TPR)
    PlayerRow = 5

    ## Changing Paramaters to match minimum game settings & Calling the addplayer function
    if PA < 3:
        minPlayer = 3
        AddPlayer(minPlayer, PlayerRow)
    elif PA > 10:
        maxPlayer = 10
        AddPlayer(maxPlayer, PlayerRow)
    else:
        AddPlayer(PA, PlayerRow)


    #These are still playable, although promt the user just incase
    if TPR > 15:
        print("This is going to be a long game")

    if TPR < 3:
        print("This is going to be a short game")

#Player Functions
    ########################### Solved use list instead of tuple (Tuple you can't redefine the values, list you can)


 
def AddPlayer (PA, PlayerRow):
    a = 1
    print("PA value: ", PA)
    #Labels to indicate player and corresponding number
    Label1 = None
    Label2 = None
    Label3 = None
    Label4 = None
    Label5 = None
    Label6 = None
    Label7 = None
    Label8 = None
    Label9 = None
    Label10 = None
    
    #Entry Boxes for Player Cards
    Reveal1 = None
    Reveal2 = None
    Reveal3 = None
    Reveal4 = None
    Reveal5 = None
    Reveal6 = None
    Reveal7 = None
    Reveal8 = None
    Reveal9 = None
    Reveal10 = None
    
    player_list = [Label1, Label2, Label3, Label4, Label5, Label6, Label7, Label8, Label9, Label10]
    reveal_card = [Reveal1, Reveal2, Reveal3, Reveal4, Reveal5, Reveal6, Reveal7, Reveal8, Reveal9, Reveal10]

    ## Cross Refrencing Instructions. Make sure that the parameters given are playable
    if PA < 3:
        print("There must be atleast 3 players")
        print("REFER TO THE INSTRUCTIONS: Setting to 3 players")
        instructions()
    if PA > 10:
        print("A game with greater than 10 people would take too long")
        print("REFER TO THE INSTRUCTIONS: Setting to 10 players")
        instructions()
    
    for i in range(PA):
        player_list[i] = Label(root, text = 'Player ' + str(a), bg = color)
        player_list[i].grid(row = PlayerRow, column = 0)
        if PlayerRow == 5:
            reveal_card[i] = Button(root, text = 'Reveal', width = 8, command = revealspy, highlightbackground = color)
            reveal_card[i].grid(row = PlayerRow, column = 1)
            PlayerRow = PlayerRow + 1
            a = a + 1
        else:
            reveal_card[i-1] = Button(root, text = 'Reveal', width = 8, command = reveal, highlightbackground = color)
            reveal_card[i-1].grid(row = PlayerRow, column = 1)
            PlayerRow = PlayerRow + 1
            a = a + 1






## Player Class
class player:
    def __init__(self, name, location, Job):
        self.name = name
        self.location = location
        self.job = job
    
    

        

        
        
        
#Start Game Button
StartGameButton = Button(root, text = 'Start Game', width = 10, command = StartGame, highlightbackground = color)
StartGameButton.grid(row = 3, column = 1)

#Location Buttons
LocationNum = len(locations)
LocationRow = 10
b = 1
b = int(b)
LLLabel1 = None
LLLabel2 = None
LLLabel3 = None
LLLabel4 = None
LLLabel5 = None
LLLabel6 = None
LLLabel7 = None
LLLabel8 = None
LLLabel9 = None
LLLabel10 = None

LLabel1 = None
LLabel2 = None
LLabel3 = None
LLabel4 = None
LLabel5 = None
LLabel6 = None
LLabel7 = None
LLabel8 = None
LLabel9 = None
LLabel10 = None
llocation_list = [LLLabel1, LLLabel2, LLLabel3, LLLabel4, LLLabel5, LLLabel6, LLLabel7, LLLabel8, LLLabel9, LLLabel10]
location_list = [LLabel1, LLabel2, LLabel3, LLabel4, LLabel5, LLabel6, LLabel7, LLabel8, LLabel9, LLabel10]
for i in range(LocationNum):
    llocation_list[i] = Label(root, text = "Location" + str(b), bg = color)
    llocation_list[i].grid(row = LocationRow, column = 0)
    location_list[i] = Label(root, text = str(locations_strings[i]), bg = color)
    location_list[i].grid(row = LocationRow, column = 1)

    LocationRow = LocationRow + 1
    b = b + 1
    


root.mainloop()
