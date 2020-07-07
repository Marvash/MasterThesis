import torch
import numpy as np
import torch.nn as nn
import math
import os
import random
import matplotlib.pyplot as plt

def convert_2dto3d(toConvert):
    tmp = toConvert[0][:][:][:]
    print(tmp[0][38][32]) # 0,0 upper left corner x goes down y goes right
    #plt.imshow(tmp.permute((1, 2, 0)).cpu().numpy())
    #plt.show()
    expandedTensor = toConvert.unsqueeze_(-1).expand(toConvert.shape[0], toConvert.shape[1], toConvert.shape[2], toConvert.shape[3], toConvert.shape[2])
    print(expandedTensor[0][0][38][32][:])
    