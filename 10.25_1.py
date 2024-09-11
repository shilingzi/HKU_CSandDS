# Q1 (20 marks) A positive integer n > 2 is sacred if n = $$a^2 + b^3$$ for some integers a and
# b. Write a program (using either the programming language C, C++, Java, Python) that
# repeatedly asks the user to input a positive integer n > 2, and prints "YES" if it is sacred,
# and "NO" otherwise. The program stops if a negative integer is input.
# CSDN @Kevin_wzf
def is_scared(n):
    for a in range(int(n**0.5)+1):
        for b in range(int(n**(1/3)+1)):
            if a**2+b**3 ==n:
                return True
    return False
def main():
    while True:
        try:
            n = int(input("please input a postive integer number n>2 or input a negative number to exit program:"))
            if (n<0):
                print("exit program")
                break
            elif (n<=2):
                print("please input a postive number>2")
                continue
            else:
                if is_scared(n):
                    print("YES")
                else:
                    print("NO")
        except:
            print("invalid input, please input a integer")
if __name__ == "__main__":
    main()

