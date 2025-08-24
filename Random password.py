#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string
Dif = input("How difficult you want your password to be? ")
NHa = random.randint(8,10)
NMe = random.randint(4,7)
NEa = random.randint(2,3)
pasH = []
pasM = []
pasE = []
if Dif == "hard":
    for i in range(NHa//2):
        randomLetter = random.choice(string.ascii_letters)
        randomNumber = random.randint(0,9)
        pasH.append(randomLetter)
        pasH.append(randomNumber)
    random.shuffle(pasH)
    print("".join(map(str, pasH)))
if Dif == "medium":
    for i in range(NMe//2):
        randomLetter = random.choice(string.ascii_letters)
        randomNumber = random.randint(0,9)
        pasM.append(randomLetter)
        pasM.append(randomNumber)
    random.shuffle(pasM)   
    print("".join(map(str, pasM)))
if Dif == "easy":
    for i in range(NEa//2):
        randomLetter = random.choice(string.ascii_letters)
        randomNumber = random.randint(0,9)
        pasE.append(randomLetter)
        pasE.append(randomNumber)
    random.shuffle(pasE)
    print("".join(map(str, pasE)))

