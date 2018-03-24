'''
The code is based on the a class assignment at Rutgers University. 
Assignment: Homework 5 - Nueral Networks
Class:  Software Engineering II  
Course No: ECE568
Professor: Shiyu Zhou
Semester: Spring 2018
Website code developer: Tina Drew
'''


'''Imports necesssary python libraries'''
import csv
import random
import math
import os
import numpy as np

'''Set global variables'''
class glVar():
    directory = myFile = ''
    weights = [] #array of weights
    errM = 0.0 #max error
    errE = 0.0 #current error
    netHid = []
    Y = [] #expected output
    a = [] #predicted out
    
    L_out = H1= H2 = Xin = []
    w1 = w2 = []
    
    
    X_Train = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    '''This is the expected output of the X1 OR X2'''
    Y = np.array([[0, 1, 1, 0]])
    
    
    
    #TrainingData = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]]



'''Activation function'''
def f(x):
    return 1/(1+np.exp(-x))
    
def fp(x):
    return f(x)*(1-f(x))
    
    #print(y)

'''
Gets the XOR value
def XOR(x, y):   
    z = x^y 
    #print (z) 
    return z
'''
    
'''Generates random numbers bewteen -1 and 1 for the weights'''
def getWeights(n):
    glVar.w1.append(round(random.uniform(-1, 1),2))
    glVar.w2.append(round(random.uniform(-1, 1),2))       

def getArrays():
    '''Creating and array of integars with a base of 1
    Each row corresponds to X1, X2, Base'''
    
    
    #X = np.array([0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0])

    for k in range(10):
        i = np.random.randint(glVar.X_Train.shape[0])
        
        Xb = [glVar.X_Train[i]]
        #print(Xb)
        
        glVar.H1 = fp(np.dot(Xb, glVar.w1))
        glVar.H2 = fp(np.dot(Xb, glVar.w2))
        print(glVar.H1)

getWeights(2)
getArrays()

