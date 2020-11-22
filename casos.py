import numpy as np

melhor = np.arange(1, 50000)

pior = np.arange(1, 50000)[::-1]

medio = np.arange(1, 50000)
np.random.shuffle(medio[len(medio)//2:])

file_melhor = open("melhor.txt", "w")
file_pior = open("pior.txt", "w")
file_medio = open("medio.txt", "w")

for i in melhor:
    file_melhor.write(f"{i}\t")

for i in pior:
    file_pior.write(f"{i}\t")

for i in medio:
    file_medio.write(f"{i}\t")

file_melhor.close()
file_pior.close()
file_medio.close()