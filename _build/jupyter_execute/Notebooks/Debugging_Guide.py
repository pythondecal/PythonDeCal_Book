#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import numpy as np 
from math import sqrt


# # Debugging Strategies
# 
# Hello, welcome to the Python DeCal debugging strategies notebook. This will serve as a great resource for those who are new to python and don't know how to fix code when it's not working. This is not an all encompasing resource for all the possible debugging tools, but it will walk you through the basics and make you feel more comfortable when an error pops up in your coding expeditions.
# 
# We break this notebook up into 4 sections. Section I serves as a walkthrough of the overal debugging process, Section II summarizes those steps into a cohesive list, Section III shows the most common types of errors that occur in scientific programming to help you anticipate them, and Section IV shows you how to write code that anticipates errors. Section IV is particularly useful if you wish to write code that is usable by someone other than yourself.

# ## I. Reading Error Messages

# Often times, the hardest part of learning how to debug is simply just understanding what all the red text means! We address that in this section with a workflow example. Below is an example of a common buggy code that was written hastly and needs some debugging treatment.
# 
# This is some code that makes use of a fun statistical fact that if we draw a quarter of a circle inside of a square and randomly throw some darts at the square, the ratio of darts inside the circle to the number of total darts thrown approximates $\pi/4$! 
# 
# <p align="center">
#   <img src="https://github.com/James11222/Python_DeCal/blob/master/DeCal_Images/darts_pi.png?raw=true" alt="monte pi", width=50%>
# </p>
# 
# This code is purposefully flawed. Let's try running the cell below and see what happens.
# 

# In[2]:


#-------------------------------------------------------
#                     Code Below
#-------------------------------------------------------


def throw_dart():
    """
    A function that effectively throws a dart, if it lands in
    the quarter circle we return 1, if not we return 0.
    """
    x, y = np.random.uniform(0,1, 2), np.random.uniform(0,1, 2) #giving each dart a random x,y position between 0 and 1
    if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5: #check to see if its in the circle
        return 1
    else:
        return 0


def estimate_pi(number_of_darts):
    """
    A simple function to estimate π using
    sampling from a normal distribution with num points.
    """
    number_of_darts_in_circle = 0

    for throw in range(number_of_darts):
        number_of_darts_in_circle += throw_dart()
        
    pi_approx = 4 * (number_of_darts_in_circle / number_of_darts)
    
    return pi_approx

#-------------------------------------------------------
#                 Executing the Code
#-------------------------------------------------------

estimate_pi(200000)


# Hmm, something is wrong here. This might be a bit daunting to read but fear not, we will walk through it. 
# 
# <p align="center">
#   <img src="https://github.com/James11222/Python_DeCal/blob/master/DeCal_Images/debugging_step1.png?raw=true" alt="debug step 1", width=70%>
# </p>
# 
# When reading these huge error statements it is important to first direct your attention the the very bottom of the statement. This will tell you what kind of error is occuring and a short summary of the problem. In this case a `TypeError` means we are using the wrong data type somewhere and we are trying to do an operation that doesn't make sense for the data types being used (an example would be `max(7)`, that would give a type error because you can't take the max of an integer). We also get a small sentence explaining the issue 
# 
# `TypeError: only size-1 arrays can be converted to Python scalars`
# 
# which immediately tells us something is funky with our use of arrays/lists and assigning them to variables. Often times if you have absolutely no idea what this sentence means, you can google it! Literally copy and paste that line into google and find a stack overflow page that might help. That would look something like:
# 
# 
# <p align="center">
#   <img src="https://github.com/James11222/Python_DeCal/blob/master/DeCal_Images/debugging_gif.gif?raw=true" alt="debug gif", width=70%>
# </p>
# 
# Typically there is atleast 1 other person in the world who has likely had the same question as you. It is a common joke/meme that software developers are just experts at using stack overflow for this very reason. Note that if you do end up using/copying code from one of these threads, it is a good idea to cite that thread to give credit to those who answered the question.
# 
# Another tool at our disposal is checking the stack trace. This means reading through the error message text above the final line. This is often really powerful and allows us to find exactly what lines of code are causing the problem. Let's go back to that original image we had earlier:
# 
# <p align="center">
#   <img src="https://github.com/James11222/Python_DeCal/blob/master/DeCal_Images/debugging_step2.png?raw=true" alt="debug step 2", width=70%>
# </p>
# 
# The purple serves as a guide for reading the stack trace. We start at the very top to find what line of code started the cascade of errors. Then we go down the stack (follow the arrows) which show what lines caused our original line to error. In the image above we see that line 36 (our `estimate_pi` function call), errored because of line 26 earlier in the code. This tells us line 26 has a problem, but since this isn't the final error in the stack trace it actually goes deeper. Since we are calling a function on that line `throw_dart()`, it is likely the error is coming from that function. If we keep going with the next arrow to see that line 12 seems to be the root source of error in our code. Line 12 does happen to be inside our `throw_dart` function, so this function has a bug in it! Let's fix it.
# 
# It appears that `x` and `y` aren't behaving as we think they should. We had originally planned for `x` and `y` to simply be a coordinate of a single dart. This means that `x` should be a `float` and `y` should also be a `float`. We can check to see if that is the case by adding a print statement to see what `x` and `y` really are. We have to do this **before** the line where we expect the error to occur. We know this error occurs in the if statement, so lets add the print statements before that so they will execute before the code errors.

# In[ ]:


def throw_dart():
    """
    A function that effectively throws a dart, if it lands in
    the quarter circle we return 1, if not we return 0.
    """
    x, y = np.random.uniform(0,1, 2), np.random.uniform(0,1, 2) #giving each dart a random x,y position between 0 and 1

    print("the type of x is: ", type(x)) #temporary debugging print statements
    print("the type of y is: ", type(y)) #temporary debugging print statements

    if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5: #check to see if its in the circle
        return 1
    else:
        return 0


throw_dart()


# Notice we didn't plan to fix the issue, simply diagnose it, so we will still see the error messages. Our print statements ran (above the error message) and they show exactly what data types x and y are. They are numpy arrays! Aha, let's fix that issue by looking at how we made `x` and `y`. We made them in this line
# 
# ```python
#  x, y = np.random.uniform(0,1,2), np.random.uniform(0,1,2)
# ```
# 
# we should probably check to see if we understand how `np.random.uniform()` works. You can simply just google that function string plus the word python right after and go to the documentation website. You would type something like
# `"np.random.uniform() python"`
# into google. Clicking on one of the first links:  https://numpy.org/doc/ gives us
# 
# <p align="center">
#   <img src="https://github.com/James11222/Python_DeCal/blob/master/DeCal_Images/numpy_doc.png?raw=true" alt="documentation", width=70%>
# </p>
# 
# By closely reading what each parameter/argument means in this function and looking at the returns. We see the third argument creates the size of an array! We don't want that, we just want 1 float value for each call so we need to just remove the 3rd argument to our function calls! Let's try it!
# 

# In[ ]:


#-------------------------------------------------------
#                     Code Below
#-------------------------------------------------------


def throw_dart():
    """
    A function that effectively throws a dart, if it lands in
    the quarter circle we return 1, if not we return 0.
    """
    x, y = np.random.uniform(0,1), np.random.uniform(0,1) #giving each dart a random x,y position between 0 and 1
    if sqrt((x - 0.5)**2 + (y - 0.5)**2) <= 0.5: #check to see if its in the circle
        return 1
    else:
        return 0


def estimate_pi(number_of_darts):
    """
    A simple function to estimate π using
    sampling from a normal distribution with num points.
    """
    number_of_darts_in_circle = 0

    for throw in range(number_of_darts):
        number_of_darts_in_circle += throw_dart()
        
    pi_approx = 4 * (number_of_darts_in_circle / number_of_darts)
    
    return pi_approx

#-------------------------------------------------------
#                 Executing the Code
#-------------------------------------------------------

print("π =", estimate_pi(200000))


# Voila! There we have it, we successfully debugged the code. This isn't the absolute best way to do it, there are other tools you can use that are meant to streamline this process but those typically require using applications like <a href="https://code.visualstudio.com">VS-Code</a>,  <a href="https://www.jetbrains.com/pycharm/">pycharm</a>, or debugging widget extensions. This is merely serving as giving you the absolute fundamentals of learning how to read errors and use them to help you fix your code. Feel free to add more darts and see how much better it approximates $\pi$!

# ## II. Debugging Strategies Summarized

# To summarize and add to the strategies in the previous section, here are some steps to follow when debugging your code: \
# 
# 
# 1.   **Read the error** 
# > * Find out what kind of error you have (such as a `TypeError`, `RuntimeError`, etc.)
#  * This will help you figure out how to start debugging
#  * If the error is one you are unsure about, look it up in the [list of errors](https://docs.python.org/3/library/exceptions.html) (or simply Google it 😎).
# 
# 
# 
#  2. **Locate the error**
# > * Follow the arrows in the outputted arrow to see which line is triggering the error
# * If there are multiple errors, the topmost one corresponds to the line which resulted in an error. The last error is the line that you actually need to fix.
# 
# 3. **Attempt to fix the error**
# > *   You may know exactly what needs to be fixed just by looking at the line. Other times, however, you may have no idea where to even begin.
# >* If you have an inkling of the root of the issue, utilize a print statement like in the above example. If a value is of a different type than intended or a loop is not performing as expected and so on, this will help you understand the issue further. 
# >* If you're completely stuck though (which happens more often than not), Google and StackOverflow are your best friends 😃.
# 
# And if all else fails, feel free to ask your peers, a mentor/professor, or even us instructors; we're always happy to help!
# 
# 
# 
# 
# 

# ## III. Different Types of Errors

# **Examples of Syntax Errors**
# These types of errors are the definition of "It is the small things that matter." On the bright side, Python immediately stops the running the code once it hits an error which makes life easier if you know how to read the error.
# 
# Exercise your error reading skill by trying the below examples and fix what is wrong.

# In[ ]:


# Just a few tweaks 
if ("your mom" != "cool")
     print("your mom is still cool")


# Above we expect a SyntaxError because we forgot to close the `if` statement with a `:`. Also, be careful of additional spaces in between indents. Here is correct way to write that:

# In[ ]:


#Solutions for Syntax Errors 

# Just a few tweaks (1)
if ("your mom" != "cool"): # -- It's okay to Google syntax <3
    print("your mom is still cool") # -- Python loves reading spaces so be careful! 


# In[ ]:


#Jean's Mass 
K = 1.38 * 10^-23
T = 70 #temperature in Kelvin
G = 6.674 * 10**-11 #graviational constants in m^3 kg^-1 s^-2
mu = 1
M = 1.673 * 10**-27 #mass in kg
n = 10**-7 
rho = M * n #density

Mj = ((5K * T)/(G * mu * M)) ** (3/2) * (3/(4 * np.pi* rho))**(1/2))
print(Mk)


# There is a lot going on here. First make sure that all the operators are correct such as replacing any `^` with `**` and ensuring that all values are being multiplied using `*`. Then check your parenthesis!

# In[ ]:


#Jean's Mass
K = 1.38 * 10**-23 # --- Don't use ^ for powers --
T = 70 #temperature in Kelvin
G = 6.674 * 10**-11 #graviational constants in m^3 kg^-1 s^-2
mu = 1
M = 1.673 * 10**-27 #mass in kg
n = 10**12 
rho = M * n #density

Mj = ((5 * K * T)/(G * mu * M)) ** (3/2) * (3/(4 * np.pi* rho))**(1/2) #Always use * between each variable and an extra parenthesis
#PROTIP: break apart big equations like these into different variable if you can't find what is wrong. 
print(Mj)


# **Examples of Run Time Errors:**
# These happen when the syntax of the code checks out but there is another underlying issue. 

# In[ ]:


#Can anything go at the speed of light?
time = 5 
v = 3 * 10 ** 8
c = 3 * 10 ** 8
timePrime = time / ((1 - (v/c)**2)**(1/2)) 


# EXPLANATION: Since v = c, and v/c = 1, the denominator becomes 0. 

# In[ ]:


#How about faster than the speed of light?
time = 5 
v = 3 * 10 ** 10
c = 3 * 10 ** 8
timePrime = time / sqrt((1 - (v/c)**2)) 
print(timePrime)


# EXPLANATION: Here, v > c, so it is taking the square root of a negative. 

# In[ ]:


#The need for speed!
time = 5 
c = 3 * 10 ** 8
timePrime = time / ((1 - (u/c)**2)**(1/2))


# EXPLANATION: v is not defined. 

# In[ ]:


#Opening a pandora box that doesn't exist
f = open("pandorabox.txt") 


# EXPLANATION: Make sure the file you're trying to open is in the same directory as the code you are trying to run!

# In[ ]:


#Vector vs Scalar
vectorA = np.array([1, 2, 3])
vectorB = np.array([4, 5, 6])
scalar = np.dot(vectorA, vectorB) #taking dot prouct
notScalar = np.cross(scalar, vectorB) #taking cross product


# EXPLANATION: Dot product produces a scalar quantity while cross product gives needs 2 vector so this code will not run. 

# In[ ]:


#And it goes on and on and on - for a bit too long.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
       
print(fibonacci(1000))


# EXPLANATION: Python has a limit for the number times it can call itself. For more information go here: https://www.pythonpool.com/recursionerror-maximum-recursion-depth-exceeded-while-calling-a-python-object/

# **Examples of Type Errors:** Type errors are usually found when there are odd clashes - like the character 's' being added to the int 1. 

# In[ ]:


#Call me maybe - or later - or not at all
song = ["here's", "my", "number", "so", "call", "me"]
song.append["maybe"]


# EXPLANATION: There needs to be `()` instead of `[]`!
# 
# 

# In[ ]:


#Leave "them" out of this!
theDrama = 5
addingThemToTheDrama = "them" + theDrama


# EXPLANATION: Make sure that all operators that are being operated on are of the same type. 

# 
# ## IV. Anticipating Errors

# If you have a feeling that your code may produce an error, there is a way to check and see if it will error. This method is called `try` and `except`. They are quite useful when going through lists/arrays that you don't know the contents of.\
# The syntax for this is as follows:

# In[ ]:


try:
    "code with expected error"
except "error name" as "alias":
    print('what you want to show if error does occur')


# Say you a `ZeroDivisionError` (dividing by zero) may occur in your code. You can do this to see if it does happen:

# In[ ]:


try:
    print(10/0)
except ZeroDivisionError as error:
    print("can't divide by zero!")


# They can also be implemented in functions!

# In[ ]:


def divide(dividend, divisor):
    try:
        result = dividend/divisor
    except ZeroDivisionError:
        print("divided by zero :o")
        result = 0
    return result

print(divide(1, 0))


# ## That's it!
# 
# Good job reading through this guide. We hope it will be useful for you in the future, and make you feel a bit more confident when your code starts breaking.
# 
# This resource was written by the Python DeCal Staff: James Sunseri, Megan Joseph, and Mahum Khan 

# In[ ]:




