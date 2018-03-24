'''
The code is based on the a class assignment at Rutgers University. 
Assignment: Homework 5 - Nueral Networks
Class:  Software Engineering II  
Course No: ECE568
Professor: Shiyu Zhou
Semester: Spring 2018
Modified by: Tina Drew
'''

'''
This code was copied and modified from: 
http://www.bogotobogo.com/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php
I modified as necessary to meet class requirements
'''
import numpy as np

class glVar():
    Err = []
    E_first = E_first_avg = E_final = E_final_avg = []
    W_Init = W_final = []
    Learn_rate = 0.2
    E_target = 0.1
    E_avg = 100.1
    Batch_sz = 4
    Batch_run  = 0

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

class NeuralNetwork:

    def __init__(self, layers, activation='tanh'):
        '''Select the appropriate activation function'''
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_prime
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_prime

        '''Creates array of weights for nodes  in the hidden network'''
        # Set weights
        self.weights = []
        # layers = [2,2,1]
        # range of weight values (-1,1)
        # input and hidden layers - random((2+1, 2+1)) : 3 x 3
        
        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)
        # output layer - random((2+1, 1)) : 3 x 1
        r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
        self.weights.append(r)
        glVar.W_Init = self.weights
        
    def fit(self, X, y, learning_rate, epochs=100000):
        # Add column of ones to X
        # This is to add the bias unit to the input layer
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
         
        for k in range(epochs):
            '''Randomly selects rows of X(training data and appends it to a test array (a))'''
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                '''Performs dot matrix multiplication of the weight and inputs(a)'''
                dot_value = np.dot(a[l], self.weights[l])
                '''complete activation for this row of a'''
                activation = self.activation(dot_value)
                '''appends estiamted result to a'''
                a.append(activation)
            # output layer
            error = y[i] - a[-1]
            relErr = abs(y[i] - a[-1])
            deltas = [error * self.activation_prime(a[-1])]
                        
            glVar.Err.append(relErr)
            temp = glVar.Err[k-10:]
            glVar.E_avg = sum(temp)/(len(temp))
            #print(glVar.E_avg)
            '''If the relative error reachs get below the target the code below is executed 
            and the loop stops'''
            if abs(glVar.E_avg) <= glVar.E_target:
                glVar.E_first = glVar.Err[:3]
                glVar.E_first_avg = sum(glVar.E_first)/len(glVar.E_first)
                glVar.E_final = glVar.Err[k-3:]
                glVar.E_final_avg = sum(glVar.E_final)/len(glVar.E_final)
                glVar.Batch_run = int(k/glVar.Batch_sz) + 1
                glVar.W_final = self.weights
                break
            
            # we need to begin at the second to last layer 
            # (a layer before the output layer)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()

            # backpropagation
            # 1. Multiply its output delta and input activation 
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight.
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            #if k % 10000 == 0: print 'epochs:', k

    def predict(self, x): 
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)      
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a

def printOutput():
    '''Prints summary of parameters'''
    print('\n-----------------------------------')
    print('Learning Rate: ', glVar.Learn_rate)
    print('Target Error Rate: ', glVar.E_target)
    print('Batch Size: ',glVar.E_first)
    print('Number of batches run: ', glVar.Batch_run)
    
    '''Prints final data  summary'''
    print('\n-----------------------------------')
    print('Initial Weights: ', glVar.W_Init)
    print('Initial Errors: ',glVar.E_first)
    print('Initial Error Average: ', glVar.E_first_avg)

    print('\n-----------------------------------')
    print('Final Weights: ', glVar.W_final)
    print('Final Errors: ',glVar.E_final)
    print('Final Error Average: ', glVar.E_final_avg)
    
    '''Prints final predicted value'''
    print('\n-----------------------------------')
    print('[X1, X2] [Predicted Value]')


def main():

    glVar.Learn_rate = float(input('Please enter the learning rate: '))
    glVar.E_target = float(input('Please enter the targe error: '))
    
    nn = NeuralNetwork([2,2,1])
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 1, 1, 0])
    nn.fit(X, y, glVar.Learn_rate)

    printOutput()
    
    for e in X:
        print(e,nn.predict(e))

main()   
input()