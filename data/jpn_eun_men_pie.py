import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))

values = [50, 33]
labels = ["JPN", "EUN"]
colors = ["yellowgreen", "teal"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

ax.set_title("Men")
# generate the chart
plt.show()