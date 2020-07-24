def power(n,a):
    if n==0:
        return 1
    elif n==1:
        return a
    return a*power(n-1,a)
#get the input from the user
print("Enter the input")
input1=int(input())
#calculate power with respective base and exponent
output=power(input1,input1)+power(input1,2)
print(output)
