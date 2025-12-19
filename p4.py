# for i in range(10, 20, 2):
#     print(i)


# def func1(*args):
#     print(args)

    # s = 0
    # for i in m:
    #  s+=i
    # s = sum(args)

    # func(1,2)

def func2(**kwargs):
   # print(kwargs)
    for k, v in kwargs.items():
        print(k,v)
        func2(isn="alish", yosh=19,vazin=666)