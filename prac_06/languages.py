from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic Typing", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic Typing", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static Typing", False, 1991)

# Add the __str__ method to the ProgrammingLanguage class
def __str__(self):
    return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

ProgrammingLanguage.__str__ = __str__  # Adding the __str__ method to the class

# Printing the objects
print(python)
print(ruby)
print(visual_basic)

# Creating a list of ProgrammingLanguage objects
languages_list = [python, ruby, visual_basic]

# Looping through and printing dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages_list:
    if language.is_dynamic():
        print(language.name)
