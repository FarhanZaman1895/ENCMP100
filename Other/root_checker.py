import numpy as np

# Inputted Numbers
a = float(input("coeff a: "))
b = float(input("coeff b: "))
c = float(input("coeff c: "))

# Calculate Discriminant
D = b**2 - 4 * a * c

# Check for errors
if D < 0:
    print("No real roots")
elif D == 0:
    root = -c/b
    print("There is a single root, %.4f" % root)
elif D > 0:
    root = [-b+np.sqrt(D)/(2*a),
        -b-np.sqrt(D)/(2*a)]

    print("There are two roots, %.4f and %.4f" % (root[0], root[1]))
