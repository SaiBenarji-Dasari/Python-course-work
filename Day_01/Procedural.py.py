n = "Ravi"
p = 500
def Calculate_bill(p):
    tax = p * 0.18
    return p + tax
def print_bill(n, total):
    print("customer:",n)
    print("Total Bill:", total)

total = Calculate_bill(p)
print_bill(n, total)

