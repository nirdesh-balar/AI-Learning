import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
direct = [50, 60, 70, 80, 90, 100, 110]
organic = [30, 40, 50, 55, 60, 70, 80]
social = [20, 25, 30, 35, 40, 50, 60]

plt.stackplot(days, direct, organic, social, labels=['Direct', 'Organic', 'Social'])
plt.legend(loc='upper left')
plt.title("Website Traffic Over a Week")
plt.xlabel("Days")
plt.ylabel("Number of Visitors")

plt.show( )