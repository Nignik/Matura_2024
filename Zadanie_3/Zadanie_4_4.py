with open("../Dane/liczby.txt") as file:
    dane = file.read().split("\n")

row_1 = [int(x) for x in dane[0].split(" ")]

print(row_1)

prefix = []
prefix.append(0)
for i in range(1, len(row_1)+1):
    prefix.append(prefix[i-1] + row_1[i-1])

best_l = 100000000
best_avg = -1
how_many = -1
print(prefix)
for i in range(50, len(prefix)):
    l, r = 1, i
    while r < len(prefix):
        avg = abs(prefix[r] - prefix[l-1]) / (r - l + 1)

        if best_avg < avg:
            best_avg = avg
            best_l = row_1[l-1]
            how_many = (r-l)
        elif best_avg == avg:
            if l < best_l:
                best_avg = avg
                best_l = row_1[l - 1]
                how_many = (r - l + 1)

        l += 1
        r += 1

print(f"{best_avg} {how_many+1} {best_l}")
