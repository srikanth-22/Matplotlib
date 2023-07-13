# Horizontal Bar plots using pandas

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity, height = 0.25)

plt.title("MOst Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("No of People who use")

plt.tight_layout()
plt.show()