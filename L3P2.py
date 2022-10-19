
import matplotlib.pyplot as plt


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

x1 = ['Mon', 'Tues', 'Wed',
      'Thurs', 'Fri']
y1 = [300, 450, 150, 400, 650]
y2 = [400, 500, 350, 300, 500]



fig.suptitle('Daily Sales', fontsize=20)

plt.subplot(1, 2, 1)
plt.title(label="Sales Data1 ",
          loc="right")

plt.subplot(1, 2, 2)
plt.title(label="Sales Data2 ",
          loc="center")


l1 = ax1.plot(x1, y1, color = 'cyan',
         linestyle = '-.', marker = 'h',
         markerfacecolor = 'magenta', mec='k',markersize = 10)

l2 = ax2.plot(x1, y2, color = 'yellow',
         linestyle = '--', marker = 'D',
         markerfacecolor = 'green', mec='r', markersize = 10)

ax1.set_ylabel('Days of week', fontsize=25)
ax2.set_ylabel('Days of week', fontsize=25)

ax1.set_xlabel('Sale of Drinks', fontsize=25)
ax2.set_xlabel('Sale of Food', fontsize=25)


plt.subplots_adjust(right=0.9)

plt.show()