def fib(n):

    if n <= 0:
        return 0
    elif n < 2: 
        return 1

    return fib(n-1) + fib(n-2)

print(fib(10))

# def dynamicFib(num):

#     fib[0] = 0
#     fib[1] = 1

#     # for i in range(2, num):
#     #     fib[i] = fib[i-1] + fib[i-2]

#     return fib[num]

#     print(dynamicFib(0))


def minOp(str1, str2):
    str_count = 0

    if len(str1) < len(str2):
        for ele in str1:
            if ele in str2:
                str_count +=1 
    else:
        for ele in str2:
            if ele in str1
                str_count +=1 

    return max(len(str1), len(str2)) - str_count

print(minOp('sundayy', 'sunday'))



#   def minOp(str1, n, str2, m):

#             if (m == 0):
#                 return n

#             if (n == 0):
#                 return m

#             if (str1[n-1] == str2[m-1]):
#                 return minOp(str1, n -1, str2, m -1)

#             return 1 + (min(minOp(str1, n, str2, m-1),  minOp(str1, n-1, str2, m), minOp(str1, n-1, str2, m-1)))

#         return minOp(word1, len(word1), word2, len(word2))


# def stairs(n):

#     if n - 2 > 0:
#         return 2

#     return n


# Input: 3

# Output: 4

# 1 + 2 + 1 = 4
# 2 + 1 + 1 = 4
# 1 + 1 + 1 + 1 = 4
# 2 + 2 = 4
# 1 + 1 + 2 = 4


#print(stairs(5))

# Input: D = 1, F = 6, Target = 4
# Output: 1

# def dice_prob(dice, face, target):
    

# def coin_count(change):
    
#     coin_hash = {"penny" : 0, "knickel" : 0, "dime" : 0, "quarter": 0}
    
#     if change >= 25:
    
#         while change >= 25:
#             change = change - 25 
#             coin_hash["quarter"] += 1
    
#     if change >= 10: 
#         while change >= 10:
#             change = change - 10 
#             coin_hash["dime"] += 1
            
        
#     return coin_hash 
     

# def get_nums(code):
#         code = str(code)
#         idx = len(code) - 1
        
#         if idx <= 0: return "Input must be greater than 0"
            
#         res = 0
#         if code[idx] != '0':
#             res += get_nums(idx - 1)
#         if idx > 0 and code[idx-1] != '0' and int(code[idx-1:idx+1]) <= 26:
#             res += get_nums(idx - 2)
            
#         return res + 1

# print(get_nums(123))

# def fewest_coins(coins, amount):
#     count = 0

#     for coin in coins[::-1]:
#         while amount - coin >= 0: 
#             amount = amount - coin
#             count += 1

#     return count if amount == 0 else -1

# print(fewest_coins([1,2,4,5], 15))


