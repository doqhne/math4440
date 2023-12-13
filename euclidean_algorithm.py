'''Calculate the gcd of 2 numbers using the euclidean algorithm'''
num1 = int(input('Please enter the first number for the gcd: '))
num2 = int(input('Please enter the second number for the gcd: '))

# make sure a is larger than b
a = max(num1, num2)
b = min(num1, num2)

def get_gcd(a, b):
    # gcd(0, n) = n
    if b == 0:
        return a
    
    # continue finding residues until we get zero
    while b != 0:
        residue = a%b
        # success, return the gcd
        if residue == 0:
            return b 
        # keep going
        else:
            # shift a and b
            a = b
            b = residue
            
print(f'gcd({num1}, {num2}) = {get_gcd(a, b)}')