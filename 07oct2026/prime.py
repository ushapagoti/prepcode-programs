number = int(input("enter the number: "))
starting = 2
is_prime = True
while(starting < number):
    
    if number % starting == 0:
        is_prime = false
    starting +=1
print(is_prime)