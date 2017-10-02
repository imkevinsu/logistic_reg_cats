import numpy as np
# import matplotlib.pyplot as plt
# import h5py
# import scipy
# from PIL import Image
# from scipy import ndimage
# from lr_utils import load_dataset

#matplotlib inline

def sigmoid(z):
    s = 1/(1+np.exp(-z))
    return s

print("sigmoid: " + str(sigmoid(np.array([0,2]))))