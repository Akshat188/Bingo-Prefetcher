import os
import pandas as pd
dirPath = "ChampSim/results_10M"
name = []
l1_d = []
ipc = []
l1d_hits = []
l1d_access = []
l1d_accuracy = []
prefetch_access = []
prefetch_accuracy = []
prefetch_hits = []

for fname in os.listdir(dirPath):
    with open("{}/{}".format(dirPath, fname)) as f:
        L = f.readlines()
    l1 = L[23].strip()
    l2 = L[24].strip()
    i1 = 24
    while "CPU" not in l1:
        i1 += 1
        l1 = L[i1-1].strip()
        l2 = L[i1].strip()
    l3 = L[i1+3].strip()
    
    # print(l2.split())
    l1_d.append(fname.split("-")[4])

    print(l1.split())
    name.append(fname.split(".")[1])
    ipc.append(float(l1.split()[4]))
    l1d_hits.append(int(l2.split()[5]))
    l1d_access.append(int(l2.split()[3]))
    l1d_accuracy.append(l1d_hits[-1] / l1d_access[-1])
    prefetch_hits.append(int(l3.split()[5]))
    prefetch_access.append(int(l3.split()[3]))
    try:
        prefetch_accuracy.append(prefetch_hits[-1] / prefetch_access[-1])
    except:
        prefetch_accuracy.append(0)
    
    

df = pd.DataFrame(zip(name, l1_d, ipc, l1d_hits, l1d_access, l1d_accuracy, prefetch_access, prefetch_accuracy, prefetch_hits), columns=["Name", 'L1D', 'IPC', 'L1D Hits', 'L1D Access', 'L1D Accuracy', 'Prefetch Access', 'Prefetch Accuracy', 'Prefetch Hits'])
df.to_csv("results.csv")


    
    

# L = os.listdir("ChampSim/results_10M")

# with open("ChampSim/results_10M/{}".format(L[0])) as f:
#     X = f.readlines()

# for x in os.list

# l1 = X[17].strip()
# ipc = l1.split()[9]



