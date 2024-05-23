
def gcd(a, c):
    if a == 0:
        return c

    return gcd(c % a, a)


with open("../Dane/skrot2.txt") as file:
    dane = file.read().split("\n")

print(dane)

ans = []
for line in dane:
    if line == '':
        continue

    n = int(line)
    m = 0
    b = 1
    while n > 0:
        temp = n % 10
        if temp % 2 == 1:
            m += b * temp
            b *= 10

        n = n // 10

    if gcd(m, int(line)) == 7:
        ans.append(line)

for liczba in ans:
    print(liczba)

