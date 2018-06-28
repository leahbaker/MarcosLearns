# ======================== 
# NEW CODE BASED ON COMMENTS
# Ignore everything else. We are finding out what the heck this string is and where it comes from and what to do with it. Thats it! 
# Do these IN ORDER and do not move on until the previous one is working. They build on each other. 
# ========================

#### TODO #1: Where are those "None" values coming from? Use lots of words! I know you know it!

# ========================

#TODO #2: Rewrite the function so that it shows you the string value but only prints one thing every time you run it, no more none. 

leahString1 = "LEAH"
leahString2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa."
leahString3 = "* Im a Su Per WeirD ! $ St>ing :)"

def validate_string(str):
    pass

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
    return True
        
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

##### WHY I SUCK FOR ASCII ART: <Answer Me>
##### badString1 = "T H I S H A S S P A C E S E V E R Y W H E R E"

##### WHY I SUCK FOR ASCII ART: <Answer Me, more words>
##### badString2 = "I have too many different, irregular symbols, please imagine me"

##### WHY I SUCK FOR ASCII ART: <Answer Me, more words>
##### badString3 = "I'm probably not ASCII"

##### WHY I SUCK FOR ASCII ART: <Answer Me, more words>
##### badString4 = "I REFUSE TO COPY THAT ABSURDITY"

##### WHY I SUCK FOR ASCII ART: <Answer Me. I see you ignorin' me.>
##### badString4 = "TODO"

##### WHY I SUCK FOR ASCII ART: <Answer Me. I see you ignorin' me.>
##### badString5 = "TODO"

# ========================

#Leah shows strings vs booleans

imABoolean = True
imAString = "True"

def return_data_type(var):
    print type(var)
    
return_data_type(imABoolean)
return_data_type(imAString)


