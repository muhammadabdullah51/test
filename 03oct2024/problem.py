# working for just single digit
# def fn(arr):
#     string = "".join(map(str, arr))
#     num = int(string)
#     newNum = num+1
#     newNum = str(newNum)
#     empty_arr = []
#     for nums in newNum:
#         empty_arr.append(int(nums))
#         print(empty_arr)
# fn([7,8,8,8,9,10])


# working for all 
def fn2(arr2):
    arr3 = arr2[0:-1]
    arr4 = arr2[-1]
    arr4 += 1 
    arr3.append(arr4)
    print(arr3)
fn2([6,7,3])

# a = '1'
# b = '2'
# c = a+b
# d = int(c)
# print(d+1)
