n = int(input())

number = int(input())
largest = number   
before_largest = largest

for i in range(n-1):
    number = int(input())
    
    
    if number > largest:
        if number > before_largest:
            before_largest = largest
        largest = number    
    
print(largest)    
print(before_largest)    