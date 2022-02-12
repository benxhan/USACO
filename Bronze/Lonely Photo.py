lines = "5\nGHGHG"
lines = lines.split("\n")
cows = lines[1]

def count_lonely_animals(cow_seq):
    g = 0
    h = 0
    for x in cow_seq:
        if x == "G":
            g += 1
        else:
            h +=1
    if g == 1 or h == 1:
        return 1
    return 0
lonely_animals = 0
print(cows)
for pos in range(len(cows)-2):
    cw = cows[pos:] # removes first letter
    print("-", cw)
    for l in range(3, len(cw)+1):
        cw_to_test = cw[0:l]
        print("--", cw_to_test)
        lonely_animals += count_lonely_animals(cw_to_test)
    print(lonely_animals)
count_lonely_animals(cows)

