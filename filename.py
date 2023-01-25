class A:
    def m1(self,*x):
        print("values is x:",x)
    def m1(self,y,c):
        print("values is y:", y)
a = A()
# a.m1()
# a.m1(10)
a.m1(10,20)