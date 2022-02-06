finput = open("C:\\Users\\ben\\Desktop\\usaco\\word.txt", "r")

lines = finput.readlines()
print(lines)

(words, maxchars) = lines[0].strip().split(" ")
(essay) = lines[1].strip().split(" ")
print(essay)

wordlength = 0
current_word = []
essay = []
for x in range(len(essay)):
    wordlength += len(essay[x])
    if wordlength < maxchars+1:
        current_word.append(essay[x] + " ")
    else:
        essay.append(current_word)
        wordlength = 0

print(essay)

with open('C:\\Users\\ben\\Desktop\\usaco\\word.out', 'w') as out:
    print("3", file=out)
