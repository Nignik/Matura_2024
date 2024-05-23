with open("../Dane/liczby.txt") as file:
    dane = file.read().split("\n")

row_1 = [int(x) for x in dane[0].split(" ")]
print(row_1)

row_1.sort(reverse=True)

print(row_1[100])

