lines = "2 2 11 4 9 7 9"
lines = [int(i) for i in lines.split(" ")]

lines.sort(reverse = False)
print(lines)
a = lines[0]
b = lines[1]
c = lines[6]-a-b

print(a, b, c)
