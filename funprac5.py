# WAF to convert USD to INR.


def UsdToInr(num):
    amount = num * 83.93
    return amount


num = int(input("Enter amount for conversion : "))
amount = UsdToInr(num)

print("Amount after conversion: ", amount)


