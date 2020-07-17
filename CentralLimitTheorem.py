# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:32:22 2020

@author: Eray
"""
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats
import math
import random
def calculate_mean(numbers):
    sumof = 0 
    for i in numbers:
        sumof += i
    return sumof/len(numbers)


def calculate_standart_deviation(numbers):
    mean = calculate_mean(numbers)
    sum_of_subtracktions = 0 
    for i in numbers:
        subtracked = i-mean
        sum_of_subtracktions += (subtracked**2)
    return math.sqrt(sum_of_subtracktions/(len(numbers)))
    
def make_two_dimentional_semi_circle(radius,sample_size):
    X = standart_uniform_dist(1,3,sample_size)
    Z = []
    Y = []
    for i in range(len(X)):
        y = math.sqrt(radius**2-abs(2-X[i])**2)
        Y.append(int(y*100))
    for i in range(len(X)):
        for i in range(len(Y)):
            Z.append(X[i])
    return Z
                
    
    
    

def standart_uniform_dist(lower,higher,sample_size):
    N=[]
    for i in range(sample_size):
        N.append(random.uniform(lower,higher))
    return N

def standart_uniform_dist_2(sample_size):
    N=[]
    a = random.uniform(0.5,1.30)
    b = a
    N.append(a)
    for i in range(sample_size-1):
        if b < 40:
            a = random.uniform(0.5,1.30)
            b+=a
            
        else: 
            a = random.uniform(-0.5,0.5)
            b+=a
        N.append(a)
            
    return N

def make_sum(numbers,how_many_numbers):
    C = []
    for i in range(len(numbers)):
        b = 0
        for j in range(how_many_numbers):
            a = random.randint(0,len(numbers)-1)
            b+= numbers[a]
        C.append(b)
    return C
            
        
def make_sum_for_later(uniform_1,uniform_2,how_many_numbers):
    C = []
    d = 0

    for i in range(len(uniform_1)):
        b = 0
        d = b
        for j in range(how_many_numbers):
            
            
            if d < 40:
                a = random.randint(0,len(uniform_1)-1)
                b+= uniform_1[a]
                
            else:
                a = random.randint(0,len(uniform_2)-1)
                b+= uniform_2[a]
        
                
        C.append(b)
    return C
            




def experiment_first_part(trial_time,sample_size):
    plt.figure()
    U = standart_uniform_dist(0,1,trial_time)   
    X = make_sum(U,sample_size)
    print("Sample mean is",calculate_mean(X))
    print("Sample standard deviation is",calculate_standart_deviation(X))

    plt.title('Histogram for generated random variables')
    plt.hist(U,100, density=True)
    plt.figure()
    
    
    plt.title('Histogram for sums of generated random variables')
    fit = stats.norm.pdf(X, calculate_mean(X), calculate_standart_deviation(X)) 
    
    plt.plot(X,fit,alpha=0.5, color='coral')
    plt.hist(X,100,alpha=0.5, density=True)
    
    plt.show()
    
def experiment_second_part(trial_time,sample_size):
    plt.figure()
    uniform_1 = standart_uniform_dist(0.5,1.5,trial_time) 
    uniform_2 = standart_uniform_dist(-0.5,0.5,trial_time) 
    uniform_3 = uniform_1.copy()
    for i in uniform_2:
        uniform_3.append(i)
    plt.title('Histogram for generated random variables')
    plt.hist(uniform_3,100, density=True)
    
    C = make_sum_for_later(uniform_1,uniform_2,sample_size)
    print("Sample mean is",calculate_mean(C))
    print("Sample standard deviation is",calculate_standart_deviation(C))
    plt.figure()
    plt.title('Histogram for sums of generated random variables')
    fit = stats.norm.pdf(C, calculate_mean(C), calculate_standart_deviation(C)) 
    
    plt.plot(C,fit,alpha=0.5, color='coral')
    plt.hist(C,100,alpha=0.5, density=True)    
    
def experiment_third_part(trial_time,sample_size):
    plt.figure()
    size = trial_time
    R = 1
    phi = np.random.random(size=size) * np.pi
    r = np.sqrt(np.random.random(size=size)) * R
    
    # transform
    x = r * np.cos(phi) + 2
    y = r * np.sin(phi)
    plt.title('Histogram for generated random variables')
    plt.bar(x,y,align='center') # A bar chart
    
    plt.show()
    Z = []
    
    Y = []
    
    for i in range(len(y)):
        Y.append((int(10*y[i])))
        
        
    for i in range(len(x)):
        for j in range(Y[i]):
            
            Z.append(x[i])
        
    M = make_sum(Z,sample_size)
    
    print("Sample mean is",calculate_mean(M))
    print("Sample standard deviation is",calculate_standart_deviation(M))
    plt.figure()
    plt.title('Histogram for sums of generated random variables')
    fit = stats.norm.pdf(M, calculate_mean(M), calculate_standart_deviation(M)) 
    
    plt.plot(M,fit,alpha=0.5, color='coral')
    plt.hist(M,100,alpha=0.5, density=True)  

    
    

print("Experiment 1:")
experiment_first_part(100000,2)
print("Experiment 2:")
experiment_first_part(100000,10)
print("Experiment 3:")
experiment_first_part(100000,50)
print("Experiment 4:")
experiment_second_part(100000,100)
print("Experiment 5:")
experiment_third_part(10000,2)
print("Experiment 6:")
experiment_third_part(10000,10)
print("Experiment 7:")
experiment_third_part(10000,50)




















