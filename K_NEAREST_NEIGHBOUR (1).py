
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')


# In[2]:


dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new_features= [5,7]


# In[3]:


plt.xlabel('Time')
plt.xlabel('Distance')

for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1],s=100,color=i)
plt.scatter(new_features[0],new_features[1],s=100)
plt.show()
            


# In[10]:


def k_nearest_neighbours(data,predict,k=4):
    print(len(data))
    if len(data)>=k:
        warnings.warn("K is set to a value less than total voting......")
    distances=[]
    for group in data:
        for features in data[group]:
            euclidean_distance =np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
    votes= [i[1] for i in sorted(distances)[:k]]
    print(votes)
    print(Counter(votes))
    vote_result = Counter(votes).most_common(1)[0][0]
    dvotes=[]
    for q in votes:
        if q not in dvotes:
            dvotes.append(q)
    print dvotes
    totalocc=len(votes)
    print(totalocc)
    for eee in range(0,len(dvotes)):
        
        occ=votes.count(dvotes(eee))
        confidence=occ/totalocc
        print("Confidence of",dvotes(e)," is ",confidence)
    return vote_result


# In[11]:


result=k_nearest_neighbours(dataset,new_features)
print(result)

