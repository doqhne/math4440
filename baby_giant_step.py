'''Solve the discrete log problem using the baby-step giant step algorithm'''

import numpy as np

# --- EDIT THESE VALUES ---
attempts = 20 # length of lists to generate
g = 2 # base
p = 11 # prime/modulus
h = 7 # g^a
N = int(np.ceil(np.sqrt(p-1)))

print(f'Solving g^a = h (mod p) given g={g}, h={h}, p={p}')

# baby-step giant-step algorithm
baby_list = []
giant_list = []
for i in range(1, attempts+1):
    baby_list.append(pow(g, i, p)) # successive powers of g: g^i
    gN = pow(g, int(-1*N), p) # g^-N mod p
    giant_list.append((h*pow(gN, i, p))%p) # successive powers of h*g^-Ni

# find intersections between lists: c=common elements, bi=index in baby_step list, gi=index in giant_step list
c, bi, gi = np.intersect1d(np.array(baby_list), np.array(giant_list), return_indices=True)

if len(c)==0:
    print("No collisions found :(")
else:
    j = bi[0]+1 # power g was raised to for the collision
    k = gi[0]+1 # power g^-N was raised to for the collision
    a = int(j+ (k*N))
    print(f'a = {a}')
    
    # check solution:
    print(f'Checking solution is correct: {pow(g, a, p) == h}')