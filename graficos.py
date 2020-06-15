import matplotlib.pyplot

import numpy

def seno(x):
    
    return numpy.sin(x)


x = numpy.linspace(0,10,100)


matplotlib.pyplot.plot(x,seno(x))
matplotlib.pyplot.show()
