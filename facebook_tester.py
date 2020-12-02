# a = [float(x) for x in range(10, 21) if x %2 == 0]
# print(f'array a:{a}')


# b = [[x for x in range(4)] for j in range(4) ]
# print(f'array b: {b}')

# a = [[1,2,3], 
#     [4,5,6], 
#     [7,8,9]]

# a.reverse()
# print(f'array: {a}')

x = 10 
y = 5

x, y = y, x

print('x =', x, 'thank you')
print(f'y = {y}')

# def rotateImage(a):
#     a.reverse()
#     for i in range(len(a)):
#         for j in range(i):
#             a[i][j], a[j][i] = a[j][i], a[i][j]
#     return a
