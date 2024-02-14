import numpy as np
import matplotlib.pyplot as plt

def transition_matrix(p, N, M):
    size = N + M + 1 
    P = np.zeros((size, size))
    
    for i in range(size):
        if i == 0:  
            P[i, i] = 1 - p
            P[i, i + 1] = p
        elif i == size - 1:  
            P[i, i] = p
            P[i, i - 1] = 1 - p
        else:  
            P[i, i - 1] = 1 - p
            P[i, i + 1] = p
    return P

def power_method(P, epsilon=1e-6):
    size = P.shape[0]
    x = np.array([1] + [0] * (size - 1))
    x_before = np.zeros(size)
    evolution = [x]  
    k = 0

    while np.linalg.norm(x - x_before) > epsilon:
        x_before = x
        x = np.dot(x, P)
        evolution.append(x)
        k += 1

    x_avg = np.mean(evolution, axis=0)
    return np.array(evolution), x_avg, k

P = transition_matrix(0.5, 5, 5)
evolution, average_distribution, iterations = power_method(P)

plt.figure(figsize=(14, 6))
for state in range(P.shape[0]):
    plt.plot([x[state] for x in evolution], label=f'State {state - ((P.shape[0] // 2)-1)}')

plt.title('Temporal Evolution of x(k) for Each State (Provided Code)')
plt.xlabel('Iteration k')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()

average_distribution, iterations

print(P)
print("Average Distribution:",average_distribution)
print("Nb of iterations",iterations)
