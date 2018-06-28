
# MarcosLearns Attempt 2 Notes
*You should only have this and SecondGo.py open! No other files open :)*
*Practice TODO's for this section are in SecondGo.py*


#### TODO #1: Im going to give you three strings. Use validate to just print out the value of those strings.

###### `<leahString1 = "LEAH">`
###### `<leahString2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa.">`
###### `<leahString3 = "* Im a Su Per WeirD ! $ St>ing :)">`

###### `<def validate_string(str):>`
######     `<print(str) # print str>`

##### call function 3 times, once with each string. check out the strings printed! 
###### `<print(validate_string(leahString1))>`
###### `<print(validate_string(leahString2))>`
###### `<print(validate_string(leahString3))>`

##### Output is: 
###### LEAH
###### None --> I don't know where this None comes from
#### TODO #1: Yes you do!!! Think. Why might something happen when you run this function AFTER you print?  You 100% know this! I believe in you! Go answer it in SecondGo.py


###### Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut mi orci, facilisis scelerisque urna et, imperdiet elementum massa.
###### None --> this one probably comes from second function with no return statement
#### TODO #1 cont.: I think warmer! Use more words in the SecondGo file


###### * Im a Su Per WeirD ! $ St>ing :)
###### None --> this one also probably comes from another function with no return statement
#### TODO #1 cont.: I think even warmer! Use more words in the SecondGo file.  You seem to understand that its happening consistently when this function is run and that it might have something to do with how funtions return.

#### TODO #2: Rewrite the function so that it shows you the string value but only prints one thing every time you run it, no more none. 

#### ========================

`<leahString1 = "true">`
`<leahString2 = "false">`
`<leahString3 = "True">`

`<def validate_string2(str):
    #return true if string is "true" and false otherwise
    # I think its correct to just write "if str" right? Its the same as saying "if str is True"
    if str:
        return True
    else:
        return False >`


`<print(validate_string2(leahString1)) #should print true! --> printing True>`
`<print(validate_string2(leahString2)) #should print false --> printing True :(>`
`<print(validate_string2(leahString3)) #should print false --> printing True :( >`
                                                            
##### it does make sense that they're ptrinting TRUE, though, cause I just told the function to return True if str is True, and they're all strings ... '''
*TRICKED YOU! True/False, Truthy/Falsy, 1/0 etc is a Boolean value. We are dealing in Strings! The computer sees the characters between the quotes as the character they are, not True or False. Those are "reserved words" unless its in ""s in which case it will be treated as a string. Dont believe me? Check out the bottom of SecondGo!*


##### OK SO IT TOOK ME ALL THIS TIME TO FINALLY UNDERSTAND THAT WHAT'S WRONG WITH STRNIGS 2 and 3 IS THAT THEY'VE GOT SPACES.
*YAY THATS ONE OF THEM! :) GOOD THINKING!*

##### SO I WILL REWRITE THE FUNCTION:

`<def validate_string2(str):
    if '' in str:
        return False
    else:
        return True>`

`<print(validate_string2(leahString1)) #should print true! --> printing False :(>`
`<print(validate_string2(leahString2)) #should print false --> printing False :)>`
`<print(validate_string2(leahString3)) #should print false --> printing False :)>`

##### Why am I getting True for all 3 of them?!?!?!?!?!?! WHAT THE FUCK?!?!?!
*Ahhhhhhhh this is a mistake I would find myself making. Talk yourself through every line and every character and what it does.  You are VERY close.*
#### TODO #3: New function! I know you figure it out below, but this is a new mini excercise. Breakin down finding if a string has spaces or not. First, we modify your above logic and we annotate. Second, we find error. Third, we find if a string contains a space!! 

##### Sorry didn't mean to say that. It's just that I wrote in the function that IF SPACE IS IN string, then RETURN FALSE, and spaces exist in strings 2 and 3
*Not only am I not easily offended, learning programming means swearing. It just does. Check it out again. Is that what you wrote?*

##### Just tried the function with if ' ' in str (with a space) instead of '' and now I get thery're all True!!! i must be making a mistake with str. It's not "a string". It's the type of string, if I understood correctly.
*REVISIT THIS. REEEEVISITTTTT THISSSSSSSS*

##### AND NOW I JUST REALIZED THAT leahstrings changed from TODO1 to TODO2. And I also just realized that what you meant in this exercise was that IF THE STRING == "true" then return True. The answer was there all along, I just read too fast, my brain doesn't like to slow down. When you said "true" between the inverted commas you were just saying that the string had to be just that ("true" with no cappital T). So this should work:
*Hey thats a thing. Part of what Im training you to do is slow down and break it down.  Im going to ramp up tiny attempts to see if you are paying attention as we go along. Told you youd hate me by the end. But youll learn and youll be good!*

`<def validate_string2(str):
    if str == 'true':
        return True
    else:
        return False>`
        
##### print(validate_string2(leahString1)) #should print true! --> printing True :D
##### print(validate_string2(leahString2)) #should print false --> printing False :)
##### print(validate_string2(leahString3)) #should print false --> printing False :) '''
##### Now I got it!!!
*There ya go! thinking in strings, recognizing your data types. Good going*


#### ========================

#### TODO #3: Think of 4 more things that might be true of a string that would fail to make ASCII art or make it icky

##### WHY I SUCK FOR ASCII ART: 
####TODO: Fill me in ^
##### badString1 = "T H I S H A S S P A C E S E V E R Y W H E R E"

##### WHY I SUCK FOR ASCII ART: 
####TODO: Fill me in ^. More words.
##### badString2 = "I have too many different, irregular symbols, please imagine me"

##### WHY I SUCK FOR ASCII ART:
####TODO: Fill me in ^. More words.
##### badString3 = "I'm probably not ASCII"

##### Marco does some crazy s*$#(!)$!t. Which Im keeping. To shame him. For this absurdity.
`
<
"
g
̷
͒
̃
͆
̈́
̃
͝
̛
̆
̠
̣
r
̴
́
̌
̀
̌
̓
̀
̈
̊
́
̫
̡
͎
͓
d
̵
̃
͂
͠
͌
̈
̠
̤
͔
̯
̧
̞
̫
̞
͚
̦
̢
̣
̣
͚
f
̶
̆
͛
͌
͒
̆
͋
̑
̒
͝
͠
̏
̕
̾
̃
̿
̭
ͅ
̝
̫
̠
g
̵
̈
̊
͑
̎
̐
͌
͗
̎
͌
̔
̾
̕
̅
̡
̨
͜
͎
d
̸
̑
͒
͋
̈́
̈
̑
̾
̃
̳
̬
̻
͇
͉
̹
̜
̦
̺
̖
̲
̘
͙
̪
f
̶
̆
̎
̨
g
̸
̓
̈
̋
͘
̄
̔
͐
̐
̐
̔
͈
̢
̼
̣
̪
̧
͈
͇
̳
̟
̭
d
̷
̈
͛
̆
̕
̑
̌
̉
̄
̽
̄
̌
͗
̆
ͅ
̹
̞
̙
̼
ͅ
̤
̧
̠
͔
̗
̘
f
̶
́
̾
̽
͐
̌
͒
̿
̄
̑
͗
̤
̤
̱
̮
͖
̻
̫
̣
͉
g
̸
̚
̈́
͠
̛
̎
͂
̄
̄
̞
̹
̙
̲
ͅ
͇
͍
d
̷
̀
̇
͐
̋
̆
̀
͛
͌
͊
̑
͌
̫
f
̵
̈
̉
̩
g
̶
͐
͘
̆
͝
́
͆
͂
̈́
́
̑
͘
͛
̽
͝
͈
͈
̢
̫
͎
̱
̢
d
̓
̓
͆
̔
̊
͑
͗
͊
̽
͂
̹
̲
̰
̼
f
̴
̇
͛
̀
̍
͠
͊
͆
͛
͗
͗
̏
͝
̖
͎
̜
g
̶
̆
̄
͘
͋
́
͝
̅
̐
̫
͈
̧
̪
͉
̘
͍
t
̵
͠
̃
̅
̇
̑
͝
́
͆
̛
̔
̂
͆
͖
̪
̟
ͅ
̙
͜
̰
ͅ
͈
̝
̜
̖
̼
̞
̗
e
̸
̓
͐
́
̌
̔
̓
̉
͆
̊
̿
̚
́
̈́
̄
̈́
̜
̣
̜
ͅ
̘
r
̵
͛
̋
̾
͝
̈
̎
͗
̂
͊
̨
̻
̲
̺
̲
͚
̮
͍
t
̷
͒
̐
͝
͛
͑
̃
̞
͖
e
̶
̀
̾
̀
̾
̎
͒
̉
̧
̙
̯
͛
̓
́
̛
̉
̽
͘

̯̍
̲
̼
̥
͜
̥
͚
t
̵
̃
̀
̀
͝
̍
́
̔
̽
̾
͋
͋
̑
͝
̌
̩
̦
̙
e
͐
̉
̈
̈́
́
̹
͙
r
̷
͑
̍
͛
̾
̆
̒
̋
̈́
͌
̍
͠
̰
͇
̤
̢
̟
̳
̣
̘
̧
̦
̭
͈
̟
t
̴
͒
͐
̎
͗
̿
̓
̊
͌
̋
̾
̆
̚
́
̕
͈
̲
̘
̖
e
̵
̔
̎
͂
͠
͗
̀
͑
̾
̾
͂
̪
̖
̰
̻
̳
͇
̱
̫
̫
̞
̗
͚
͇
r
̵
̌
̓
̥
̳
t
̶
̓
͝
"
"

##### </> Marco does some crazy s*$#(!)$!t

##### WHY I SUCK FOR ASCII ART: 
##### badString4 = "TODO"

##### WHY I SUCK FOR ASCII ART: 
##### badString5 = "TODO"


#### ========================

#### TODO #4: Given the information that the user will be typing in a string to use to make art, why might we want to "validate it" before trying to turn it into art?

##### ANSWER: Cause you can't make something out of stuff that don't make that something. Let me rephrase that: if we assume that the final art that we are going to create is a painting, then we need paint. We can't make ou art with a guitar because we don't want music when we're done, we want paint in a painting. If someone gives us a guitar then its invalidated. If they give us paint, then its validated. In our excercise, that means that if we get a string, then its valid. But if we get a bool, or an int, or a list, etc, then its not valid. Someone could also give us some paint that doesn't work, maybe cause its expired. That's the case with strings with spaces (correct type but wrong string).

*Fair. You indeed can not make something out of things that dont make something.  Think of it like little boxes like so: 

[] [] [] [] </br>
[] [] [] [] </br>
[] [] [] [] </br>
[] [] [] []

In order to build that shape you want to put SOMETHING in each of those boxes right? A space would leave a box empty which messes up your shape. ALSOOOOOOO you just named another issue we are going to want to validate for!!! Data type! We want to make sure what is passed in is a string at all! So right now we have two, is it a string, and does it contain spaces. There are a handful more, keep thinking for them, we will get there!*

##### ========== WE STOPPED HERE =============

### QUESTIONS (Keep adding to that file, I'll answer them in each relevant attempt file)
##### No new ones this time around :) 