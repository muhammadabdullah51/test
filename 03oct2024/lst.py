def fn():
    lst2 = [5,2,90,24,5,2,90]
    # lst3 = [10,222,90,24,5,2,90]
    # comb_list = list(zip(lst2, lst3))
    # lst2.reverse()
    # res = list(dict.fromkeys(lst2))
    # res = list(filter(myfilter, lst2))

    # list comprehension
    # res = [num for num in lst2 if num>10]


    # mapping
    xby2oflst = list(map(xby2, lst2))
    # return res
    lst2d = [[1,2],
             [3,4],
             [4,5]]
    lst_res = [num for each_lst in lst2d for num in each_lst]
    mostFreq = max(set(lst2), key=lst2.count)

    a = [3,4,5]
    b = [6,7]
    a.extend(b)
    return a


def xby2(num):
    return num*2

def myfilter(num):
    if num%2==0:
        return num
print(fn())