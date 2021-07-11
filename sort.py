'''
Test sort
'''
print('==========================Test Sort====================================')

l = [('ASDD',123,0.9),('DsdD',13,0.817),('JKKll',781,0.776),('OOkl',89,1.514)]

print(sorted(l,key=lambda x : x[0]))
print(sorted(l,key=lambda x : x[1]))
print(sorted(l,key=lambda x : x[2], reverse = True))

print('-----------------------------------------------------------------------')
l2 = [101,-3.5,99.8,7,-66]
print(sorted(l2,key=abs))
print(sorted(l2,reverse=True))
