a = []

n = int(input())
m = int(input())

#int(input("Enter a number: "))

#n = 3
#m = 10

for i in range(n):

    a.append(i)

#print(a)

b = []

b = a

for i in range(m):

    if i>=n:

        res = 0

        for j in range(n):

            res = b[i-(j+1)]+res

        b.append(res)
        #print(res)

print(b)