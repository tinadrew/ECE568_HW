"""
Tina Drew - 035006375
ECE568 - Spring 2018
Homework 3
This Code complete homework 3
"""

""""
This code was modified by Tina Drew from:
Curve fitting by  Sam Ramezanli Create curvefit.py
https://github.com/samramez/Bayesian-Curve-Fitting
"""
from decimal import*
getcontext().prec = 28
from fractions import Fraction

from builtins import open
from builtins import str
# etc., as needed

import decimal, numpy
import math
import numbers
import operator
import re

import matplotlib
from numpy  import *
import numpy
import pytest
import matplotlib.pyplot as plt
#from scipy import interpolate
import pylab as pl

class glVar():
    s2 = []
    mx = []

#file = raw_input("enter the data file name in txt format (enter data.txt) \n")

# x = raw_input("enter the amount for the x (You can enter 10 as an exmple) \n")
x = 11
# M = raw_input("Please type in the highest order M (how about entering 4! ) \n")
M = 15

Mp = M + 1

N=[1,2,3,4,5,6,7,8,9,10]
#This is a counter for the Sigma seri 

alpha = 0.005
beta = 11.1


#start---------------------------------------------------------
#function to store the data in the matrix and returns Data stored in the text format file
def store(filename):
    file = open(filename)
    X = []
    for line in file.readlines():
        X.append(line)
    X = map(str.strip, X) #I use this to eliminate '\n' from my list
    return(X)
#end---------------------------------------------------------

Datas =[1222.52,1222.51,1222.29,1222.9,1222.37,1222.272,1222.356,1222.53,1222.69,1222.90]

#Datas =[12.52,12.51,12.29,12.29,12.37,12.272,12.356,12.53,12.69,12.90]

#the following function, generates the PhiX
#start---------------------------------------------------------
def getPhiX(x):
    PhiX = []  #getting PhiX
    i = 0 
    while i < Mp:
        PhiX.append(math.pow(x,i))
        i += 1
    PhiX = numpy.array(PhiX)
    #print('PhiX: ', PhiX)
    return PhiX
    
#end---------------------------------------------------------
 
# This function returns S^(-1)
#start---------------------------------------------------------
def getInvS():    
    I = numpy.ones((Mp,Mp)) #creating all one matrix as matrix I
    tmp = numpy.zeros((Mp,Mp)) # tmp = Phi(Xn).Phi(X)^T    
    n = 0
#     while n < len(N):
#         PhiX = getPhiX(N[n])
#         PhiX.shape(Mp,1)
#         PhiXT = numpy.transpose(PhiX) 
#         tmp += numpy.dot(PhiX,PhiXT) 
#         n += 1
        
    for n in range (0,len(N)):
        PhiX =getPhiX(N[n])  #Phix = PhiX[j]
        PhiX.shape=(Mp,1)
        PhiXT = numpy.transpose(PhiX) #DONE 
        tmp += numpy.dot(PhiX,PhiXT) #Multipy PhiX by it's transpose. Then add to summary. 
        
    betaPhi = beta*numpy.matrix(tmp) #multiplying a matrix by a constant number beta
    alphaI = alpha*numpy.matrix(I) #multiplying a matrix by a constant number alpha
    InverseS = alphaI + betaPhi
    print('InverseS: ', InverseS)
    return InverseS 
    # returns S^(-1)
#end---------------------------------------------------------


#This function returns mean(x)
#start---------------------------------------------------------
def getm(x):
    
    tmp = numpy.zeros( Mp)
    PhiX = getPhiX(x)
    #print('PhiX', PhiX)
    PhiX.shape= ( Mp ,1)
    InverseS = getInvS()
    S =  numpy.linalg.inv(InverseS) # getting inverse from InverseS and getting S
    PhiXT = numpy.transpose(PhiX)
    tmp1 = numpy.dot(PhiXT,S)
    mult = beta*numpy.matrix(tmp1)
    n = 0
    while n < len(N):
        phiXn = PhiX[N[n]]
        z = numpy.dot(phiXn, Datas[n])
        tmp = numpy.add(tmp,z)
        n += 1
    numpy.transpose(mult)
    #print('Datas', Datas)
    #print('Z : ', z)
    #print('Mult: ',mult)
    
    result = numpy.dot(numpy.transpose(mult),z)
    print('mx', result)
    return result

#end---------------------------------------------------------


#finding S^2
#start---------------------------------------------------------
def gets2(x):
    PhiX = getPhiX(x)
    PhiX.shape = (Mp,1)
    InverseS = getInvS()
    PhiXT = numpy.transpose(PhiX)
    S =  numpy.linalg.inv(InverseS)    
    tmp = numpy.dot(PhiXT,S)
    s2 = numpy.dot(tmp,PhiX)
    s2 += (1/beta)
    print('s2', s2)
    return s2

#end---------------------------------------------------------

#start---------------------------------------------------------
def showPlot():
    pl.plot(Datas)
    pl.show()
#end---------------------------------------------------------

'''
Modified code2 from: 
https://stackoverflow.com/questions/14873203/plotting-of-1-dimensional-gaussian-distribution-function
'''
import numpy as np

def gaussian(x, mu, sig):
    u = np.exp(-np.power(x - mu, 2.000)/ (2 * np.power(sig, 2.00)))
    v = (1/(2 * math.pi * np.power(sig, 2.)))**(1/2)
    print('x-mu',x - mu)
    print('v',v )
    print('u', u)

    return u*v
'''End of modified code2'''

def main():
    
    #we set the range of the plot
    S2 = gets2(x)
    MeanX = getm(x)
    tmp = MeanX[0]
    
    start = 1215
    stop = 1230
    
    div = float((stop - start)/len(numpy.array(tmp).flatten()))

    
    print('div', div)
    rg = numpy.arange(1215, 1230, 0.1)
    xe = range = numpy.arange(start,stop,div)

    S2 = numpy.array(S2).flatten()
    sig = Fraction(str(S2[0]))
    sig = float(sig)

    print('range', range)
    print('sig', sig)
    print ('\ntmp', tmp)
    
   

    #print(gaussian(xe, MeanX, sig))
    plt.figure(122)
    plt.title('Distribution')
    plt.plot(gaussian(xe, MeanX, sig))
    plt.figure(122).show()
    
    plt.figure(123)
    plt.title('Data')
    plt.plot(Datas)
    plt.figure(123).show()
 
 
 
main()
showPlot()