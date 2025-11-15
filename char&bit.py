
#char-stuffing
data = input("Enter data: ")
sd = input("Start delimiter: ")
ed = input("End delimiter: ")

res = sd
for ch in data:
    if ch == sd or ch == ed:
        res += ch
    res += ch
res += ed

print("Stuffed data:", res)





#bit stuffing
bits = input("Enter bit string: ")

count = 0
result = ""
for b in bits:
    result += b
    if b == '1':
        count += 1
        if count == 5:
            result += '0'
            count = 0
    else:
        count = 0

print("Stuffed bits:", result)








#checksome
a = input("Enter 1st binary: ")
b = input("Enter 2nd binary: ")

carry = 0
res = ""

for i in range(len(a)-1, -1, -1):
    s = int(a[i]) + int(b[i]) + carry
    res = str(s % 2) + res
    carry = s // 2

checksum = ""
for bit in res:
    checksum += '1' if bit == '0' else '0'

print("Sum :", res)
print("Checksum :", checksum)


