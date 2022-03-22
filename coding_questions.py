#question one
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
def hello_name(user_name):
    print(f"Hello_{user_name}!")

#question two

def first_odds():
    #Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
    odd = 1
    while odd < 101:
        if odd % 2 ==1: 
            print(odd)
        odd += 1

#question three
def max_num_in_list(a_list):
    #Please write a Python function, max_num_in_list to return the max number of a given list.
    max = 0
    for num in a_list:
        max += 1

    return max

#question four

def is_leap_year(a_year):
    #Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
    if a_year % 4 == 0:
       return True 
    elif a_year % 100 == 0:
        if a_year % 400 == 0:
            return True
    else:  
        return False

#question 5

def is_consecutive(a_list):
    #Write a function to check to see if all numbers in the list are consecutive numbers.
   length = len(a_list)
   x = a_list[0]
  
    
   for i in a_list:
      
       
      
       if x != i:
          #print( i, x)
           return False
       else:
           x = x+1
           continue
   return True

   


#print(is_consecutive([7,8,9,10,11])) 
   


