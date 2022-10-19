# importing package
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
y1 = np.array([173, 153, 195, 147, 120, 144, 148, 109, 174, 130, 172, 131])
y2 = np.array([189, 189, 105, 112, 173, 109, 151, 197, 174, 145, 177, 161])
y3 = np.array([185, 185, 126, 134, 196, 153, 112, 133, 200, 145, 167, 110])
# plot lines
plt.plot(x, y1, label="Affordable segment", linestyle="-",color = 'red')
plt.plot(x, y2, label="Luxury Segment", linestyle="-",color = 'yellow')
plt.plot(x, y3, label="Super luxury segment", linestyle="-",color = 'blue')


plt.title(label="Sales Data ",
          loc="center")

plt.ylabel("Sales of Segments")
plt.xlabel("Months of Year with font size 18")


plt.legend()
plt.show()