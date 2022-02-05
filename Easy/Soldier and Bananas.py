finput = open("C:\\Users\\ben\\Desktop\\usaco\\solider.txt", "r")

lines = finput.readlines()
(cost, money, bananas) = lines[0].strip().split(" ")

banana_cost = 0
loan = 0
for x in range(int(bananas)):
    banana_cost += (x+1)*int(cost)

if banana_cost > int(money):
    loan = banana_cost - int(money)
    
with open('C:\\Users\\ben\\Desktop\\usaco\\soldier.out', 'w') as out:
    print(total_distance, file=out)
