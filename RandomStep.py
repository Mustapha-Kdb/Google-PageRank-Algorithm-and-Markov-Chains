import matplotlib.pyplot as plt
import random

def randomStep(p,k,N,M):
    position = 0
    positions = [position]  
    for _ in range(k):
        step = 1 if random.uniform(0,1) < p else -1
        position += step
        if position < -N:
            position = -N 
        elif position > M:
            position = M 
        positions.append(position) 
    
    return positions

positions = randomStep(0.5, 10, 4, 4)

plt.figure(figsize=(14, 4))
plt.plot(positions, marker='o', linestyle='-', markersize=4)
plt.title('Random Walk Simulation over {} Steps'.format(len(positions)-1))
plt.xlabel('Time step')
plt.ylabel('Position')
plt.grid(True)
plt.show()

def evolTime(positions):
    k= len(positions)
    reps = {}
    for i in range (k):
        if positions[i] in reps:
            reps[positions[i]]+=1 
        else:  
            reps[positions[i]]=1

    for i in (reps):
        reps[i]=reps[i]/k

    return reps      

Nbreps = evolTime(positions)
print(Nbreps)
print(sum(Nbreps.values()))
plt.figure(figsize=(10, 6))
plt.bar(Nbreps.keys(), Nbreps.values())
plt.title('Proportion of Time Spent in Each State')
plt.xlabel('State')
plt.ylabel('Proportion of Time Spent')
plt.grid(True)
plt.show()

