lines = "4 0\n 1 100 2 3"
lines = [int(i) for i in lines.strip().split(" ")]

n = lines[0] # number of papers
L = lines[1] # citations

true_h_index = 0
for x in range(n):
    h_index = x+1
    citations = 0
    for y in range(n):
        if lines[y+2] >= h_index:
            citations += 1
            if L != 0:
                L -= 1
                lines[y+4] += 1
    if (citations >= h_index):
        true_h_index = h_index

print(true_h_index)
