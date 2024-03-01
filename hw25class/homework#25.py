
"""Homework Assignment: Introduction to Classes in Python"""

"""Instructions:
Create a Python program with two classes that model real-world objects. 
Each class should have attributes, methods, and a main program that demonstrates 
their functionality. Follow the steps below to complete the assignment."""

"""Class 1: Person"""

"""Create a class named Person with the following attributes and methods:"""

"""Attributes:"""

""" name (str) - The name of the person.
    age (int) - The age of the person.

Methods:

greeting(self) - A method that prints a greeting message using the person's name.
sleep(self) - A method that prints a message indicating that the person is going to sleep."""

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __str__(self) -> str:
#         return f"{self.name}"
        
#     def greeting():
#         return f"Hello"
    
#     def sleep():
#         return "went to sleep"
    
# human_1 = Person("Mark", 21 )
# human_2 = Person("Terry", 25 )

# greet = Person.greeting()
# sleeping = Person.sleep()

# print(greet, human_1)
# print( human_2, sleeping)
    


"""Class 2: Animal

Create a class named Animal with the following attributes and methods:

Attributes:

name (str) - The name of the animal.
age (int) - The age of the animal.
color (str) - The color of the animal
Methods:

eat(self) - A method that prints a message indicating that the animal is going to eat.
run(self) - A method that prints a message indicating that the animal is running."""

# class Animal:
#     def __init__(self, name, age, color) -> None:
#         self.name = name 
#         self.age  = age       
#         self.color = color
        
#     def __str__(self) -> str:
#         return f"{self.name}"
    
#     def eat():
#         return "went to eat"
    
#     def run():
#         return "runs on the lawn"
    
#     def swim():
#         return "swims in the lake"
        
# animal_1 = Animal("horse", 3, "black")              
# animal_2 = Animal("dog", 3, "brown")              
# animal_3 = Animal("crocodile", 7, "green")   
     
# eating = Animal.eat()
# running = Animal.run()
# swims = Animal.swim()


# print(animal_1.color, animal_1.name, running)
# print(animal_2.color, animal_2.name, eating)
# print(animal_3.color, animal_3.name, swims)




# Main Program:

# Write a main program that demonstrates the use of the Person and Animal classes. 
# Create instances of both classes and use their methods to show their behavior. 
# For example, create a person and an animal, set their attributes, and call 
# their appropriate methods for each of them.

# Ensure that your program is well-documented and follows best practices for Python 
# code formatting and style.


class Person:
    def __init__(self, name, age, speaks, reading, smart) -> None:
        self.name = name
        self.age = age
        self.speaks = speaks
        self.reading = reading
        self.smart = smart


        
person = Person("Mark", 19, "speaks english", "is reading a book", "is intelligent" )        
print(person.reading)        
        
class Animal:
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color
        
animal = Animal("bear", 3, "brown")
print(animal.color)

        




# Quiz.
# 1. What is a class in Python?
#     a) A class is a built-in function.
#     b) A class is an instance of an object.
"""    c) A class is a blueprint for creating objects."""
#     d) A class is a reserved keyword in Python.

# 2. In Python, which keyword is used to define a class?
"""    a) class"""
#     b) define
#     c) struct
#     d) object

# 3. How do you create an instance of a class in Python?
#     a) By using the new keyword.
#     b) By calling the class as a function.
#     c) By using the instance keyword.
"""    d) By using the class name followed by parentheses."""
    
# 4. Which of the following statements is true regarding attributes in a class?
#     a) Attributes are methods defined within a class.
#     b) Attributes are used to create instances of a class.
"""    c) Attributes are variables that store data in a class."""
#     d) Attributes are not allowed in Python classes.

# 5. Which keyword is used to access the attributes and methods of a class instance?
#     a) access
#     b) use
#     c) this
"""    d) dot (.)"""
    
# 6. How do you create an instance of a class in Python?
#     a) By using the new keyword.
"""    b) By calling the class as a function."""
    
# 7. Which of the following statements is true regarding attributes in a class?
"""    a) Attributes are methods defined within a class."""
#     b) Attributes are variables that store data in a class.
    
# 8. What is an "object" in the context of classes?
"""    a) An instance of a class."""
#     b) A Python module.
#     c) A function

# 9. What is the relationship between a class and an object in Python?
"""    a) A class is an instance of an object."""
#     b) An object is an instance of a class.
    
# 10. What are "attributes" in a class?
#     a) Functions defined within a class.
"""    b) Variables that store data within a class."""
    
# 11. In Python, how do you define a class?
"""    a) By using the class keyword followed by the class name and a colon."""
#     b) By using the def keyword followed by the class name and a colon.
