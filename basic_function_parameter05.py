# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.


def unlilar_soni(text):
    s=0
    unli=['a','e','i','o','u','A','E','I','O','U']
    for i in text:
        if i in unli:
            s+=1

    # for j in unli:
    #     print(j)
    return s
print(unlilar_soni(text='Hello world'))

