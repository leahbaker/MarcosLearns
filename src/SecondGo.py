# ======================== 
# NEW CODE BASED ON COMMENTS
# Ignore everything else. We are finding out what the heck this string is and where it comes from and what to do with it. Thats it! 
# Do these IN ORDER and do not move on until the previous one is working. They build on each other. 
# ========================

#### TODO #1: Where are those "None" values coming from? Use lots of words! I know you know it!
# I went to PythonTutor and visualized the code. Still don't get why I'm getting the None value, cause, you know, I'm zpecial.
# Asked for help in PythoTutor. The way to not get None is to replace print by return. Funtions use return statements. If there's no reture, there's no (None) output. (I'ts easy how one forgets basic stuff, of course I knew this, its just that the big picture overwhelms me)

# Leah: That's exactly why you write this stuff out. You got it, you just need confidence you got it! Its exactly that. The goal of a function is to return something, NOT to display or print something. Most of the time you dont actually want functions you write trying to spit out values places, thats why learning testing is so important.  Lots of things are invisibile and can overwhelm you if you dont test.  Youd be shocked how many print statments (or the other language equivalents) there are floating around production code in companies. I use them all the time, just to see whats going on in the background to see why things are going wrong.  So yes, the short answer is that functions WANT to return something. You can use "pass" as the body of a funtion you dont want to fill in yet to avoid this. Otherwise, MOST of the time you should be returning something. 

# ========================

#TODO #2: Rewrite the function so that it shows you the string value but only prints one thing every time you run it, no more none. 

# Leah: SEE. You know this. :) 

leahString1 = "LEAH"
leahString2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa."
leahString3 = "* Im a Su Per WeirD ! $ St>ing :)"

def validate_string(str):
    return str

print(validate_string(leahString1))
print(validate_string(leahString2))
print(validate_string(leahString3))


# ========================

#TODO #3: New function! I know you figure it out below, but this is a new mini excercise. Breakin down finding if a string has spaces or not. First, we modify your above logic and we annotate. Second, we find error. Third, we find if a string contains a space!! 

string1 = "nospaces"
string2 = "l o t s o f s p a c e s"
string3 = "one space"
string4 = "           "

#Rewrite me, using these strings and annotate each line. Youll find your error quickly, I promise. 
#Return true if a string contains 1 or more spaces, false if not.
def contains_spaces(str):
    if ' ' in str:
        return True
    else:
        return False
# Is this correct? I feel like its the same I did last time. Maybe this time I'm using '_' correctly. 
# ASKED FOR HELP IN PYTHONTUTOR AGAIN (these guys are amazing) --> '' is empry string. '_' is space. Got it! (again, it's so obvious, it slips away from my mind :S)
# Leah: See? You TOTALLY knew that! I KNOW you knew that! Remember, if it seems heavy, stop and take a deep breath and think of it in the simplest possible terms. '' IS a string, its one I use fairly regularly infact. But it does not contain a space. 
        
string1spacecheck = contains_spaces(string1)
print string1spacecheck

string2spacecheck = contains_spaces(string2)
print string2spacecheck

string3spacecheck = contains_spaces(string3)
print string3spacecheck

string4spacecheck = contains_spaces(string4)
print string4spacecheck


# ========================

#TODO #4: Fill in reasoning

##### WHY I SUCK FOR ASCII ART: spaces, spaces ain't cool. We need stuff that fills in, otherwise we don't get boxes, or triangles, or whatever.
##### badString1 = "T H I S H A S S P A C E S E V E R Y W H E R E"

##### WHY I SUCK FOR ASCII ART: There needs to be some kind of regularity, othewise we might get a box, but the art's gonna be icky, not regular.
##### badString2 = "I have too many different, irregular symbols, please imagine me"

##### WHY I SUCK FOR ASCII ART: This one and the weird shit I answered in our last class is the same answer. My mistake. I meant that as its not composed by ASCII characters, and we want to get ASCII art, then the string isn't valid.
##### badString3 = "I'm probably not ASCII"

##### WHY I SUCK FOR ASCII ART: lol. This one and the last one are the same.
##### badString4 = "I REFUSE TO COPY THAT ABSURDITY"

##### WHY I SUCK FOR ASCII ART: I'm a different type. I'm no string. I'n not valid.
##### badString4 = "TODO"

##### WHY I SUCK FOR ASCII ART: <Answer Me. I see you ignorin' me. > I ran out of ideas! 
##### badString5 = "TODO"

# Leah: Valid :) I'll give you a few ideas to think on
# 1: What would you do if a string was empty?
# 2: What if what is input isnt a string at all?
# 3: Are their other ways a string can be "empty"? Hint, think about concepts (some of which have shown up in python already...) like null, none, void, nada, kaput. Is a='' the sane as a=None?
# ========================

#Leah shows strings vs booleans

imABoolean = True
imAString = "True"

def return_data_type(var): 
    print type(var)
    
return_data_type(imABoolean)
return_data_type(imAString)

# Question about this: here you are using a print statement. Why doesn't this function print none?
# You missed my non obvious question. So I'm moving it down. :P