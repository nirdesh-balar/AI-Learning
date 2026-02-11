import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [np.sqrt(i) for i in x ] # square roots
y2 = [i * 2 for i in x] # double
y3 = [i ** 2 for i in x] # squares
y4 = [i ** 3 for i in x] # cubes


# First subplot
plt.subplot(2, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y1)
plt.title("Plot 1 - square root")

# Second subplot
plt.subplot(2, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y2)
plt.title("Plot 2 - double")

# Third subplot
plt.subplot(2, 2, 3)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y3)
plt.title("Plot 3 - squares")

# Fourth subplot
plt.subplot(2, 2, 4)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y4)
plt.title("Plot 4 - cubes")

plt.tight_layout()
plt.show()