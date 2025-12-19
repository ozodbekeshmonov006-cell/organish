# def salom_ber():
#     print("hello")

# salom_ber()
# salom_ber()

# def salom_ber(a,b,s=0):
#     print(a+b+s)

# salom_ber(1,2,3)
# salom_ber(4,5,6)

#     print(a+b+s)
#     return a*b*s

# print(salom_ber(2,4))
# print (salom_ber(5,6,8))


# def salom_ber(a,b,c=0):
#     n=a+b+c
#     m=a*b*c
#     return n,m
# print(salom_ber(2,4))
# print(salom_ber(5,6,8))

def funk1(a):
    if a == 1:
        return 1
    return a + funk1(a-1)
print(funk1(5))