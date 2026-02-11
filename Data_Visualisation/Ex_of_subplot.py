import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

cities = ["New York", "London", "Delhi", "Tokyo"]

temperatures = [
    [22, 23, 21, 24, 25],   # New York
    [18, 19, 17, 20, 21],   # London
    [30, 32, 31, 33, 34],   # Delhi
    [25, 26, 24, 27, 28]    # Tokyo
]

fig, axes = plt.subplots(2, 2)
count=0
for i in range(2):
    for j in range(2):
        axes[i][j].plot(days, temperatures[count], marker='o')
        axes[i][j].set_title(cities[count])
        axes[i][j].grid(True)
        count = count + 1


fig.suptitle("Weekly Temperature by City")
fig.supylabel("Temperature (°C)")
fig.supxlabel("Day")

fig.tight_layout()

plt.show()