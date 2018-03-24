'''
The code is based on the a class assignment at Rutgers University. 
Assignment: Homework 5 - Nueral Networks
Class:  Software Engineering II  
Course No: ECE568
Professor: Shiyu Zhou
Semester: Spring 2018
Website code developer: Tina Drew
'''

'''
Code from: 
http://www.bogotobogo.com/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php
'''
import numpy as np

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x) 

def tanh_prime(x):
    return 1.0 - x**2

class glVar():
    E_target = 0.0
    mu = 0.0
    W_ini = []

class NeuralNetwork:
    
    def __init__(self, layers, activation='tanh'):
        '''Select the appropriate sigmoid function'''
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
        glVar.W_ini = self.weights
        
        print('--------------------------------------------\n')
        print('Initial Weights: ', self.weights)

    def fit(self, X, y, learning_rate, epochs=20):
        # Add column of ones to X
        # This is to add the bias unit to the input layer
        #print('Orginal X', X)
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
        #print('Biased X', X)
        E = E_first = E_final = []
        E_Avg = 100.0
        eps  = 0.1
        k = 0
        '''Randomly selects rows of X(training data and appends it to a test array (a))'''
        
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            #print('i: ', i)
            a = [X[i]]
            #print('a:', a)
            E = []
            k += 1
        
            for l in range(len(self.weights)):
                '''Performs dot matrix multiplication of the weight and inputs(a)'''
                dot_value = np.dot(a[l], self.weights[l])
                '''complete activation for this row of a'''
                activation = self.activation(dot_value)
                '''appends estiamted result to a'''
                a.append(activation)
            # output layer
            error = y[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]
            
            E.append(error)
            print(E)
            
            E_Avg = np.mean(E, axis = 1)
            
            if k > 3:
                E_first.append(error)
                print('Initial Avg Error', np.mean(E, axis = 1))

            # we need to begin at the second to last layer 
            # (a layer before the output layer)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()
            #print(deltas)

            # backpropagation
            # 1. Multiply its output delta and input activation 
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight.
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
                #print(self.weights)
            '''    
            if k % 10000 == 0: 
                print ('epochs:', k)
            '''
             
            print('Initial Error: ', E_first)
            print ('\n--------------------------------------------- ')
            print ('Final Weights: ', self.weights)
            print('Final Error: ', E)
            print ('Number of batches: ', k+1 )
            print ('--------------------------------------------- \n')
            
     
        
            
               
    def predict(self, x): 
        #print(x)
        #print(np.array(x))
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)       
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a
        
if __name__ == '__main__':

    nn = NeuralNetwork([2,2,1])
    
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([0, 1, 1, 0])
    
    nn.fit(X, y, 0.2)
    
    for e in X:
        print(e,nn.predict(e))
    
    
    
    
    