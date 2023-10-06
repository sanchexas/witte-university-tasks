# import os

# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, 'numbers.txt')
# f = open(filename, encoding="utf-8")
f = open("numbers.txt")
nums = f.read().strip()
numsAsStrArr = nums.split(" ")
numsArr = []
for i in range(len(numsAsStrArr)):
    if '-' in numsAsStrArr[i]:
        numsArr.append(int(numsAsStrArr[i]))
print(sum(numsArr))