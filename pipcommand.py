#using numpy for statistical opertion
import numpy
from scipy import stats
pricelist=[56,89,23,35,35,60,62,60,60,72,60,210,124]
pricelist.sort()
print("original price value are")
print(pricelist)
meanprice=numpy.mean(pricelist)
print("mean price =%.2f"%(meanprice))

medianprice=numpy.median(pricelist)
print("median price =%.2f" %(medianprice))
stdprice1=numpy.std(pricelist)
print("standard deviation of price %.2f" %(stdprice1))

x=stats.mode(pricelist)
print("mode =",x)
