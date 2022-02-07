finput = open("C:\\Users\\ben\\Desktop\\usaco\\buckets.txt", "r")

lines = finput.readlines()

for x in range(10):
    lines[x] = lines[x].strip()
    
barn = []
rock = []
lake = []
for x in range(10):
    for n in range(10):
        if lines[x][n] == "B":
            barn = [x, n]
        elif lines[x][n] == "R":
            rock = [x, n]
        elif lines[x][n] == "L":
            lake = [x, n]
            
cows = abs(barn[0] - lake[0]) + abs(barn[1] - lake[1]) -1

if (barn[0]==rock[0] and rock[0] == lake[0]):
    cows += 2
    
if (barn[1]==rock[1] and rock[1] == lake[1]):
    cows += 2
    
print(cows)
with open('C:\\Users\\ben\\Desktop\\usaco\\buckets.out', 'w') as out:
    print(cows, file=out)
