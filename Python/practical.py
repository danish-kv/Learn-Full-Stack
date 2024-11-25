word = "wwoppopdbdhsblolkkokk"
c = 0
for i in range(len(word)):
    temp = ''
    for j in range(i+1,len(word)):
        temp += word[j]
        if len(temp) > 1:
            if temp == temp[::-1]:
                c += 1
# print(c)


arr = [[1, 2], [3, [4, 5]], 6]
# [6, [[5, 4], 3], [2, 1]
def rev(arr):
    res=[]
    arr.reverse()
    for i in arr:
        if isinstance(i, list):
            res.append(rev(i))
        else:
            res.append(i)
    return res

print(rev(arr))