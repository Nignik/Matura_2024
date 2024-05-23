with open("../Dane/liczby.txt") as file:
    dane = file.read().split("\n")

cnt = 0

row_1 = dane[0].split(" ")
row_2 = dane[1].split(" ")

print(row_1)
print(row_2)

for l1 in row_1:
    for l2 in row_2:
        if int(l2) % int(l1) == 0:
            cnt += 1
            break

print(cnt)