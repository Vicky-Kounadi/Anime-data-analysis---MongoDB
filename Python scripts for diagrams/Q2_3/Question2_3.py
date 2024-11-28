import matplotlib.pyplot as plt
import pandas as pd
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'Question2_3.csv')

data = pd.read_csv(filename, delimiter=',', header=None)

df = pd.DataFrame(data) 

df = df.astype(str)


X = list(df.iloc[1:, 0])
Y = list(df.iloc[1:, 1])
X = [int(x) for x in X]


# Bar Chart
plt.bar(Y, X, color='g') 
plt.title("Anime Count by Tags") 
plt.xlabel("Tags") 
plt.ylabel("Anime Count") 
plt.xticks(rotation=45, ha='right')

plt.show() 