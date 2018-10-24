#!/usr/bin/env python3
all_lang = set()
mutual_lang = set()
all_langueg = set()

for i in range(int(input())):
    for j in range(int(input())):
        langueg = set(input().split())
        all_langueg.update(langueg)
    all_lang.update(all_langueg)
    if i == 0:
        mutual_lang.update(all_langueg)
    else:
        mutual_lang &= all_langueg
    all_langueg = set()

print(len(mutual_lang))
for _ in mutual_lang:
    print(_)
print(len(all_lang))
for _ in all_lang:
    print(_)
