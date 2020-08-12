#part 1:calculate factorial of given number
#part 2: find the number of trailing 0's in that factorial

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)


def factTrailingzero(number):
    #5=5*4*3*2*1
    #6=6*5*4*3*2*1
    #100!=100//5 + 100//5*5
    count=0
    i=5
    while(number//i!=0):
        count+=int(number/i)
        i=i*5
    return count






if __name__ == '__main__':
    number=int(input("Enter a number: \n"))
    #fac=factorial(number)
    #print(f"Factorial of {number} is:{fac}")
    print(f"Number of trailing zero's:",factTrailingzero(number))

