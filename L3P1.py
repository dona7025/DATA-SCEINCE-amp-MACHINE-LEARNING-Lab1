import matplotlib.pyplot as plt

# initializing the data
x = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
y = [24000, 22500, 19700, 17500, 14500, 10000, 5800 ]


plt.plot(x, y, color = 'red',
         linestyle = '--', marker = '*',
         markerfacecolor = 'green', markersize = 20)


plt.title("Value Depreciation ")

plt.ylabel("Year")
plt.xlabel("Car Value")
plt.show()