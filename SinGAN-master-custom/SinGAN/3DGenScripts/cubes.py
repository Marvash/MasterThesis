import torch
import numpy as np
import torch.nn as nn
import math
import os
import random
import matplotlib.pyplot as plt
import sys
import customFuncs


size = 40
toRtn = torch.full((1,1,size,size,size), 1)
for i in range(0, size):
    for j in range(0, size):
        for k in range(0, round(size/5)):
            toRtn[0][0][i][j][k] = -1
for l in range(0, 20):
    loc = (random.randrange(8,35),random.randrange(8,35),random.randrange(round(size/5),35))
    for i in range(loc[0]-4, loc[0]+4):
        for j in range(loc[1]-4, loc[1]+4):
            for k in range(loc[2]-4, loc[2]+4):
                toRtn[0][0][i][j][k] = -1
customFuncs.visualizeVolume(toRtn)
customFuncs.save3DFig(toRtn, "../../Input/Images3D/original.pt")