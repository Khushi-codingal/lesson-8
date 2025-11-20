print("enter a number(numerator):")
n1 = int(input())
print("enter a number(denominator):")
n2 = int(input())
if n1% n2 == 0:
    print("\n"+str(n1)+"is divisible by"+str(n2))
else:
    print("\n"+str(n1)+"is not divisible by"+str(n2))