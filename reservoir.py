
import random
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd 
class Reservoir:
    def __init__(self, k):  # k = 배열의 크기 
        self.k = k
        self.sampled = []
        self.size =0
    
    def add(self, x):
        self.size += 1

        if self.size <= self.k:
            self.sampled.append(x)
        else:
            i = random.randrange(0,self.size)
            if i < self.k:
                self.sampled[i] = x
            else:
                pass


sampled_data = []
r = Reservoir(100)
for games in range(10000):
    for i in range(1000):  # range 내 숫자는 입력되는 스트림의 크기 
        r.add(i)
        sampled_data.append(r.sampled)

integrated_sample_data = np.array(sampled_data).flatten().tolist()
count_each_data = Counter(integrated_sample_data)
k_data = pd.Series(count_each_data)
k_index = dict(sorted(k_data.items()))
plt.bar(range(len(k_index)),list(k_index.values()),align='center')
plt.xticks(range(len(k_index)), list(k_index.keys()))
plt.show()




