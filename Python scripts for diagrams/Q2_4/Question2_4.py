import matplotlib.pyplot as plt
import pandas as pd
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Question2_4.csv')

data = pd.read_csv(filename, delimiter=',', header=None, skiprows=1)

df = pd.DataFrame(data)


# Studio ID (String)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Number values (some sort of float parse error)
df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1])

# Number values (some sort of float parse error)
df.iloc[:, 2] = pd.to_numeric(df.iloc[:, 2])

X = list(df.iloc[:, 0])   # Col. 0 (Studio)
Y1 = list(df.iloc[:, 1])  # Col. 1 (Episodes)
Y2 = list(df.iloc[:, 2])  # Col. 2 (Ratings)

# Avoid collision (0.4 is bar width)
X1 = range(len(X))
X2 = [x + 0.4 for x in X1]


# Bar Chart
plt.bar(X1, Y1, color='b', width=0.4, label='Avg. Episodes')
plt.bar(X2, Y2, color='r', width=0.4, label='Avg. Ratings')

plt.title("Average Episodes and Ratings by Studio")
plt.xlabel("Studio Name")
plt.ylabel("Values")
plt.xticks([i + 0.4 / 2 for i in X1], X)
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.show()
