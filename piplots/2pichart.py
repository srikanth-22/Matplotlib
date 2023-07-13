from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]


plt.pie(slices, labels= labels,explode=explode,shadow=True,
        pctdistance= 1.25, labeldistance= 0.4,startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
