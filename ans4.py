n = []
while True:
    try:
        l = int(input("Enter the size of the array="))
        if l > 0:
            print("Entre the elements=")
            break
    except ValueError:
        print("This is not valid input, Try again with non zero positive value")
else:
    print("Entre non zero positive value")
for i in range(l):
    try:
        array_element = int(input())
        if array_element >= 0:
            n.append(array_element)
            k = n.copy()
            m = len(k)
            o = 2
            a = k[o:m]
            b = k[0:o]
            c = a+b
    except ValueError:
        print("This is not valid input, Try again with non zero positive value")
print("Array=", k)
print("Modified array=", c)