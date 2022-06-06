import matplotlib.pyplot as plt
import numpy

#? HISTOGRAM

#* array containing 250 random floats between 0 and 5
a = numpy.random.uniform(0.0, 6.0, 250)


#* NORMAL DATA DISTRIBUTION
b=numpy.random.normal(5.0,1.0,1000)

#plt.hist(b, 100)
#plt.show()

#? SCATTER PLOT
#x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

#y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

#plt.scatter(x, y)
#plt.show()


