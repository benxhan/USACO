finput = open("C:\\Users\\ben\\Desktop\\usaco\\promote.txt", "r")

lines = finput.readlines()
print(lines)

(bb, ba) = lines[0].strip().split(" ") # bronze before, bronze after
(sb, sa) = lines[1].strip().split(" ") # silver before, silver after
(gb, ga) = lines[2].strip().split(" ") # gold before, gold after
(pb, pa) = lines[3].strip().split(" ") # plat before, plat after

bs = 0 #bronze to silver promo
sg = 0 #silver to gold promo
gp = 0 #gold to plat promo
participants_before = int(bb) + int(sb) + int(gb) + int(pb)
participants_after = int(ba) + int(sa) + int(ga) + int(pa)
new_participants = participants_after - participants_before

gp = int(pa) - int(pb)

sg = int(ga) - int(gb) + int(gp)

bs = int(sa) - int(sb) + sg

print (gp, sg, bs)

# let's be smarter by using f-string in Python
line = f"{gp}\n{sg}\n{bs}"
print(line)

with open('C:\\Users\\ben\\Desktop\\usaco\\promote.out', 'w') as out:
    print(line, file=out)
