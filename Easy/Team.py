finput = open("C:\\Users\\ben\\Desktop\\usaco\\team.txt", "r")

lines = finput.readlines()
print(lines)
(problem_nums) = lines[0].strip().split(" ")


problems_submitted = 0
print(problem_nums)
for x in range(int(problem_nums[0])):
    problem = lines[int(x)].strip().split(" ")
    correct = 0
    for n in problem:
        if (n == "1"):
            correct += 1
    if correct > 1:
        problems_submitted += 1
    
    
with open('C:\\Users\\ben\\Desktop\\usaco\\team.out', 'w') as out:
    print(problems_submitted, file=out)

print(problems_submitted)
