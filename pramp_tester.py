import copy

# def calcProductArray(arr):
#     n = len(arr)
#     productArr = []

#     if(n == 0 or n == 1):
#         # no values to multiply if n equals to 0 or 1
#         return []

    
#     product = 1
#     for i in range(0, n):
#         productArr.append(product)
#         product *= arr[i]

#     product = 1
#     for i in range(n-1, -1,):
#         productArr[i] *= product
#         product *= arr[i]

#     return productArr


# arr = [2, 7, 3, 4]

# print(calcProductArray(arr))

# # arr = []
# # arr.append(1)
# # arr.append(4)

# # print(arr)

# def checker(str1, str2):
#     count = 0

#     if len(str1) > len(str2):
#         for inx, ele in enumerate(str1):
#             if str1[inx] not in str2:
#                 count +=1
#     else:
#          for inx, ele in enumerate(str2):
#             if str2[inx] not in str1:
#                 count += 1

#     return count

# print (checker('boat', 'got')) 


# document = "Practice makes perfect. you'll only. get Perfect by practice. just practice!"

#Naive solution:
#1.) seperate all the words in the string by white spaces
#2.) creat hash and use each word as a key for a hash
#3.) iterate again through string and count each word.
#4.) Update accordingly in hash
#5.) iterate through hash and save the key, value pairs in an array of arrays
#6.) return my array of arrays

# def fixed_word(word):
#   word = word.lower()
#   pun = 'abcdefghijklmnopqrstuvwxyz'

#   for inx, char in enumerate(word):
#     if char not in pun:
#       word = slice(inx-1, 1)

#   return word


# def word_count_engine(document):
#   words = document.split(" ")
#   return_array = []

#   word_hash = {}

#   for word in words:
#     word = fixed_word(word)
#     if word in word_hash:
#       word_hash[word] += 1
#     else:
#       word_hash[word] = 0

#   i = 0

#   #for key, value in word_hash.items():
#   # return_array[i] = [key, str(value)]
#   #i += 1

#   for key, value in sorted(word_hash.items(), key=lambda item: -1*item[1]):
#     return_array.append([key, str(value)])

#   return return_array


# input:  document = "Practice makes perfect. you'll only
# get Perfect by practice. just practice!"

# output: [["practice", "3"], ["perfect", "2"],
#          ["makes", "1"], ["youll", "1"], ["only", "1"],
#          ["get", "1"], ["by", "1"], ["just", "1"]]


# def find_array_quadruplet(arr, s):
#     arr.sort()
#     return_arr = []
#     i = 0

#     while i+3 <= len(arr) - 1:
#       if arr[i] + arr[i+1] + arr[i+2] + arr[i+3] == s:
#         return_arr = [arr[i], arr[i+1], arr[i+2], arr[i+3]]
#         return_arr.sort()
#         return return_arr
#       i += 1

#     return []


# arr = [4,4,4,4]
# s = 16

# print(find_array_quadruplet(arr, s))

'''
arr.sort()
 n log(n)
O(n^4)

O(1) space
for first in arr:
  n of first
  for second in arr:
    n of second
[a,s,g,h,d,0, 4 ,7, 9]
'''

# [0, 1, 2, 3, 4, 5, 7, 9]
#  0  1  2  3  4  5  6  8


# def find_array_quadruplet(arr, s):
#   arr.sort()
#   for i in range(len(arr) - 3):  # first
#     first = arr[i]  # first = 0
#     for j in range(i + 1, len(arr) - 2):
#       second = arr[j]
#       third, fourth = two_sum(arr, j + 1, len(arr) - 1,
#                               s - first - second)  # -1, -1
#       if third == -1 and fourth == -1:
#         continue
#       if first + second + third + fourth == s:
#         return [first, second, third, fourth]
#   return []
#   #            [5, 7, 9], 16


# def two_sum(arr, start, end, target):
#   if start >= end:
#     return -1, -1
#   if arr[start] + arr[start + 1] > target or arr[end] + arr[end - 1] < target:
#     return -1, -1
#   while start < end:
#     if arr[start] + arr[end] == target:
#       return arr[start], arr[end]
#     elif arr[start] + arr[end] < target:
#       start += 1
#     else:
#       end -= 1
#   return -1, -1


# def bracket_match(text):

#   open_count = 0
#   close_count = 0

#   for char in text:
#     if char == '(':
#       open_count += 1
#     elif char == ')':
#       if open_count > 0:
#         open_count -= 1
#       else:
#         close_count += 1

#   return open_count + close_count


#def four_sum(arr, sum):
    #identify the sum/2 + 1 different two sums that equal sum
    #whithin a while loop up to len(n) / 2 + 1
    #iterate through the array looking for 1/2 of the two (two sums combo)
    #keep track of All the indices that give you a two sum
    #if found iterate through the the list again looking for the second half without duplicates
    #if found create arrays of the combinations and place in a return array
    #return that return array

# def four_sum(arr, sum):
#     sum1 = sum
#     sum2 = 0
#     # arr.sort()
#     half_sum = []
#     return_arr = []
#     repeat_hash = {}

#     while sum1 >= sum2:
        
#         inx = 0
#         sum_hash = {}
        
#         while (inx < len(arr)):
#             diff = sum1 - arr[inx]
#             if diff not in sum_hash:
#                 sum_hash[arr[inx]] = True
#             elif (diff in sum_hash) and ((diff and arr[inx]) not in repeat_hash):
#                 half_sum.append([arr[inx], diff])
#                 repeat_hash[diff] = True
#                 repeat_hash[arr[inx]] = True
#             inx += 1

#         inx = 0
#         sum_hash = {}

#         if (len(half_sum) > 1) and (half_sum[0][0] + half_sum[0][1] + half_sum[1][0] + half_sum[1][1] == sum):
#             return_arr.append([half_sum[0][0], half_sum[0][1], half_sum[1][0], half_sum[1][1]])
#         elif arr[0] + arr[1] + arr[2] + arr[3] == sum:
#             return_arr.append([arr[0],arr[1],arr[2],arr[3]])

#         while (inx < len(arr)):
#             diff = sum2 - arr[inx]
#             if diff not in sum_hash:
#                 sum_hash[arr[inx]] = True
#             elif (diff in sum_hash) and ((diff and arr[inx]) not in repeat_hash):
#                 temp_sum = []
#                 for ele in half_sum:
#                     temp_sum = copy.copy(ele)
#                     temp_sum.append(arr[inx])
#                     temp_sum.append(diff)
#                     return_arr.append(temp_sum)
                    
              
#             inx += 1
            
#         half_sum = []
#         sum1 -= 1
#         sum2 += 1

#     return return_arr


# arr = [-3, -1, 0, 2, 4, 5]
# print(four_sum(arr, 0))


# test_dict = {'map': 3, 'happy': 2, 'gobble': 4, 'park': 9}
# stringer = {k:str(v) for k,v in test_dict.items()}

# sorted_test = sorted(test_dict.items(), key = lambda x: -x[1])

print(sorted_test)
