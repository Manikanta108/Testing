#a = [3, 5, 11, 1, 6, 13, 9, 2]
a = [3, 5, 11, 1, 6, 13, 9]

b = max(a)
c = min(a)

print(f'Maximum Value of the given array is: ',b)
print(f'Minimum Value of the given array is: ',c)

d = len(a)
for i in range(d-1):
    for j in range(1, d):
        if(a[i]+a[i+1] == a[j]):
            print("Success")
        else:
            print("No Success")
            break
    break