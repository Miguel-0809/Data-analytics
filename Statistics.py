import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("Mean: ",round(numpy.mean(speed),2))
print("Median: ",numpy.median(speed))
print("Mode: ",stats.mode(speed))

#* σ => Standard deviation is a number that describes how spread out the values are
print("Standard Deviation: ",round(numpy.std(speed),2))
#* σ^2 => Variance = std*std
print("Variance: ", round(numpy.var(speed),2))

#* Percentiles
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print("Percentile: ",numpy.percentile(ages,75)) 
#? What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.






