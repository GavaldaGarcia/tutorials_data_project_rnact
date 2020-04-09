import random

def my_sum_function(value_0, value_1):
    sum_result = value_0 + value_1
    
    return sum_result 


def my_substraction_function(value_0, value_1, reverse=False):
    if not reverse:
        substraction_result = value_0 - value_1
    else:
        substraction_result = value_1 - value_0
    
    return substraction_result


def factorial(n):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i 

    return fact


def random_insult():
    # generate insults lists
    insults_list = []
    insults_file = open('insults.csv', 'r')
    for line in insults_file:
        for insult in line.rstrip().split(','):
            insults_list.append(insult)
    
    ultimate_insult = random.choice(insults_list)
    return ultimate_insult
    