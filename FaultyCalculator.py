print("This is a calculator\n" + "Enter the two numbers")

N1 = int(input())
N2 = int(input())
sum = N1 + N2
multi = N1 * N2
devide = N1 / N2
if N1 == 56 and N2 == 9 and sum == 65:
    print("Default calculator")
elif N1 == 45 and N2 == 3 and multi == 135:
    print("Default calculator")
elif N1 == 24 and N2 == 6 and devide == 4:
    print("Default calculator")
else:
    print(sum)
    print(multi)
    print(devide)
