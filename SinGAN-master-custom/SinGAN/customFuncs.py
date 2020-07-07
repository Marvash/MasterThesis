import torch
import numpy as np
import torch.nn as nn
import math
import os
import random
import matplotlib.pyplot as plt

def get3D(toConvert):
    #print(toConvert[0][0][38][32]) # 0,0 upper left corner x goes down y goes right
    expandedTensor = toConvert.unsqueeze(-1).expand(toConvert.shape[0], toConvert.shape[1], toConvert.shape[2], toConvert.shape[3], toConvert.shape[2])
    tmp = toConvert[0][:][:][:]
    #plt.imshow(tmp.permute((1, 2, 0)).cpu().numpy())
    #plt.show()
    expandedTensor = torch.zeros(toConvert.shape[0], 1, toConvert.shape[2], toConvert.shape[3], toConvert.shape[3])
    print(expandedTensor.shape)
    for i in range(0, toConvert.shape[2]):
        for j in range(0, toConvert.shape[3]):
            expandedTensor[0][0][i][j][(math.floor(toConvert.shape[3]/2)-1)] = 1 - norm01(toConvert[0][0][i][j])
    #print(expandedTensor[0][0][37][32][31])
    #print(expandedTensor[0][0][38][32][30])
    #print(expandedTensor[0][0][39][32][31])
    #plt.imshow(tmp.permute((1, 2, 0)).cpu().numpy())
    #plt.show()
    tmp = expandedTensor[0][0][:][:][:]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(tmp, edgecolor='k')

    plt.show()
    return expandedTensor
    
def get3DPyramid(reals):
    reals3D = []
    for real in reals:
        reals3D.append(get3D(real))
    return reals3D
    
def norm01(num):
    return (num+1)/(2)