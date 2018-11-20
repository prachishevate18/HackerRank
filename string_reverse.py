def reverse_str(inp_str):
    if len(inp_str) == 0:
        return inp_str
    else:
        return reverse_str(inp_str[1:]) + inp_str[0]  #recursive call to reverse function

str_var = str(input("Enter the string to be reversed: "))
print(reverse_str(str_var))