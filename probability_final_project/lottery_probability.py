# goal: given a positive integer n, find the probability of selecting six
# integers from the set {1,2,...,n} that were mechanically selected in a lottery

# print purpose of program
print("The purpose of this program is to find the probability of selecting six integers from the set {1,2,...,n} that were mechanically selected in a lottery")

# ask user for a positive integer n
n = int(input("Give me a positive integer equal to or greater than 6: "))
the_set = []
element_count = 1 # establish count to increase each element by 1

# append 1,...,n to the set
for i in range(n):
    the_set.append(element_count)
    element_count += 1 #increment count


# create a factorial function definition to help find number of r-combinations 
def factorial(num:int)->int:
    factorial_result = 1 # start at 1, multiplying by num's factorial until reaching 1 each time
    count = num # for decrementing purposes
    # base cases
    if num == 0:
        return 1 #factorial of 0! is 1
    elif num == 1:
        return num
    # calculate factorial manually 
    else:
        while (count != 1): # can skip multiplying by 1 once we reach it
            factorial_result = count * factorial_result 
            count -= 1 # decrement number 
        return factorial_result
            

# n choose 6, so our formula is n!/r!(n-r)!, where r = 6
r = 6 # set r to 6
if (n < 6): # n is less than 6, not enough integers to calculate probability
    # print report to user
    print("The integer you selected is less than 6, please enter a number equal to or greater than 6 next time.")
else: # n is 6 or greater
    # compute n choose r using formula
    n_choose_r = (factorial(n)/(factorial(r)*factorial(n-r)))
    # according to uniform distribution, there are n possible events each with probability 1/n, so the probability that 6 integers are selected is 1/(total number of events)
    probability = 1/n_choose_r # assign calculation to probability
    # display result to user
    print("The probability of selecting the six integers from the set", the_set, "that were mechanically selected in a lottery is", probability)
    
