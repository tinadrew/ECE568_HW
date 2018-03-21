'''
Tina Drew - 035006375
ECE568 - Spring 2018
Homework 3
This Code complete homework 3

This code is based on example for site below:  
https://stackoverflow.com/questions/14873203/plotting-of-1-dimensional-gaussian-distribution-function
'''
import csv
import random
import math
import os
import numpy as np

'''Initializes global variables'''
class glVar():
    #arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    dataFiles = ''
    currFile = ''
    myFile = ''
    dataFile = ''
    directory = myFile = ''
    
    dataArr = Xm =  []
    dataSum = []
    dataSorted = []
    
    beta  = 11.1
    alpha = 0.005
    
    MeanX = 0.0
    Mp = 15
    
    Pred = Px = sig2 = sig = 0.0

    N = 0
    
'''Allows the user to choose a data file or series of data files to be tested''' 
def getFilePath():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    glVar.dataFiles = filedialog.askopenfilenames(parent=root,title='Select files to be tested')
    glVar.directory = os.path.dirname(glVar.dataFiles[0])
    glVar.dataFile = glVar.dataFiles[0]

'''Retrieves the training data for the file'''
def getData(myFile):
    '''
    lines = csv.reader(open(myFile, "rt"))
    dataset = list(lines)
    for i in range(len(dataset)):
       glVar.dataArr = dataset[i] = [float(x) for x in dataset[i]]
    '''
    
    with open(myFile) as fi:
        glVar.dataArr = []
        data1 = fi.read().splitlines()
        glVar.dataArr = [float(x) for x in data1]
        #print(data1)
    glVar.N = len(glVar.dataArr)
    return glVar.dataArr
    
    
    
'''Calculates the mean of the training data'''
def getMeanX(arr):
    Xm = []
    #Gets subset of data
    '''This was added to control the number of data sammples that are test'''
    if len(arr) >= 11:
        glVar.Xm = arr[len(arr)-11:]
    else:
        glVar.Xm = glVar.dataArr
   
    glVar.MeanX = sum(glVar.Xm)/len(glVar.Xm)
    #print('Data tested', glVar.Xm)
    #print('Original Length', len(glVar.dataArr))
    #print('New Length', len(glVar.Xm))

'''
Code snippet from https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/ 
Used to calulate variance
'''
def getSig(arr):
    glVar.sig2 = sum([pow(x-glVar.MeanX,2) for x in arr])/len(arr)
        
    #print("sig2:", glVar.sig)
    glVar.sig = math.sqrt(glVar.sig2)


'''Get Gaussian distribution'''
def getGausDist(x, mu, sig2): 
    dist = []
    for i in range(0, len(x)-1):
        dist.append(np.exp(-np.power(x[i] - mu, 2.000)/ (2 * np.power(sig2, 2.00)))/(1/(2 * math.pi * np.power(sig2, 2.)))**(1/2)) 
    Prob = max(dist)*100
    ind = dist.index(max(dist))
    glVar.Pred = x[ind]    
    #print(dist)
    #print(x)
    return dist, Prob

'''Get a range of values to test the probabilit against'''
def getTestXa(arr, Mp):
    Xa = []
    div = float(max(arr) - min(arr))/Mp
    Xa.append(min(arr))
    for i in range(1, Mp):
        Xa.append(Xa[i-1]+div)
    Xa.append(max(arr))
    #print(div)
    print('Range: ', Xa)
    return Xa  

'''Gets the predicted values based on input values'''
def getPred(arr):
        
    Xa = getTestXa(arr[:len(arr)-2], glVar.Mp)
    getGausDist(Xa, glVar.MeanX, glVar.sig2)
    actual = glVar.Xm[-1] 
    absErr = abs(glVar.Pred - actual)  
    relErr = abs((absErr/actual)*100)
        
    print('Predection: ', glVar.Pred)
    print('Actual Value: ', actual)
    print('Absolute Error: ', absErr)
    print('Relative Error: ', relErr,'%')

'''Main function.'''   
def main():
    
    getFilePath()
    
    for f in glVar.dataFiles:
        glVar.dataSum = []
        myFile = os.path.basename(f)
        print('Data File:', myFile)
        getData(f)
        print('data', glVar.dataArr)
       
       
       
        getMeanX(glVar.dataArr)
        print('mean: ', glVar.MeanX)
        getSig(glVar.Xm) 
        print('variance: ', glVar.sig2)
        getPred(glVar.Xm)
        print('---------------------------------------------------------------------------------------------------------------------\n')
        
main()


    
    