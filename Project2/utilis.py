import numpy as np
import time
def load_data():
    data = np.loadtxt('data.txt')
    data = data[:,0:2]
    return data

def init_facilities(k):
    mask = np.random.randint(k,size=654)
    return mask

def find_cost(mask,data,k):
    mu_array = np.zeros((654,2))
    for i in range(k):
        mu = np.mean(data[mask==i,:],axis=0)
        mu_array[mask==i,:] = mu
    return np.sum((data-mu_array)**2)

def sqrt_cost(mask,data,k):
    mu_array = np.zeros((654,2))
    for i in range(k):
        mu = np.mean(data[mask==i,:],axis=0)
        mu_array[mask==i,:] = mu
    total_cost = 0
    for i in range(654):
        total_cost += np.linalg.norm(data[i,:]-mu_array[i,:])
    return total_cost