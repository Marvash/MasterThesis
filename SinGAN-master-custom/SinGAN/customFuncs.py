import torch
import numpy as np
import torch.nn as nn
import math
import os
import random
import matplotlib.pyplot as plt
from SinGAN.imresize import imresize3D

def get3D(toConvert):
    #print(toConvert[0][0][38][32]) # 0,0 upper left corner x goes down y goes right
    expandedTensor = toConvert.unsqueeze(-1).expand(toConvert.shape[0], toConvert.shape[1], toConvert.shape[2], toConvert.shape[3], toConvert.shape[2])
    tmp = toConvert[0][:][:][:]
    #plt.imshow(tmp.permute((1, 2, 0)).cpu().numpy())
    #plt.show()
    expandedTensor = torch.zeros(toConvert.shape[0], 1, toConvert.shape[2], toConvert.shape[3], toConvert.shape[3])
    #print(expandedTensor.shape)
    for i in range(0, toConvert.shape[2]):
        for j in range(0, toConvert.shape[3]):
            Zcoord = (math.floor(toConvert.shape[3]/2)-1)
            expandedTensor[0][0][i][j][Zcoord] = toConvert[0][0][i][j]#(1 - norm01(toConvert[0][0][i][j])) > 0.5
            expandedTensor[0][0][i][j][Zcoord+1] = expandedTensor[0][0][i][j][Zcoord]
            expandedTensor[0][0][i][j][Zcoord+2] = expandedTensor[0][0][i][j][Zcoord]
            expandedTensor[0][0][i][j][Zcoord-1] = expandedTensor[0][0][i][j][Zcoord]
            expandedTensor[0][0][i][j][Zcoord-2] = expandedTensor[0][0][i][j][Zcoord]
    #print(expandedTensor[0][0][37][32][31])
    #print(expandedTensor[0][0][38][32][30])
    #print(expandedTensor[0][0][39][32][31])
    #plt.imshow(tmp.permute((1, 2, 0)).cpu().numpy())
    #plt.show()
    tmp = expandedTensor[0][0][:][:][:]
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    #ax.voxels(tmp, edgecolor='k')

    plt.show()
    return expandedTensor
    
def get3DPyramid(real,reals,opt):
    real = real[:,0:1,:,:]
    print(opt.stop_scale)
    for i in range(0,opt.stop_scale+1,1):
        scale = math.pow(opt.scale_factor,opt.stop_scale-i)
        print(opt.stop_scale-i)
        print(scale)
        print(real.shape)
        curr_real = imresize3D(real,scale,opt)
        print(curr_real.shape)
        #tmp = curr_real[0][0][:][:][:]
        #fig = plt.figure()
        #ax = fig.gca(projection='3d')
        #ax.voxels(tmp, edgecolor='k')
        #plt.show()
        reals.append(curr_real)
    return reals
    
def norm01(num):
    return (num+1)/(2)