finput = open("C:\\Users\\ben\\Desktop\\usaco\\fence_input.txt", "r")

lines = finput.readlines()
print(lines)
(a, b) = lines[0].strip().split(" ")
(c, d) = lines[1].strip().split(" ")

ans = []
for i in range(int(a), int(b)):

    ans.append(i)
    
for i in range(int(c), int(d)):

    if i not in ans:
        ans.append(i)

answer = len(ans)
print(answer)

with open('C:\\Users\\ben\\Desktop\\usaco\\paint.out', 'w') as out:
    print(answer, file=out)
