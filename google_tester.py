# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
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


# #print(solution(0))

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

# #print(solution(0))

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# #A function to check if the string of str1 is greater than the string of str2
# def num1_greaterthan_num2(str1, str2, dec1_inx, dec2_inx):
    
#     #creates a variable for the index of the first decimal in each version
#     #the first call of this function sets this index to 0.
#     str1_first_dec_inx = dec1_inx 
#     str2_first_dec_inx = dec2_inx 

#     #checks to see if there is a decimal in each string version given and sets 
#     #my index variable to the index of that decimal. Else, sets index to end of 
#     #the string if no decimal is present 
#     if '.' in str1:
#         str1_first_dec_inx = str1.index('.')
#     else: 
#          str1_first_dec_inx = len(str1)

#     if '.' in str2:
#         str2_first_dec_inx = str2.index('.')
#     else: 
#          str2_first_dec_inx = len(str2)


#     #creates a variable to house a portion of str1 and str2 from a starting   
#     #index to a required ending index for comparisons
#     str1_checker = ''
#     str2_checker = ''


#     #sets both string checker variables to the portion of the string from 
#     #the beginning of the string to the index of the first decimal or end
#     for char1 in str1[:str1_first_dec_inx]:
#         str1_checker += char1

#     for char2 in str2[:str2_first_dec_inx]:
#         str2_checker += char2 


#     #comparison logic to see if which string checker(from beginning to first 
#     # decimal or end) is greater  
#     if int(str1_checker) > int(str2_checker): 
#         return True 
#     elif int(str1_checker) < int(str2_checker): 
#         return False
    
#     #comparison logic to see if both string checkers are the same but only one 
#     # has a decimal in the string. If so the checker with the decimal 
#     # is automatically greater
#     elif (str2_first_dec_inx == len(str2)) and (str1_first_dec_inx != len(str1)):
#         return True 
#     elif (str1_first_dec_inx == len(str1)) and (str2_first_dec_inx != len(str2)):
#         return False
   

#     #if all previous comparisons fail then we must have two checkers 
#     #that equal the same but are followed by a decimal point with additional 
#     # numbers. Use recursion here to use the logic of this greater_than 
#     # function to compare these following digits
#     else:
#         is_Greater = num1_greaterthan_num2(
#         str1[str1_first_dec_inx + 1:], 
#         str2[str2_first_dec_inx + 1:], 
#         str1_first_dec_inx,
#         str2_first_dec_inx)

#     #return the result of if the digits after str1 are greater than the digits 
#     # that are following str2
#     return is_Greater



# #Basic Mergesort Algorithm 
# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if num1_greaterthan_num2(left[left_index], right[right_index], 0, 0):
#             merged.append(right[right_index])
#             right_index += 1
#         else:
#             merged.append(left[left_index])
#             left_index += 1
        
#     merged += left[left_index:]
#     merged += right[right_index:]
        
#     return merged

# #this solution calls on the recursive power of mergesort to seperate and sort each  
# #elevator version in the given array. It determines if one string version is greater than or 
# #less than anotehr version based off the properties of my num1_greaterthan_num2() function. 
# def solution(l):
#     if len(l) <= 1:
#         return l
    
#     mid = len(l) // 2

#     left_half = l[:mid] 
#     right_half = l[mid:]

#     left = solution(left_half)
#     right = solution(right_half)

#     return merge(left, right)

# #print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
# #print(0.0 == 0)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

 
# board_length = 8
# board = [None] * 64
 
# def move_tracker(moves, cell_from):
#     def select_value(old, new):
#         if old is None:
#             return (new, True)
   
#         value = min(old, new)
 
#         return (value, value == new and new != old)
 
#     for move in moves:
#         board[move], updated = select_value(board[move], board[cell_from] + 1)
 
#         if updated:
#             new_moves = all_moves(move)
#             move_tracker(new_moves, move)
 
 
# def all_moves(src):
#     def is_valid_move(row, column):
#         return (row >= 0) and (row <= board_length - 1) and (column >= 0) and (column <= board_length - 1)
 
#     moves = [None] * board_length
 
#     row = src // board_length
#     column = src % board_length
 
#     moves[0] = src - 1 - 2 * board_length if is_valid_move(row - 2, column - 1) else None
#     moves[1] = src + 1 - 2 * board_length if is_valid_move(row - 2, column + 1) else None
#     moves[2] = src + 1 + 2 * board_length if is_valid_move(row + 2, column + 1) else None
#     moves[3] = src - 1 + 2 * board_length if is_valid_move(row + 2, column - 1) else None
#     moves[4] = src - 2 - 1 * board_length if is_valid_move(row - 1, column - 2) else None
#     moves[5] = src + 2 - 1 * board_length if is_valid_move(row - 1, column + 2) else None
#     moves[6] = src + 2 + 1 * board_length if is_valid_move(row + 1, column + 2) else None
#     moves[7] = src - 2 + 1 * board_length if is_valid_move(row + 1, column - 2) else None
 
#     return [move for move in moves if move is not None]
 

# def solution(src, dest):

#     moves = all_moves(src)
#     board[src] = 0
#     move_tracker(moves, src)
 
#     return board[dest]
 
# #print(solution(0, 1))
# #print(solution(0, 1))

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 2.2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 3.1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# def xor_sum(n):
#     val = n % 4
#     if val == 0:
#         return n
#     elif val == 1:
#         return 1
#     elif val == 2:
#         return n + 1
#     return 0

# def solution(start, length):
#     if length == 1:
#         return start
#     val = xor_sum(start + 2*(length-1))
    
#     if start > 1:
#         val = val ^ xor_sum(start - 1)
#     for i in range(length-2):
#         elems = length - 2 - i
#         init = start + length*(2 + i) - 1
#         val = val ^ xor_sum(init + elems) ^ xor_sum(init)
        
#     return val
# #print(solution(0, 3))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ level 3.3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def factor_hash():
    two facts = {}
    base = 2
    while len(str(base)) <= 309:
        twofacts[base] = True
        base = base * 2
    return two facts


def answer(n):
    factors = factor_hash()
    count = 0
    n = int(n)
    while n != 1:
        if n-1 in factors:
            n = n-1
            count += 1
        elif n+1 in factors:
            n = n+1
            count += 1
        elif n % 2 != 0:
            n = n+1
            count += 1
        n = n // 2
        count += 1
    return count


# assert answer(15) == 5
# assert answer(4) == 2
# assert answer(3) == 2
# assert answer(2) == 1
# assert answer(6) == 3




# def solution(n):
#     count = 0
#     n = int(n)

#     while(n > 1):
#         if (n % 2 == 0):
#             n //= 2
#         else:
#             high = n+1
#             low = n-1
#             high_count = low_count = 0
#             while(high % 2 == 0):
#                 high //= 2
#                 high_count += 1
#             while(low % 2 == 0):
#                 low //= 2
#                 low_count += 1
#             #Exception for number 3 since it can be divided in less steps than 4.
#             if (high_count > low_count and n != 3):
#                 n += 1
#             else:
#                 n -= 1
#         count += 1
#     return count

# print(answer('1'))
# print(answer('2'))
# print(answer('4'))







