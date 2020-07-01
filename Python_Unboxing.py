
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import random as rd
from itertools import permutations, combinations

# For 8x8 Chess Board
x = range(0, 8)

# Use Permutations to come up with all possible sequences of placing 8 queens on a 8x8 Chess Board

list1 = []
for piece in permutations(range(0, 8)):
    y = piece
    list2 = []
    for x_val, y_val in zip(x, y):
        list2.append((x_val, y_val))
    list1.append(list2)

# Function to check if any 2 points (queens in this case) are diagonal or not

def Diagonal(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    slope = (y2 - y1) / (x2 - x1)
    if slope == -1 or slope == 1:
        return(True)
    else:
        return(False)

# Create list of all possible sequences of queens

seq = []
for seq1 in list1:
    diag_list = []
    for p1, p2 in set(list(combinations(seq1, 2))):
        diag_list.append(Diagonal(p1, p2))

    if True not in diag_list:
        seq.append(seq1)

# Chose one random sequence from all possible sequences

rd.choice(seq)

