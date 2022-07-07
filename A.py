s = input("Enter value:")
dict = {}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(sorted(dict.items()))
file = open('Sample.py')
print(file.read())
file.close()
file = open('Sample.py','w')
file.write("\n#Hello Jwala")
file.close()
#C:\Users\jwalaunique\Desktop\final\chromedriver_win32