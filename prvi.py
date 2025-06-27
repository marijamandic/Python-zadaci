print("Enter a value in the form 'base-exponent'. Example: 3-2.")

bases = []
exponents = []

while True:

    x = input("Enter a value: ")

    if "-" not in x:
        raise ValueError("Incorrect input => accepted format: base-exponent (e.g., 2-3)")


    b, e = x.split("-")

    b = int(b)
    e = int(e)

    if b <= 0 or e <= 0:
        raise ValueError("Both the base and the exponent must be positive values greater than 0.")
    
    bases.append(b)
    exponents.append(e)

    while True:
        answer = input("Add a value? (y/n): ")
        if answer == "y" or answer == "n" or answer == "Y" or answer == "N":
            break
        else:
            print("Incorrect input. Add a value? (y/n):")

    if answer == "n" or answer == "N":
        break

output = []
result = 0

for i in range(len(bases)):
    output.append(f"{bases[i]}^{exponents[i]}")
    result += bases[i] ** exponents[i]

print(" + ".join(output), "=", result)

