import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(aspect="equal"))

values = [269, 351]
labels = ["USA", "CAN"]
colors = ["blue", "indigo"]

explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

ax.set_title("Ice Hockey")
# generate the chart
plt.show()