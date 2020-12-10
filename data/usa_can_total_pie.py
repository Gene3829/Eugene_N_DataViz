import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))

values = [653, 625]
labels = ["USA", "CAN"]
colors = ["red", "orange"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

ax.set_title("Total")
# generate the chart
plt.show()

# import matplotlib.pyplot as plt

# fig = plt.figure()

# ax = fig.add_axes([0,0,1,1])

# countries = ['USA', 'CAN']
# totalmedals = [653, 625]

# ax.bar(countries,totalmedals)

# plt.show()