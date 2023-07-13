# Horizontal bar plot using CSV module

from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

plt.style.use('ggplot')

with open ('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("MOst Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("No of People who use")

plt.tight_layout()
plt.show()