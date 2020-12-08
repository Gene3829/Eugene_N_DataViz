import matplotlib.pyplot as plt

values = [386, 239]
labels = ["Men", "Women"]
colors = ["green", "gold"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)
# generate the chart
plt.show()