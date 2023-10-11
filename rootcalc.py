def convert_to_standard(a, b, c):
    return "Standard form: {}x² + {}x + {}".format(a, b, c)

def convert_to_vertex(a, b, c):
    h = -b / (2*a)
    k = c - (b**2 / (4*a))
    return "Vertex form: {}(x - {})^2 + {}".format(a, h, k)

def convert_to_root(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        r = (-b + d**0.5) / (2*a)
        s = (-b - d**0.5) / (2*a)
        return "Root form: {}(x - {})(x - {})".format(a, r, s)
    else:
        return "The equation has complex roots and cannot be converted to root form."

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        return "The roots are real and different: {} and {}".format(root1, root2)
    elif d == 0:
        root = -b / (2*a)
        return "The roots are real and same: {}".format(root)
    else:
        real_part = -b / (2*a)
        imag_part = (-d)**0.5 / (2*a)
        return "The roots are complex: {} + {}i and {} - {}i".format(real_part, imag_part, real_part, imag_part)

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    form = input("Enter the form of your equation; 'standard', 'vertex', or 'root':  ")
    if form.lower() == "standard":
        a = get_float_input("Enter the variable a for ax²: ")
        b = get_float_input("Enter the variable b for bx: ")
        c = get_float_input("Enter enter the variable c for c: ")
    elif form.lower() == "vertex":
        a = get_float_input("Enter the variable a for a(x-h)²+k: ")
        h = get_float_input("Enter the variable h for (x-h)²: ")
        k = get_float_input("Enter the variable k for k: ")
        b = -2*a*h
        c = a*h**2 + k
    elif form.lower() == "root":
        a = get_float_input("Enter a for a(x-r)(x-s): ")
        r = get_float_input("Enter r for a(x-r)(x-s): ")
        s = get_float_input("Enter s for a(x-r)(x-s): ")
        b = -(r + s)*a 
        c = r*s*a 
    else:
        print("Invalid form! Please enter either 'standard', 'vertex', or 'root'.")
        continue

    result = solve_quadratic(a, b, c)
    print(result)

    while True:
        convert = input("Do you wish to convert your equation to a different form (Y/N)? ")
        if convert.lower() == 'n':
            break
        elif convert.lower() == 'y':
            new_form = input("Which form do you want to convert to? 'standard', 'vertex', or 'root'? ")
            if new_form.lower() == 'standard':
                print(convert_to_standard(a, b, c))
            elif new_form.lower() == 'vertex':
                print(convert_to_vertex(a, b, c))
            elif new_form.lower() == 'root':
                print(convert_to_root(a, b, c))
            else:
                print("Invalid form! Please enter either 'standard', 'vertex', or 'root'.")
        else:
            print("Invalid input! Please enter either 'Y' or 'N'.")
