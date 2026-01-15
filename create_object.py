Q)   In the previous chapter, a series of exercises asked you to write a `Date` class and several functions that work with `Date` objects.
Now let's practice rewriting those functions as methods.

1. Write a definition for a `Date` class that represents a date -- that is, a year, month, and day of the month.

2. Write an `__init__` method that takes `year`, `month`, and `day` as parameters and assigns the parameters to attributes. Create an object that represents June 22, 1933.

2. Write `__str__` method that uses a format string to format the attributes and returns the result. If you test it with the `Date` you created, the result should be `1933-06-22`.

3. Write a method called `is_after` that takes two `Date` objects and returns `True` if the first comes after the second. Create a second object that represents September 17, 1933, and check whether it comes after the first object.

Solution :


# Solution goes here
class Date():
    

    def __str__(self, year=0,month=0,day=0):
        d = (f'{self.year}-{self.month:02d}-{self.day:02d}')
        return d

    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    

    def to_tuple(self):
        return (self.year,self.month,self.day)

    def is_after(self, other):
        return self.to_tuple() > other.to_tuple()


birthday1 = Date(1933, 6, 22)
print(birthday1) #should be False

birthday2.is_after(birthday1)  # should be True
