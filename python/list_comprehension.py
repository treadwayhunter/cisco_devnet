x = [1, 2, 3]
y = [i**2 for i in x if i % 2 == 0]
print(x)
print(y)


# i is only scoped within the list comprehension
# in older python versions, i was available outside of the list scope
