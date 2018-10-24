mylist = list(input().split())
# myset = set()
for i in mylist:
    if i in myset:
        print('YES')
    else:
        print("NO")
        myset.add(i)
