
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

print("AND Gate")
print("0 AND 0 = ", AND(0, 0))
print("0 AND 1 = ", AND(0, 1))
print("1 AND 0 = ", AND(1, 0))
print("1 AND 1 = ", AND(1, 1))

print("\nOR Gate")
print("0 OR 0 = ", OR(0, 0))
print("0 OR 1 = ", OR(0, 1))
print("1 OR 0 = ", OR(1, 0))
print("1 OR 1 = ", OR(1, 1))

print("\nNOT Gate")
print("NOT 0 = ", NOT(0))
print("NOT 1 = ", NOT(1))

print("\nXOR Gate")
print("0 XOR 0 = ", XOR(0, 0))
print("0 XOR 1 = ", XOR(0, 1))
print("1 XOR 0 = ", XOR(1, 0))
print("1 XOR 1 = ", XOR(1, 1))