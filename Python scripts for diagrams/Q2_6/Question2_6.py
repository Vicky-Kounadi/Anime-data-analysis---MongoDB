import matplotlib.pyplot as plt
import pandas as pd
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Q_2.6.csv')

data = pd.read_csv(filename, delimiter=',', header=None, skiprows=1)

df = pd.DataFrame(data)


# Number values (some sort of float parse error)
df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1])

# Number values (some sort of float parse error)
df.iloc[:, 76] = pd.to_numeric(df.iloc[:, 76])

# Number values (some sort of float parse error)
df.iloc[:, 77] = pd.to_numeric(df.iloc[:, 77])

# Number values (some sort of float parse error)
df.iloc[:, 78] = pd.to_numeric(df.iloc[:, 78])


X = list(df.iloc[:, 0])    # Col. 0 (Name)
Y1 = list(df.iloc[:, 1])   # Col. 1 (count Anime)
Y2 = list(df.iloc[:, 76])  # Col. 76 (average Episodes)
Y3 = list(df.iloc[:, 77])  # Col. 77 (avgRating)
Y4 = list(df.iloc[:, 78])  # Col. 78 (maxMinDuration)

# Width of each bar (smaller because of too much data)
bar_width = 0.2

# Avoid collisioning
X1 = range(len(X))
X2 = [x + bar_width for x in X1]
X3 = [x + 2*bar_width for x in X1]
X4 = [x + 3*bar_width for x in X1]


# Bar Chart
plt.bar(X1, Y1, color='b', width=bar_width, label='total Anime')
plt.bar(X2, Y2, color='r', width=bar_width, label='average Episodes')
plt.bar(X3, Y3, color='g', width=bar_width, label='average Rating')
plt.bar(X4, Y4, color='y', width=bar_width, label='maxMinDuration')

plt.title("total Anime, average Episodes, average Rating & Max Min Duration by Franchise")
plt.xlabel("Name")
plt.ylabel("Values")
plt.xticks([i + 1.5*bar_width for i in X1], X)
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
