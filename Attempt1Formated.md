
# MarcosLearns Attempt 1 Notes
*We are going to cut back for the second try to JUST string validation. Youll see why in a bit!*
*Practice TODO's for this section are in FirstGo.py*

##### LEAH PRE ASSIGNMENT INSTRUCTIONS: First, you want to validate the string's contents. It can be anything, all you know is that it is a string. If the string "passes" your tests, flip VALID to true. Else it can remain false, and then return that value to use in the next method.
*Pulling the important words from above just scanning: "validate, passes, any string content, flip VALID, remain false".  Im careful with the words I use here, they will help you if you piece them out. Always start by doing that.  You dont have to break them down, just make a list of the key parts you think are important.*

`<def validate_string(str):>`

##### 1: ok, here we go. Trying to understand what I gotta do with this
*Good start! Great tip, roll it ALLLLLL the way back, as far back as you can get it. You know how you can keep breaking matter down until you are splitting atoms? Do that! Read the whole problem once and then start breaking it down once you understand the whole goal. I strongly recomend doing this one a white board or a notebook. In fact just GET a white board if you dont, its like 20$ on amazon and it will help a lot. So for this problem, youd read it and say "ok the high level goal is to take a string and make some ascii shapes. Let me break it down now". So now we go to the first function. In this case its called validate string. So you know the goal of the project is to take a string (dont worry about what and where yet) and turn it into some shapes. So this is probably validating this string right? Ok so we are that far, we know this function takes in a string as a parameter and validates the string. Or if you want to think of it this way, its just a set of instructions for a certain condition. So say you give your calcualtor a number plus another number, you expect it to return the sum right? Well, somewhere sometime someone told the caluculator how to do that. So the calculator says "AHH WE HAVE A PLUS OPERATOR WHAT DO I DO?". The function for adding would say alright dawg I need 2 numbers to give you an answer. So the calcualtor says here sure, and gives it two numbers. The add fucntion can now plug those values into its add function and get an answer based on those specific numbers, and then talk back with a sum.  So in this case youd have def add(num1,num2) and calcualtor knows to go there when it needs to add and knows it can hand over info and get the right thing back. So thats your function, parameters, and return the sum.  Applied to our case, this function validates whatever string the user types in. Users do funny stuff. They dont always give you reasonable stuff, and you have to plan for them to be a dick and give you 100 spaces as a string. This function makes sure whatever string comes in (takes it in as a param)*

##### 2: so I know there's a string somewhere and it's gonna be used in this function. But what do I have to do with it? To be continued next chapter XD
*Good thinking. You got this far. You realize that theres a string SOMEWHERE that you have to do SOMETHING with in this function. You know its being passed into the function as a parameter. So, youve hit your first blocker. You dont know what this string is, where it come from, or what the heck to do with it. So... lets start out just printing it!*
###### TODO #1: Fill in function in FirstGo.py and print out the string in question so you can see what it is to demystify it a little. Do this before moving on, and ONLY do this. Dont look past it, just look at one, get one working, and come back here :) 


##### 3: from the top of my head, the first thing I think about is that in order to validate something, that something has to look like something else I should stipulate first. So probably this is gonna need to be a boolean. Something like --> if str == my_string, return True.
*Hey, good thought process! Way to pick out the word validate and work on trying to figure out what I meant by it! You didn't quite go the right direction, but thats ok! You are thinking right, just sometimes ended up with the wrong final solution. That I can help with! So lets start with what was absolutely RIGHT in your comment.  First, taking the funtion name and trying to figure out what to do with it with context clues.  Also, you nailed boolean! It is absolutely going to return a boolean.  Why?  Well. Imagine I wrote a method called validate_marco(MarcoPerson).  If I passed in you, youd want the validation method to say yep! true! greenlight! we checked, thats certainly a marco!. On the flip side, If I passed in me, youd want it to say NO BAD THATS NOT A MARCO, FALSE, WRONG. Thats exactly what we are doing here, but its whether or not the string is valid. We are getting to what that means.  Now the part where you sidetracked is the "looks like something I stipulate".  Nope! Easier! You, as the function, waits around to be called and passed in something. That something is the thing you are trying to check for valid properties. Again, we will get to what valid means, its part of a larger coding mentality and will get its own block.*
###### TODO #2: I have the calls set up for you. Make the funtion print true or false, true if the string that is put in is "true" and false if its anything else at all. Go finish that and then come back here! 


##### 4: Typing that last comment I realized that the variable in validate_string is a type, not a string (I mean its not a variable that holds a string, and it's not a string in itself).
*YES! :) Its basically saying hey validate function! When you are called, someone needs to put a string in this spot. Otherwise break everything because thats not what we said we needed to use us. It is only saying a string must go here when called*


##### 5: Ohhhh. Does that mean that ANY string that goes through this function should return in a different shape? That makes sense. Like you said on slack, maybe if the function receives "LEAH" and has to create a box, it should return: LE
*Well, any string runs though this function will return true if its "valid" and false if its "invalid".  Get the shapes out of your head for the time being, no shapes. All we are going to do is take a user input string and say yes this is a valid string to make a shape eventually or no this is not valid, we aint doin it.  The only thing this funtion does is tell you true or false, no shapes yet :).  Remember, dont get ahead of yourself. Break it into little pieces and tackle them first. Then use the small stuff to build the bigger stuff!*


##### 6: AH - In that case I could use .format but its probably not the best way to do this (I've tried to do it that way and Jason[tutor]) said I should try otherwise.
*While .format is indeed a thing, we dont need it for now, all we need is a boolean.  And Jason is right, but since we arent doing anything but looking at a string and giving it a thumbs up or thumbs down, we will forget that for now. To be covered when we get there.*


##### 7: I'm writing too many comments and no code.
*No, you did exactly what I asked you to do, you got your whole thought process down on paper.  It was perfect, dont second guess yourself! :)*


##### 8: The problem is I still don't understand what the guidelines are for me to know what format the resulting string should have. Maybe this exercise gets its ideas from the exercise I showed you. I'll check that.
*AHA. Remember how I said this hits on a fundamental programming concept and deserves its own block? Welcome to the block! :) So lets roll it way back and think conceptually in general. Think about all the times a program of any sort wanted you to give it anything, like typing in your log in info.  How many times have you put .gmai instead of .gmail. Did it yell at you instead of letting you into your account? God, I hope so. Thats because the programmer behind the wall sat and thought about ALLLLL the dumb crazy things people could type in that arent....drumroll please... VALID! :) So valid in this case is typing in a real email address. If my email is leah@leah.com and I type in leahleah.com OR leah.com OR leah@lea.com all those are INVALID email values right? You want to NOT let this person in, you want to show them an error message. So in this case, some of the things that make an email VALID are things like having an @, being from a real domain, containing the .com (or . whatever... more cases to check!). You know wy this is the example? I had to build it a week ago. This is real world stuff.  Youll be expected to anticipate users putting in something that doesnt work and handle those cases. Thats EXACTLY what this function does. But for strings that make art*
###### TODO #3: Go think hard until you come up with AT LEAST 5 things that would invalidate a string. Ive given you a freebee, spaces should invalidate a string. Space is a real ASCII value, it will be put into your art in the spot it should be placed and it will mess it up because it will look like you missed a space. So thats one, come up with 4 more that you think MIGHT make a string INVALID FOR OUR APPLICATION (remember, that means can the string build ascii art that wont suck!). Don't worry, I'll walk you though the common ones, I just want you to give it a shot first. Dont forget to leave comments! 


##### 9: Maybe you mean that str should change into multiple lines following a given format. This is again what I don't get. What's the format I should follow? Stuck here again.
*Simpler! No formats or anything yet. Alllll we are doing is saying if its a usable string or not.*


##### 10: Argentina's playing the worldcup and I GOTTA watch the game.
*Understandable, I hear thats a thing haha*


##### 11: I'm back. We lost. We're lost. Ralized that PROABLY by 'str' you mean just a regular string and not a type as I said before. And probably this doesn't have to be a boolean. Well, it could be. That depends on what the function will do. If the funcion will only check if a string has a certain format, then it's gonna be a boolean. If it will rearrange the string so as to create a new format, then it's gonna be something else, something a bit more complicated. I need to know that before continuing. 
*AHA Good thinking here! You were talking yourself back to the right path! Yes, if all it does is check a "format" (contains valid content), its going to be a boolean. Whichhhh is exactly what its doing! Is this an ok string to use? TRUE. Is this an ok string to use? FALSE. Thats its only job.  No rearranging, the string makes it though this funtion COMPLETELY unchanged. Youre just checking it out, not editing it at all. You made it more complicated than it needed to be, dont get ahead of yourself, slow and steady!*
###### TODO #4: Go answer the question with all the thoughts you have in your brain. Then head on back. 


##### 12: Maybe when you gave the example of the triangle created by numbers and box created by letters you meant that 'L E A H' wasn't a valid string because if we want to make a triangle out of strings, then the string should have an odd number of indexes (actually since indexes are 0-based, it should have an even number of indexes so as to be odd)
*Not quiteeee, we handle excess character's in the strings. But this is definitely a good start on thinking about it. But if youll notice, this is the third time Ive said this... dont get ahead of yourself! This is a surefire way to get overwhelmed. Just focus on validating a string for now.  Bite sized chunks.  Also trying to show you at what points your brain started trying to think of the WHOLE project and how thats when you are most sidetracked.*


##### 13: If you did mean that, then I'll try to write some code cause this is too much commenting:
*Ey, way to take a crack at it. No shame in that.*


`<box = None>`
`<triangle = None>`
*Nope! No shapes! 0 shapes! Only strings. Justttttt strings*


##### 14: Ok, now I'm confused again. I want to specify that if the number of indexes in the string is odd and the shape we want is a square, then the string is valid. And if it's even and we want a triangle, then it's valid. Reading this comment maybe I need to make a boolean with 2 needed parameters. I'll just write the code that I'm imagining here:

`<if len(str) % 2 != 0 and>`
*Of course you are confused! You are trying to write the whole project into the validate string method! :) Methods are seperate blocks because they all have a point. They have a start, they do some stuff, and then a result.  The start of validating a string is a string. The stuff it does is tests the string for the stuff you come up with that you deem invalid. The result is a boolean true or false value that lets us know if the string that was input is usable or not.  If it is, we can move on.  If it is not, we will need to show the customer an error or something. Thats in the future but I want to make sure you are thinking about the scope of this funtion beginning to end.  

##### 15: Maybe if it's a square or a triangle is not that important for our purpose. But it has to be. If it wasn't, then any string would be valid, so that makes no sense. I have to define what makes a square True and a triangle True. Wait, I think I juts realized it. Maybe it's correct having created a None for boz and a None for triangle. This is what I'm thinking:

`<if len(str) % 2 != 0:>`
`<box == True>`
`<if len(str) % 2 == 0:>`
`<triangle == True>`
`<else:>`
`<box == False # this makes no sense, and it's probably not correct, I don't know if I can have two variables like>`
`<triangle == False # this in an else statement. I'm just not deleting code as you told me to.>`
`<return box  -- this was code>`
`<return triangle -- this was code>`
*NOOOOO you thought it, I saw where you started thinking it, and then you cut it off to focus on the "bigger picture" of the project. And HERES the kicker: "If it wasn't, then any string would be valid". Nope. Not at all! Strings can pretty much hold anything. Can you make a shape out of 10 spaces? Because 10 spaces is a valid string! No box. No triangle. Only Zuul. I mean string. Only string. Think of it this way. Later if you want to validate strings elsewhere for some reason, you might be able to resue this. If you put boxes and trianges into it and stuff its useless.  Always stop and write down three things for each funtion: Start, Middle, Result.  Start is what happens when its called. So for this, its called with a string passed into it with the intention of validating that string. The middle, or do stuff part, validates the string for use.  The end is reporting back and telling us if it can or cant be used. Thats ALL this function does.  Ahead of yourself again, no wonder you are confused! You are trying to put the whole project in the first small funtion.*


##### 16: Continuing with my last comment, I should probably merge box and triangle into one variable, so as to be able to return it (I can't return 2, can I? Maybe I can, I'll try) --> yeah, Python says 'unreachable code', so it won't get to the second return statement :( how bout this?:

`<return box, triange -- (this was code) problem with this is that I will have two results and I only want one. Should change the code a little bit:>`
`<if box == True or triangle == True:>`
`<return True>`
`<else:>`
`<return False>`
`<print(validate_string('hello')) # --> this prints False. I don't know if my code is wrong, or if I'm just not getting the basics and therefore my code is just not correctly oriented because of that first important mistake>`

*Very well done, this is very much where you started rabbit holing and you cut it off.  Good self awareness.  This gives me a headache, no wonder you were frustrated. Reel it WAYYYYYYYYYYY back in. WAY back :)*

*Final TODO: get the method to the point where it is validating strings. Dont freak! Ill be here along the way once you tackle the above.*

##### ========== WE STOPPED HERE =============

### QUESTIONS (Keep adding to that file, I'll answer them in each relevant attempt file)
##### 1. I don't fully understand how to run tests in the console. 
*We will get to tests.  My goal is to strip away all the outside stuff for the first go of it so we can get you thinking the right way.  They are coming soon! But pretend they dont exist just for now*
##### 2. I don't know how to run stuff outside the console (can I?)
*You can! Python is cool, its a scripting language. You can do all sorts of funky stuff with it. This is another one that is good to ask but coming later. Definitely something we will cover. For now, stick to the easy way so we can get your thinking in the right logic path*