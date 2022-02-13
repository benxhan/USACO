lines = "5\n3\n8 10 5\n6\n4 6 4 4 6 4\n3\n0 1 0\n2\n1 2\n3\n10 9 9"
lines = [i for i in lines.split("\n")]

cases = int(lines[0])

for case_num in range(cases):
    # goes through each case 
    num = lines[case_num*2+1]
    case = lines[case_num*2+2].strip().split()
    hungriest = [0, 0] # cow number, hunger
    for cow in range(len(case)):
        if int(case[cow]) > int(hungriest[1]):
            hungriest = [cow, case[cow]]
    case.pop(hungriest[0])
    # hungriest = the cow with the highest hunger level
    # now find second highest?
    other_hungriest = [0, 0]
    for cow in range(len(case)):
        if int(case[cow]) > int(other_hungriest[1]):
            other_hungriest = [cow, case[cow]]
            
    # now we have the two hungriest cows
    while (int(hungriest[1]) != 0) or (int(other_hungriest[1]) != 0) or (int(hungriest[1]) == int(other_hungriest[1])):
        int(hungriest[1]) -= 1
        int(other_hungriest[1]) -= 1
