
def gcd(a, c):
    if a == 0:
        return c

    return gcd(c % a, a)


with open("../Dane/skrot.txt") as file:
    dane = file.read().split("\n")

print(dane)

cnt = 0
najwieksza = -1
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

    print(m)

    if m == 0:
        najwieksza = max(najwieksza, int(line))
        cnt += 1

print("Opowiedz 1: ", cnt)
print("odpowiedz 2: ", najwieksza)