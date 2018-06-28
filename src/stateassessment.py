# ========================================================================================
# Marcos first assignment! Loosely structured because I'm making this up as I go along.
# 
# Instructions in README, you'll want to read that first.
#
# ~~~!!!PROJECT BUILD ASCII EVERYTHING ART!!!~~~
#
# This project is going to require using all the things you have learned so far.  Because Im not actually the worst, heres a short list:
#
# Ex. Data types, Operators, Functions, If statements, While loops, Lists, Indexing or Slicing, Operations on lists
#
# I'm going to give you a string of god knows what. You're going to create the methods that do all these lovely things with it.
#
# You can test at the bottom of this file. Make your own crazy strings and test if your code works. Remember, all you have to do is run python stateassessment.py! When in doubt, print stuff. SEE what you are working with, dont let your data be ambiguous.
#
# Oh yeah, I forgot, no questions! :) If you have a question put it in the file I have made for you called Questions.txt.  Even if you answer it, leave it in. 
#
# HINT 1: Remember you can print out lists and strings and other properties if you are questioning yourself
# HINT 2: This project can be done entierly with things youve used in projects already. If you find yourself googling off on a tangent, pull it back in.
# HINT 3: Make sure this mystery input string passes the validate test and gets placed into CURRENT_LIST before doing anything with it. 
# ========================================================================================

VALID = True
CURRENT_LIST = []
CURRENT_BOX = []
CURRENT_TRI = []
CURRENT_FIXED_WIDTH_BOX = []


#LEAH: First, you want to validate the string's contents. It can be anything, all you know is that it is a string. If the string "passes" your tests, flip VALID to true. Else it can remain false, and then return that value to use in the next method.
# def validate_string(str):
    # ok, here we go. Trying to understand what I gotta do with this
    # so I know there's a string somewhere and it's gonna be used in this function. But what do I have to do with it? To be continued next chapter XD
    # from the top of my head, the first thing I think about is that in order to validate something, that something has to look like something else I should stipulate first. So probably this is gonna need to be a boolean. Something like --> if str == my_string, return True.
    # Typing that last comment I realized that the variable in validate_string is a type, not a string (I mean its not a variable that holds a string, and it's not a string in itself).
    # Ohhhh. Does that mean that ANY string that goes through this function should return in a different shape? That makes sense. Like you said on slack, maybe if the function receives "LEAH" and has to create a box, it should return: LE
    #           AH - In that case I could use .format but its probably not the best way to do this (I've tried to do it that way and Jason[tutor]) said I should try otherwise. 
    # I'm writing too many comments and no code.
    # The problem is I still don't understand what the guidelines are for me to know what format the resulting string should have. Maybe this exercise gets its ideas from the exercise I showed you. I'll check that.
    # Maybe you mean that str should change into multiple lines following a given format. This is again what I don't get. What's the format I should follow? Stuck here again.
    # Argentina's playing the worldcup and I GOTTA watch the game.
    # I'm back. We lost. We're lost. Ralized that PROABLY by 'str' you mean just a regular string and not a type as I said before. And probably this doesn't have to be a boolean. Well, it could be. That depends on what the function will do. If the funcion will only check if a string has a certain format, then it's gonna be a boolean. If it will rearrange the string so as to create a new format, then it's gonna be something else, something a bit more complicated. I need to know that before continuing. 
    # Maybe when you gave the example of the triangle created by numbers and box created by letters you meant that 'L E A H' wasn't a valid string because if we want to make a triangle out of strings, then the string should have an odd number of indexes (actually since indexes are 0-based, it should have an even number of indexes so as to be odd)
    # If you did mean that, then I'll try to write some code cause this is too much commenting:
    # box = None 
    # triangle = None 
    # Ok, now I'm confused again. I want to specify that if the number of indexes in the string is odd and the shape we want is a square, then the string is valid. And if it's even and we want a triangle, then it's valid. Reading this comment maybe I need to make a boolean with 2 needed parameters. I'll just write the code that I'm imagining here:
  # if len(str) % 2 != 0 and   this was code 
    # Maybe if it's a square or a triangle is not that important for our purpose. But it has to be. If it wasn't, then any string would be valid, so that makes no sense. I have to define what makes a square True and a triangle True. Wait, I think I juts realized it. Maybe it's correct having created a None for boz and a None for triangle. This is what I'm thinking:
    # if len(str) % 2 != 0:
    #     box == True
    # if len(str) % 2 == 0:
    #     triangle == True
    # else:
    #     box == False # this makes no sense, and it's probably not correct, I don't know if I can have two variables like
    #     triangle == False # this in an else statement. I'm just not deleting code as you told me to.
    # return box  -- this was code
    # return triangle -- this was code
    # Continuing with my last comment, I should probably merge box and triangle into one variable, so as to be able to return it (I can't return 2, can I? Maybe I can, I'll try) --> yeah, Python says 'unreachable code', so it won't get to the second return statement :(
    # how bout this?:
    # return box, triange -- (this was code) problem with this is that I will have two results and I only want one. Should change the code a little bit:
    # if box == True or triangle == True:
    #     return True
    # else:
    #     return False
# print(validate_string('hello')) # --> this prints False. I don't know if my code is wrong, or if I'm just not getting the basics and therefore my code is just not correctly oriented because of that first important mistake

# ===== 2nd try:

def validate_string(str):
    if '' in str:
        return False
    else:
        return True
# so I basically did what I had done in FirstGo.py. Thinking if there are any other situations (besides spaces) when strings wouldn't be valid ...        
        

#LEAH: Put your string into a list! Specifically, the final value CURRENT_LIST I have made for you above that starts as an empty list and will hold whatever the current string you are using. One element per list spot. Return the list. I know there are cheat ways to do this, use logic :) Make sure to check the valid boolean first! If the boolean isnt valid, return a print statement that says "Leah is a super mean teacher". Otherwise, return your list (CURRENT_LIST).
def str_to_list(bool, str):
    pass


#LEAH: Now time to do something with this list. So this list can have one thing in it or 47 or 1908472. Make the most even box you can out of what you have. For example, if you have one element, youll have a 1x1 box. 5 elements mean a 2x2 box, the last character remains unused. Remember, width = height so you want the biggest value you can make with what you have. If you get stuck on making the box, try just printing the first line of the box. So for example a strong of 107 astrics make a 10x10 box of astrics but if you cant get the nesting working, try for getting the math and logic working and print just a line of 10 astrics. Return your box or line or whatever you got goin on. Made you a final CURRENT_BOX to dump your results into. Yes I know Im using final values poorly, leave me alone :P.
def create_box(list):
    pass


#LEAH: Now build on the above! Make the biggest triangle you can. Remember, each line on a triangle is 2 more than the last. 1, 3, 5, 7, etc. Again like above, if you cant get nesting working dont stress, try just printing the first line. Return the CURRENT_TRI list.
def create_triangle(list):
    pass



#LEAH: Box with a twist! It also takes in a width! So if the string is 10 astrics and the width value input is 3, youd be making a 3x3 out of 9 astrics and throwing away the last one. Dont forget, if the width is larger than the string can handle you have to handle that! (A Print statement of any degree will work).  Otherwise return the CURRENT_FIXED_WIDTH_BOX. Nested or first line or whatever you can is cool. 
def create_box(width, list):
    pass


#LEAH: Come up with a shape! Or an anything. Just something that is your own.  Do this very last, you may not even want to go near it. It's another step forward in the process. 
def create_marcos_choice(height, width, char):
    pass