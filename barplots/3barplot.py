# horizontal multiple bar plot

from matplotlib import pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight")

ages_y = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y_indexes = np.arange(len(ages_y))

height = 0.25

dev_x = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.barh(y_indexes-height, dev_x,height = height, color="#444444", label="All Devs")

py_dev_x = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.barh(y_indexes, py_dev_x,height = height, color="#008fd5", label="Python")

js_dev_x = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.barh(y_indexes + height, js_dev_x,height = height, color="#e5ae38", label="JavaScript")

plt.legend()
plt.yticks(ticks=y_indexes, labels=ages_y)

plt.title("Median Salary ($USD) by Age")
plt.ylabel("Ages")
plt.xlabel("Median Salary ($USD)")

plt.tight_layout()
plt.show()