"""
Classes - Object-Oriented Programming

Concepts:
    - Class definition and instantiation
    - Constructor (__init__) and instance attributes
    - Instance methods and self
    - Class variables vs instance variables
    - Inheritance and super()
    - Special methods (dunder methods)
    - Properties (@property)
    - Class methods and static methods
    - Multiple inheritance and MRO
"""


class Dog:
    """Simple Dog class"""

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age}"


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog1: {dog1.describe()}")
print(f"Dog2: {dog2.bark()}")


# Class varibales
class Cat:
    species = "Felis catus"
    total_cats = 0

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        Cat.total_cats += 1

    def info(self):
        return f"{self.name} is a {self.color} {Cat.species}"

    @classmethod
    def get_total_cats(cls):
        return cls.total_cats


cat1 = Cat("Whiskers", "orange")
cat2 = Cat("Shadow", "black")

print(f"Cat1: {cat1.info()}")
print(f"Cat2: {cat2.info()}")
print(f"Total cats: {Cat.get_total_cats()}")
print(f"Species: {Cat.species}")

Cat.species = "Domestic Cat"
print(f"Updated species: {cat1.species}")  # Affects all instances


# Inheritance
class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} is moving"


class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self.can_fly = can_fly

    def make_sound(self):
        return "Tweet tweet!"

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying"
        return f"{self.name} cannot fly"


# Using inheritance
eagle = Bird("Eagle", "Aquila", True)
penguin = Bird("Penguin", "Spheniscidae", False)

print(f"{eagle.name}: {eagle.make_sound()}")
print(f"{eagle.fly()}")
print(f"{penguin.name}: {penguin.fly()}")
print(f"{penguin.move()}")  # Inherited from parent


# Special methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """String representation for users"""
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """String representation for developers"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __len__(self):
        """Length of the book"""
        return self.pages

    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        """Less than comparison (for sorting)"""
        return self.pages < other.pages

    def __add__(self, other):
        """Addition operation"""
        if isinstance(other, Book):
            return f"Combined pages: {self.pages + other.pages}"
        return NotImplemented


# Using special methods
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Fluent Python", "Luciano Ramalho", 792)
book3 = Book("Python Crash Course", "Eric Matthes", 544)

print(f"str(book1): {str(book1)}")
print(f"repr(book1): {repr(book1)}")
print(f"len(book1): {len(book1)}")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 + book2: {book1 + book2}")


# Properties
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property for fahrenheit"""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set celsius from fahrenheit"""
        self._celsius = (value - 32) * 5 / 9


# Using properties
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"After setting Fahrenheit to 86:")
print(f"Celsius: {temp.celsius}°C")

# Validation
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")


# Class method and static method
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor from string"""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Alternative constructor for today's date"""
        import datetime

        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

    @staticmethod
    def is_valid_date(year, month, day):
        """Static method for validation"""
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True


# Using class methods
date1 = Date(2024, 1, 15)
date2 = Date.from_string("2024-03-20")
date3 = Date.today()

print(f"date1: {date1}")
print(f"date2 (from string): {date2}")
print(f"date3 (today): {date3}")

# Using static method
print(f"Is 2024-02-30 valid? {Date.is_valid_date(2024, 2, 30)}")
print(f"Is 2024-03-15 valid? {Date.is_valid_date(2024, 3, 15)}")


# Multiple inheritance
class Flyable:
    def fly(self):
        return "Flying in the sky"


class Swimmable:
    def swim(self):
        return "Swimming in the water"


class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")

    def make_sound(self):
        return "Quack quack!"


# Using multiple inheritance
duck = Duck("Donald")
print(f"{duck.name} can:")
print(f"  - {duck.fly()}")
print(f"  - {duck.swim()}")
print(f"  - Say: {duck.make_sound()}")
print(f"  - {duck.move()}")

# Method Resolution Order (MRO)
print(f"Duck MRO: {Duck.__mro__}")
