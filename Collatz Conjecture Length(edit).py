#The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1. If you repeat the process continuously for n, n will eventually reach 1.
#For example, if n = 20, the resulting sequence will be:
#[20, 10, 5, 16, 8, 4, 2, 1]
#Write a program that will output the length of the Collatz Conjecture for any given n.
#In the example above, the output would be 8.

def collatz(n):
    c_c = [];
    c_c.append(n);
    if n // 2 == 0:
        n = n / 2
        c_c.append(n)
    print(c_c)

collatz(20)
