import numpy as np

dataTrain = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
b = [1, 3, 4, 4, 3, 2, 10]

a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
print(a[0][2])

print(b[-1])


def getArrays(epochs):
    Y = [] #expected output
    a = [] #predicted out
    
    Xin = []
    
    '''Creating and array of integars with a base of 1
    Each row corresponds to X1, X2, Base'''
    Xb = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    
    '''This is the expected output of the X1 OR X2'''
    Y = np.array([[0, 1, 1, 0]])
    
    
    #X = np.array([0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0])

    for k in range(epochs):
        i = np.random.randint(X.shape[0])
        #print('i: ', i)
        print([X[i]])
    

def getWeights(n):
    glVar.w1.append(round(random.uniform(-1, 1),2))
    glVar.w2.append(round(random.uniform(-1, 1),2))       


  

getArrays(10)

