class Greet:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

g = Greet()
g.greet()            # Output: Hello!
g.greet("Sarbuland") # Output: Hello, Sarbuland!
