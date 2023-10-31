class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"


# Example Usage:

# Creating instances of ProgrammingLanguage
java = ProgrammingLanguage("Java", "Static", "Yes", 1995)
cpp = ProgrammingLanguage("C++", "Static", "No", 1983)
python = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", "No", 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", "Yes", 1995)

# Testing the is_dynamic method
print(f"Is {java.name} dynamically typed? {java.is_dynamic()}")
print(f"Is {cpp.name} dynamically typed? {cpp.is_dynamic()}")
print(f"Is {python.name} dynamically typed? {python.is_dynamic()}")
print(f"Is {vb.name} dynamically typed? {vb.is_dynamic()}")
print(f"Is {ruby.name} dynamically typed? {ruby.is_dynamic()}")
