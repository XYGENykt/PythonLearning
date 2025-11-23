x = int(input())

total = 0
count = 0
multiple = 1
avg = 0

last_digit = x % 10


while x != 0:
    total += x % 10
    multiple *= x % 10
    count += 1
    first_digit = x
    x//=10
    

avg = total / count

summa_first_last_digit = first_digit + last_digit

print(total,count,multiple,avg,first_digit,summa_first_last_digit, sep='\n')