#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# def generate_primes():
#     prime_string = ''
#     num = 2
    
#     while len(prime_string) < 10005:
#         for prime_divide in range(2, num):
#             if (num % prime_divide) == 0:
#                 break
#         else:
#             prime_string += str(num) 
#         num += 1

#     return prime_string

    

# def solution(i):
    
#     generated_prime_string = generate_primes()
#     return generated_prime_string[i:i+5]


# print(solution(0))

# def genrate_prime_num_string():
#     """ genrating prime number string by mathametical formula 
#         execution time is around 2.5 to 2.8 sec for 0 to 25000
#     """
#     PRIME_NUMBER_STRING=''
#     for num in range(2,25000):
#         for i in range(2, num):
#             if (num % i) == 0: # if true mean number is not prime
#                 break
#         else:
#             # number is prime
#             PRIME_NUMBER_STRING+=str(num)

#     return PRIME_NUMBER_STRING
# #calling genrate function and holding data in global 
# #so function can be called multiple time with generating 
# #prime string each time 



# def solution(i):
#     """
#     solution is standard function
#     i is index in prime list
#     so retuen will be index i to i+1
#     """
#     PRIME_NUMBER_STRING = genrate_prime_num_string()
#     return PRIME_NUMBER_STRING[i:i+5]

#print(solution(0))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#A function to check if the string of str1 is greater than the string of str2
def num1_greaterthan_num2(str1, str2, dec1_inx, dec2_inx):
    
    #creates a variable for the index of the first decimal in each version
    #the first call of this function sets this index to 0.
    str1_first_dec_inx = dec1_inx 
    str2_first_dec_inx = dec2_inx 

    #checks to see if there is a decimal in each string version given and sets 
    #my index variable to the index of that decimal. Else, sets index to end of 
    #the string if no decimal is present 
    if '.' in str1:
        str1_first_dec_inx = str1.index('.')
    else: 
         str1_first_dec_inx = len(str1)

    if '.' in str2:
        str2_first_dec_inx = str2.index('.')
    else: 
         str2_first_dec_inx = len(str2)


    #creates a variable to house a portion of str1 and str2 from a starting   
    #index to a required ending index for comparisons
    str1_checker = ''
    str2_checker = ''


    #sets both string checker variables to the portion of the string from 
    #the beginning of the string to the index of the first decimal or end
    for char1 in str1[:str1_first_dec_inx]:
        str1_checker += char1

    for char2 in str2[:str2_first_dec_inx]:
        str2_checker += char2 


    #comparison logic to see if which string checker(from beginning to first 
    # decimal or end) is greater  
    if int(str1_checker) > int(str2_checker): 
        return True 
    elif int(str1_checker) < int(str2_checker): 
        return False
    
    #comparison logic to see if both string checkers are the same but only one 
    # has a decimal in the string. If so the checker with the decimal 
    # is automatically greater
    elif (str2_first_dec_inx == len(str2)) and (str1_first_dec_inx != len(str1)):
        return True 
    elif (str1_first_dec_inx == len(str1)) and (str2_first_dec_inx != len(str2)):
        return False
   

    #if all previous comparisons fail then we must have two checkers 
    #that equal the same but are followed by a decimal point with additional 
    # numbers. Use recursion here to use the logic of this greater_than 
    # function to compare these following digits
    else:
        is_Greater = num1_greaterthan_num2(
        str1[str1_first_dec_inx + 1:], 
        str2[str2_first_dec_inx + 1:], 
        str1_first_dec_inx,
        str2_first_dec_inx)

    #return the result of if the digits after str1 are greater than the digits 
    # that are following str2
    return is_Greater



#Basic Mergesort Algorithm 
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if num1_greaterthan_num2(left[left_index], right[right_index], 0, 0):
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
        
    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

#this solution calls on the recursive power of mergesort to seperate and sort each  
#elevator version in the given array. It determines if one string version is greater than or 
#less than anotehr version based off the properties of my num1_greaterthan_num2() function. 
def solution(l):
    if len(l) <= 1:
        return l
    
    mid = len(l) // 2

    left_half = l[:mid] 
    right_half = l[mid:]

    left = solution(left_half)
    right = solution(right_half)

    return merge(left, right)

#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
#print(0.0 == 0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

from collections import deque
 
def solution(src, dest):
    OFFSETS = [17, -17, 15, -15, 10, -10, 6, -6]
    q, visited = deque([(0, src)]), set([src])
    min_moves = float('inf')
    while q:
        moves, curr = q.popleft()
        if curr == dest:
            return moves
        for offset in OFFSETS:
            next_sqr = curr + offset
            if next_sqr not in visited and 0 <= next_sqr <= 63:
                visited.add(next_sqr)
                q.append((moves + 1, next_sqr))
    return min_moves
 
assert solution(0, 1) == 3
assert solution(19, 36) == 1
assert solution(0, 32) == 2
print("PASSED!")