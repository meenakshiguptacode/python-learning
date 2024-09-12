# WAF to print the elements of a list in a single line. ( list is the parameter)


def print_ln(list):
    for item in list:
        print(item,end=" ")


cities = ["delhi", "gurgoan", "goa" ]

print_ln(cities)