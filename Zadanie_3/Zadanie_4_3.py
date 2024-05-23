import math
from collections import Counter


with open("../Dane/liczby.txt") as file:
    dane = file.read().split("\n")

row_1 = [int(x) for x in dane[0].split(" ")]
row_2 = [int(x) for x in dane[1].split(" ")]

print(row_1)
print(row_2)

ans = []
for l2 in row_2:
    x = l2
    for l1 in row_1:
        if x % l1 == 0:
            x /= l1

    if x == 1:
        print(l2, end=" ")
