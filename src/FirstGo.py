# ======================== 
# NEW CODE BASED ON COMMENTS
# Ignore everything else. We are finding out what the heck this string is and where it comes from and what to do with it. Thats it! 
# Do these IN ORDER and do not move on until the previous one is working. They build on each other. 
# ========================

#TODO #1: Im going to give you three strings. Use validate to just print out the value of those strings.

leahString1 = "LEAH"
leahString2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa."
leahString3 = "* Im a Su Per WeirD ! $ St>ing :)"

def validate_string(str):
    print(str) # print str

#call function 3 times, once with each string. check out the strings printed! 
print(validate_string(leahString1))
print(validate_string(leahString2))
print(validate_string(leahString3))

# Output is: 
# LEAH
# None --> I don't know where this None comes from
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa.
# None --> this one probably comes from second function with no return statement
# * Im a Su Per WeirD ! $ St>ing :)
# None --> this one also probably comes from another function with no return statement

# ========================

#TODO #2: This is going to print true or false based on whether or not the string is "true" or not.

leahString1 = "true"
leahString2 = "false"
leahString3 = "True"

'''def validate_string2(str):
    #return true if string is "true" and false otherwise
    # I think its correct to just write "if str" right? Its the same as saying "if str is True"
    if str:
        return True
    else:
        return False ''' #this was code


'''print(validate_string2(leahString1)) #should print true! --> printing True
print(validate_string2(leahString2)) #should print false --> printing True :(
print(validate_string2(leahString3)) #should print false --> printing True :( 
                                                            # it does make sense that they're ptrinting TRUE, though, cause I just told the function to return True if str is True, and they're all strings ... '''

# OK SO IT TOOK ME ALL THIS TIME TO FINALLY UNDERSTAND THAT WHAT'S WRONG WITH STRNIGS 2 and 3 IS THAT THEY'VE GOT SPACES.
# SO I WILL REWRITE THE FUNCTION:

'''def validate_string2(str):
    if '' in str:
        return False
    else:
        return True ''' # this was code

'''print(validate_string2(leahString1)) #should print true! --> printing False :(
print(validate_string2(leahString2)) #should print false --> printing False :)
print(validate_string2(leahString3)) #should print false --> printing False :) '''

#Why am I getting True for all 3 of them?!?!?!?!?!?! WHAT THE FUCK?!?!?!
#Sorry didn't mean to say that. It's just that I wrote in the function that IF SPACE IS IN string, then RETURN FALSE, and spaces exist in strings 2 and 3
# Just tried the function with if ' ' in str (with a space) instead of '' and now I get thery're all True!!! i must be making a mistake with str. It's not "a string". It's the type of string, if I understood correctly.
# AND NOW I JUST REALIZED THAT leahstrings changed from TODO1 to TODO2. And I also just realized that what you meant in this exercise was that IF THE STRING == "true" then return True. The answer was there all along, I just read too fast, my brain doesn't like to slow down. When you said "true" between the inverted commas you were just saying that the string had to be just that ("true" with no cappital T). So this should work:

def validate_string2(str):
    if str == 'true':
        return True
    else:
        return False
        
print(validate_string2(leahString1)) #should print true! --> printing True :D
print(validate_string2(leahString2)) #should print false --> printing False :)
print(validate_string2(leahString3)) #should print false --> printing False :) '''
# Now I got it!!!
# ========================

#TODO #3: Think of 4 more things that might be true of a string that would fail to make ASCII art or make it icky

#WHY I SUCK FOR ASCII ART: 
badString1 = "T H I S H A S S P A C E S E V E R Y W H E R E"

#WHY I SUCK FOR ASCII ART: 
badString2 = "I have too many different, irregular symbols, please imagine me"

#WHY I SUCK FOR ASCII ART: 
badString3 = "I'm probably not ASCII"

"g̷̛̠̣͒̃͆̈́̃̆͝ŕ̴̡̫͎͓̌̀̌̓̀̈̊́ḑ̵̢̠̤͔̯̞̫̞͚̦̣̣͚̃͂͌̈͠f̶̭̝̫̠̆͛͌͒̆͋̑̒̏̾̃̿̕͝͠ͅg̵̡̨͎̈̊͑̎̐͌͗̎͌̔̾̅̕͜d̸̳̬̻͇͉̹̜̦̺̖̲̘͙̪̑͒͋̈́̈̑̾̃f̶̨̆̎g̸̢̧͈̼̣̪͈͇̳̟̭̓̈̋̄̔͐̐̐̔͘ḑ̷̹̞̙̼̤̠͔̗̘̈͛̆̑̌̉̄̽̄̌͗̆̕ͅͅf̶̤̤̱̮͖̻̫̣͉́̾̽͐̌͒̿̄̑͗g̸̛̞̹̙̲͇͍̈́̎͂̄̄̚͠ͅd̷̫̀̇͐̋̆̀͛͌͊̑͌f̵̩̈̉g̶̢̢͈͈̫͎̱͐̆́͆͂̈́́̑͛̽͘͘͝͝d̴̹̲̰̼̓̓͆̔̊͑͗͊̽͂ḟ̴̖͎̜͛̀̍͊͆͛͗͗̏͠͝ģ̶̫͈̪͉̘͍̆̄͋́̅̐͘͝t̵̛͖̪̟̙̰͈̝̜̖̼̞̗̃̅̇̑́͆̔̂͆͜͠͝ͅͅe̸̜̣̜̘̓͐́̌̔̓̉͆̊̿́̈́̄̈́̚ͅr̵̨̻̲̺̲͚̮͍͛̋̾̈̎͗̂͊͝t̷̞͖͒̐͛͑̃͝ȩ̶̙̯̲̠̩͇͔̖̀̾̀̾̎͒̉ŕ̸̛̯̲̼̥̥͚̋͛̓́̉̽̍̚͘͜t̵̩̦̙̃̀̀̍́̔̽̾͋͋̑̌͝͝e̸̛̹͙̓̌͐̉̈̈́́r̷̢̧̰͇̤̟̳̣̘̦̭͈̟͑̍͛̾̆̒̋̈́͌̍͠t̴͈̲̘̖͒͐̎͗̿̓̊͌̋̾̆́̚̕e̵̪̖̰̻̳͇̱̫̫̞̗͚͇̔̎͂͗̀͑̾̾͂͠ř̵̥̳̓t̶̓͝""

#WHY I SUCK FOR ASCII ART: 
badString4 = "TODO"

#WHY I SUCK FOR ASCII ART: 
badString5 = "TODO"


# ========================

#TODO #4: Given the information that the user will be typing in a string to use to make art, why might we want to "validate it" before trying to turn it into art?

#ANSWER: Cause you can't make something out of stuff that don't make that something. Let me rephrase that: if we assume that the final art that we are going to create is a painting, then we need paint. We can't make ou art with a guitar because we don't want music when we're done, we want paint in a painting. If someone gives us a guitar then its invalidated. If they give us paint, then its validated. In our excercise, that means that if we get a string, then its valid. But if we get a bool, or an int, or a list, etc, then its not valid. Someone could also give us some paint that doesn't work, maybe cause its expired. That's the case with strings with spaces (correct type but wrong string).