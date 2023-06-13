# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.


def find(a):
    s=0
    for i in a:
        s+=i
    return int(s/len(a))
print(find(a=[85, 90, 92, 88, 95]))