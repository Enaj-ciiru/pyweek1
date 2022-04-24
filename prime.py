#function to check if function is prime or not

#composite numbers are numbers that have more than two factors

def primecheck(n):  
    # checking that given number is more than 1  
    if n > 1:  
        # iterating over the given number with for loop  
        for i in range(2, int(n/2)):  
            # If the given number is divisible or not  
            if (n % i) == 0:  
                print(n, "is not a prime number")  
                break  
        else:  
            print(n, "is a prime number")  
    # if given number is 1 or 0
    else:  
        print(n, "is neither prime nor composite")  
# taking an input number from the user  
a = int(input("Enter an input number:"))  
# print result  
primecheck(a)