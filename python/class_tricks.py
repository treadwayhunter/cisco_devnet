class MyClass:

    count = 0 # beware of this

    def __init__(self):
        self.count += 1 # this is a tricky one


myclass = MyClass()
print(myclass.count)

# ✅ You correctly identified that the += hides the class variable behind an instance variable. Great intuition.

# The above is per ChatGPT. I did not actually identify this.
# If count = 0 is commented out, self.count += 1 will not instantiate a new instance variable.
# However, if the class variable is available, self.count += 1 will instantiate a new instance variable.
