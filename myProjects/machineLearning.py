"""What is Standard Deviation?
Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range."""

#Use the NumPy std() method to find the standard deviation
import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)

"""Variance
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

Or the other way around, if you multiply the standard deviation by itself, you get the variance!

To calculate the variance you have to do as follows"""

#Use the NumPy var() method to find the variance
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)

"""What are Percentiles?
Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

Example: Let's say we have an array of the ages of all the people that lives in a street.

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.

The NumPy module has a method for finding the specified percentile:"""

#Example
#Use the NumPy percentile() method to find the percentiles:

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)