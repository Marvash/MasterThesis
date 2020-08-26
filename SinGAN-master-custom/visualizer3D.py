import torch
import numpy as np
import torch.nn as nn
import math
import os
import random
import matplotlib.pyplot as plt
import SinGAN.customFuncs as customFuncs
from argparse import ArgumentParser
from os import listdir
from os.path import isfile, join


parser = ArgumentParser()
parser.add_argument('--input_name', help='input fig', default='')
opt = parser.parse_args()
pathName = "piskelSmaller"
completeName = 'Output/RandomSamples/'+pathName+'/gen_start_scale=0/'
if opt.input_name == '':
    onlyfiles = [f for f in listdir(completeName) if isfile(join(completeName, f))]
    for file in onlyfiles:
        tensor = torch.load(completeName+file)
        customFuncs.visualizeVolume(tensor)
else:
    tensor = torch.load(completeName+opt.input_name)
    customFuncs.visualizeVolume(tensor)