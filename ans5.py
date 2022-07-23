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
    except ValueError:
        print("This is not valid input, Try again with non zero positive value")
print("Array=", k)
if all(k[i] <= k[i + 1] for i in range(len(k) - 1)) or all(k[i] >= k[i + 1] for i in range(len(k) - 1)):
    print("Yes it is monotonic")
else:
    print("It is not Monotonic")