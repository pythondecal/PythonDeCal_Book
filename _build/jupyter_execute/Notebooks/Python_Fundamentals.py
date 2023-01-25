#!/usr/bin/env python
# coding: utf-8

# # Python 101: The Basics
# 
# This is a resource designed simply for your reference on how the basics of python work. Feel free to look at this notebook if you get stuck working on the homework at all.
# 
# Note: a comment is denoted by `# ____ `, python ignores anything after the `#` which allows us to comment our
# code and explain what parts of the code are doing

# ## Data Types
# 
# There are a few important data types within python. Let's get acquainted with them!

# ## Floats and Integers
# Floats are essentially just numbers with decimals included, even if the decimal is just a .0 on the end

# In[1]:


30.0
30.549820
28.75
1e6 #The e6 means 10 to the 6


# Integers are just numbers without decimals

# In[2]:


30
45
213
2340328


# You can do math with combined integers and floats, this will just give you a float

# In[3]:


20.5+45
45-20.5


# In[4]:


10**3 #making the exponent an integer makes the answer an integer


# In[5]:


10**3.0 #making the exponent a float makes the answer a float


# ## Strings
# Strings are not numbers, strings are collections of letters that can be manipulated through arithmetic expressions

# In[6]:


'I love Astrophysics' #is a string

#But you need the quotes to make the string

I love Astrophysics #gives you an error as it reads this as actual code


# In[7]:


print('a'+'b'+'c') #You can add strings

print(2*'a') #repeat the same letter multiple times

print('a' * 'b') #can't multiply strings -> Error


# You can index into strings to pull out a specific letter

# In[8]:


name = 'Raphael'

#treat it like a list of letters, all the same indexing style. (0th index means first letter)
print(name[0]) #pulls out the first letter
print(name[4:6]) #pulls out the 4th through 6th letters
print(name[-1]) #pulls out the last letter


# ## Lists & Tuples
# 
# A list is a way to store several data types or items in one place for easy access. For example, it might be useful to make a list of important stars that you want to look up later. A tuple is the same as a list except you cant edit it. The reason you would want a tuple over a list is that they take up less memory on the computer and are easier for the computer to work with.

# In[9]:


stars = ['betelgeuse', 'proxima centauri', 'cal-star', 'sirius', 'Stephenson-143A'] #list

print(stars[0]) #print out the first item in the list (notice lists start with 0 as their first item's index)
print(stars[2])
print(stars[1:3])
print(stars[-1])


# In[10]:


names_tuple = ('james', 'ayla', 'emily', 'yilun', 'raphael') #tuple
names_list = ['james', 'ayla', 'emily', 'yilun', 'raphael'] #list

names_list.append('mariska') #you can append items to a list

print(names_list)

names_tuple.append('mariska') #error because you can't append (aka edit) items to a tuple


# ## Booleans
# 
# Booleans is a fancy word for True or False. Pretty simple. You can use these as conditions for different loops and conditional statements (down below)

# In[11]:


my_bool = True
my_bool2 = False

if my_bool == True: #checks to see if my_bool is True
    print('yes')
else:
    print('no')
    
if my_bool2 == True: #checks to see if my_bool2 is True
    print('yes')
else:
    print('no')


# ## Dictionaries
# 
# These are like super fancy lists. They work just like a normal dictionary. For every key in a dictionary, you have its' corresponding value. Just like in a real dictionary, the key is the word you want and the value is the definition... but in python you can generalize it.

# In[12]:


words = {'python':'a coding language', 'UC Berkeley':'the number one public university!',
         'water': 'an organic compound responsible for life on Earth', 'Mars':'4th planet in the solar system'}

print(words['UC Berkeley']) #prints out the definition for UC Berkeley
print(words['water'])

# curly braces make it a dictionary, keys are followed by a colon and a value
# to acces a value in a dictionary you index with the name of the key


# ## Functions

# Functions in python are a piece of code that defines something which can be used elsewhere in the code
# 
# Python has 3 classes of functions:
# -  built-in functions, e.g. print()
# -  functions from packages/modules, e.g. sin() from the math package(you'll learn about this later with numpy)
# -  user-defined functions.

# In[13]:


#Print statements and other built-in functions are relatively straightforward
x=5+3
print(x)


# In[14]:


#User-defined functions can do simple math or far more complicated processes
def triple(x):
    return 3*x # The final return must be indented
triple(1234)


# In[15]:


#You can define things within functions
def squared(x):
    y=x**2
    return y

squared(345)


# In[16]:


#You can have multiple arguments within a function
def absolute_val(x,y):
    return abs(x-y) #abs is a built in function
absolute_val(3,10)


# ## if/elif/else statements
# These are all conditionals, meaning they can be used to impose conditions within python. Conditionals are extremely useful because they allow one to account for several possibilities within their code. The easiest example of when to use them would be inside a function.

# To understand if statements, we can use this function which rolls a dice.
# If you roll a 6, you win. If not, you lose

# In[17]:


def roll_6(x):
    if x<6:
        return 'You Lost!'
    elif x==6: #elif means else if (like saying, okay if the "if" statement above fails, try this condition instead)
        return 'Victory!'
    else: #else is like the "if all else fails, do this" condition in your code
        return 'Not a Valid Roll'

roll_6(1) #change the 1 to a 6 and see what happens


# you can use else if you want to denote that in all other cases besides the if statmenet, the else statement should be true. Take a step function.

# In[18]:


def step_function(x):
    if x<=0:
        return 0
    else:
        return 1 
    
print(step_function(-2))
print(step_function(10))


# ## While loops

# While loops essentially impose a condition for which python will run until that condition becomes no longer true or is stopped. "While this condition is true, do this over and over again", so when the condition is no longer met the loop stops. Be careful, you may have heard of the "infinite loop" before... this is where it happens. What do you think would happen in the cell below if you forgot to add 1 to count each time?
# 

# In[19]:


#In this cell, adapted from physics 77, the while loop adds numbers until the condition is no longer met
sum = 0
count = 0
while sum < 49:
    sum += 5 # sum += 5 is short hand for sum = sum + 5 
    count += 1 
    print(sum) # the print makes sure you get an output
print(sum,count)


# In[20]:


#The break expression breaks the loop early if you want
sum = 0
count = 0
while sum < 49:
    sum += 5
    count += 1
    if count >=5:
        break
print(sum,count)
#while loops essentially can hold a condition and allow you to loop through huge sets of numbers


# ## For loops

# For loops impose a condition and loop through the index/range you give, similar to a while loop but more conventional. This loop is almost always used when you want to do a task to each item in a list, or for each item in a list. A good example of this might be when you have a python list with names of the people in our class and you wanted to check attendance. You could use a for loop to check if each name is in the zoom call.
# 
# A for loop is just a while loop in disguise basically

# In[21]:


students = ['james', 'ayla', 'emily', 'yilun', 'raphael']

for i in students: #i is just a dummy variable that keeps track of which item in the list the loop is on
    print('Here')


# In[22]:


for i in range(10): #range(10) is a built in function that makes a list of numbers from 0 to N-1 to iterate over
    print(i)
#you loop through some index and can pick out certain values


# In[23]:


#combine with if
for i in range(10):
    if i<4:
        print(i)
    else:
        print("greater than 3")


# Congratulations, you have now finished with some of the python basics! Continue to future notebooks/lectures for more details etc.

# Created by Raphael Baer-Way and James Sunseri. Some material adapted from Data 8 and Physics 77

# In[ ]:




