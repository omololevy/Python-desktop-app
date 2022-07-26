size = int(input("Enter the size list\n"))
your_list=[]
first_value = input('Enter the first number\n')
your_list.append(first_value)
while len(your_list) < size:
    another_value = input('Enter the next number\n')
    your_list.append(another_value)
    print(your_list)
    odd = []
    even = []
    prime = []
for i in your_list:
    alarm = False
    if int(i)>1:
        for x in range(2, int(i)):
            if int(i)%x == 0:
                alarm = True
                break
        if alarm:
            pass
        else:
            prime.append(i)
    if int(i) % 2 == 0:
        even.append(i)
        
    else:
        odd.append(i)
if len(even) < 2:
    print('Even number is ', len(even)) 
else:  
    print('Even numbers are ', len(even))
if len(odd) < 2:
    print('Odd number is ', len(odd)) 
else:  
    print('Odd numbers are ', len(odd))
if len(prime) < 2:
    print('Prime number is ', len(prime)) 
else:  
    print('Prime numbers are ', len(prime))