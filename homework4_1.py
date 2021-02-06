import time, sys

def test_if_prime(number):
#func: test if 'number' is prime by definition. it can be further optimized by many methods, 
#most cerainly by the Fermat primality test
#param: (int)'number' the number to evaluate
#return: (bool) True if prime, False if not prime

    divisibility = 0
    
    for k in range(2,  number+1):
        if number % k == 0:
            divisibility += 1
            #print("%d divisible by %d" %(number, k))
    if divisibility == 1:
        #print("Success! %d is only divisible by 1 and itself!" %(number))
        return True
    else: 
        #print("Fail! %d is not prime as it is divisible by another %d numbers besides 1 and itself" %(number, divisibility - 1))
        return False   

def create_prime_list(size):
#func: fill a list with prime numbers
#param: (int)'size' the amount of natural numbers to evaluate
#return: (list) a copy of a list (if C i'll be returning a pointer, so this all seems like magic) 
#and (int)the duration of the process

    #zero is not a prime number because althougth it can be divisible by 1, there is no definition for the division by zero
    #one is not a prime number because it has no two different factors by it could be divided (1 and 1 are the same!)
    start = time.time()
    
    aux_list = []
    for i in range(0, size):
        if test_if_prime(i) == True:
            aux_list.append(i)
    end = time.time()
    
    return(aux_list, end - start)

process_time = 0
if len(sys.argv) > 1 : 
#if the second index of sys.argv exist it is because an external paramether has been pass, and so take that one
    check_size = int(sys.argv[1])
else:
#else take the constant one    
    check_size = 100
    
prime_list, process_time = create_prime_list(check_size)

if len(prime_list) > 0:
    print("During a %.4f seconds process, the following %d primes has been found: %s." %(process_time, len(prime_list), prime_list))
else: 
    print("The were no primes numbers found in the selected range")