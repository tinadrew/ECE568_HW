import numpy
import math
import csv


'''
Code by: govind94/Bayesian-Curve-Fitting
https://github.com/govind94/Bayesian-Curve-Fitting
'''
def bayesian(data):
    x_10 = []
    t_data = []
    for i in xrange(len(data) - 10, len  div(data)):
        t_data.append(data[i])
    for i in xrange(1, 11):
        x_10.append(i)
    t = []
    t.append(t_data)
    t_data = t
    N = 10
    M = 6
    rel_err_dr = 0
    x = x_10[len(x_10) - 1] + 1
    for k in range(1):
        t = numpy.zeros((N, 1), float)
        phi = numpy.zeros((M, 1), float)
        phi_sum = numpy.zeros((M, 1), float)
        phi_sum_t = numpy.zeros((M, 1), float)
        for i in range(M):
            phi[i][0] = math.pow(x,i)
        for i in range(N):
            t[i][0] = t_data[k][i]
        for j in range(N):
            for i in range(M):
                phi_sum[i][0] = phi_sum[i][0] + math.pow(x_10[j],i)
                phi_sum_t[i][0] = phi_sum_t[i][0] + t[j][0] * math.pow(x_10[j],i)

        ''' Calculation of variance / standard deviation '''
        S = numpy.linalg.inv(0.005 * numpy.identity(M) + 11.1 * numpy.dot(phi_sum, phi.T))
        var = numpy.dot((phi.T), numpy.dot(S,phi))
        var = var + 1 / 11.1
        ''' Calculating the mean '''
        mean = 11.1 * numpy.dot(phi.T, numpy.dot(S,phi_sum_t))
        mean = mean[0][0]
        print ('mean', mean)
    t = t_data[0]
    t_data = t
    sum = 0
    avg = 0
    print ('t_data', t_data)
    for i in t_data:
        sum = sum + i
    mov = sum / len(t_data)
    print ('mov', mov)
    per = ((mean - mov) / mov) * 100
    print ('per', per)
    final = []
    mean = round(mean, 3)
    per = round(per, 3)
    final.append(mean)
    final.append(per)
    return final

f = open('AMZN_history.csv', 'rb')
csv_f = csv.reader(f)
data = []
data1 = []
def readLines():
    with open('AMZN_history-.csv', 'rU') as info:
        reader = csv.reader(info)
        row = list(reader)
        for x in row:
            data.append([float(str(y)) for y in x])
            print(data)
readLines()


"""
for row in csv_f:
    rows = float(row[5])
    data.append(rows)
print (data)
f.close()
"""
prediction = bayesian(data)
print (prediction)
