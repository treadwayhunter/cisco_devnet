def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))
print(append_to_list(2))

# Default arguments in Python are evaluated once at definition time
# they are not evaluated each time the function is called
# 
# You can almost think of them as 'static', it is now global
# there is one instance of my_list
