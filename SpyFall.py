# BYU Semester 1 Capstone Project
# SpyFall game
# Using Tkinter



from tkinter import *
import tkinter.messagebox

import time



# Tkinter Settings
root = Tk()
root.title('SpyFall --- Loading Page')
root.geometry("700x500")
color = 'blue'
root.configure(bg=color)
root.resizable(width=False, height=False)






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

def StartGame ():
    PA = PA_num.get()
    TPR = TPR_num.get()
    PA = int(PA)
    TPR = int(TPR)

    ## Cross Refrencing Instructions. Make sure that the parameters given are playable
    if PA < 3:
        print("There must be atleast 3 players")
        print("REFER TO THE INSTRUCTIONS")
        instructions()

    if PA > 10:
        print("A game with greater than 10 people would take too long")
        print("REFER TO THE INSTRUCTIONS")
        instructions()

        #These are still playable, although promt the user just incase
    if TPR > 15:
        print("This is going to be a long game")

    if TPR < 3:
        print("This is going to be a short game")



    if PA == 3:
        #3 Player Game Page setup
        3PGRoot = Tk()
        3PGRoot.title('SpyFall --- 3 Players')
        root.geometry("400x400")
        color = 'blue'
        3PGRoot.configure(bg=color)

        
        
        
#Start Game Button
StartGameButton = Button(root, text = 'Start Game', width = 10, command = StartGame, highlightbackground = color)
StartGameButton.grid(row = 3, column = 1)



root.mainloop()
