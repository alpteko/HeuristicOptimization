import numpy as np

def load_data():
    data = np.loadtxt('data.txt')
    data = data[:,0:2]
    return data

def init_facilities(k):
    data= load_data()
    solution =  []
    T = len(data)
    mask = np.random.randint(k,size=T)
    for i in range(k):
        ind = list(np.where(mask==i)[0])
        solution.append(list(data[ind,:]))
    return solution

def cost(solution):
    total_cost = 0
    for l in solution:
        mu = np.mean(l,axis=0)
        total_cost += np.sum((l-mu)**2)
    return total_cost

def sqrt_cost(solution):
    total_cost = 0
    for l in solution:
        mu = np.mean(l,axis=0)
        for x in l:
            total_cost += np.linalg.norm(x-mu)
    return total_cost