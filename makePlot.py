#make scatterplot of data

import matplotlib.pyplot as plt
import numpy

#create figure
fig = plt.figure()

#retrieve data from results file
f = open("results")
line = f.readline()
x = []
y = []

while line:
    fields = line.split("|")
    cases = float(fields[1])
    ratio = float(fields[2])


    #each point is a zip code
    #make list of x's
    x.append(cases) #x = number of cases per 100,000

    #make list of y's
    y.append(ratio) #y = ratio of non-severe EMS calls 2020/2019

    line = f.readline()

f.close()

#make the plot
plt.scatter(x,y)

#line of best fit
x = numpy.array(x)
y = numpy.array(y)
m,b = numpy.polyfit(x,y,1)
plt.plot(x,m*x+b)

#make dotted line y=1
x = [0,6000]
y = [1,1]
plt.plot(x,y,'r--')

#label axes
plt.xlabel("COVID cases per 100,000")
plt.ylabel("Ratio of non-severe EMS calls: 2020/2019")

#save as PDF
fig.savefig("scatterplot.pdf")


