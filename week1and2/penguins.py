#!/usr/bin/env python3

print('This is my first realy cute programm ^_^')
print('Please, write a number and enjoy :3')
quantity = int(input())
qu20 = quantity // 20
qu0 = quantity % 20
while qu20 > 0:
    prinOne = str('   _~_    ')
    print(prinOne*20)
    prinTwo = str('  (o o)   ')
    print(prinTwo*20)
    prinTre = str(' /  V  \  ')
    print(prinTre*20)
    prinFou = str('/(  _  )\ ')
    print(prinFou*20)
    prinFiv = str('  ^^ ^^   ')
    print(prinFiv*20)
    qu20 -= 1
if qu0 > 0:
    prinOne = str('   _~_    ')
    print(prinOne*qu0)
    prinTwo = str('  (o o)   ')
    print(prinTwo*qu0)
    prinTre = str(' /  V  \  ')
    print(prinTre*qu0)
    prinFou = str('/(  _  )\ ')
    print(prinFou*qu0)
    prinFiv = str('  ^^ ^^   ')
    print(prinFiv*qu0)
