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

VALID = FALSE
CURRENT_LIST = []
CURRENT_BOX = []
CURRENT_TRI = []
CURRENT_FIXED_WIDTH_BOX = []


#LEAH: First, you want to validate the string's contents. It can be anything, all you know is that it is a string. If the string "passes" your tests, flip VALID to true. Else it can remain false, and then return that value to use in the next method.
def validate_string(str):
    pass


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