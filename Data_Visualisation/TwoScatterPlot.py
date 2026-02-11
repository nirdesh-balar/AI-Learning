import matplotlib.pyplot as plt

cities = ["City A", "City B", "City C", "City D", "City E"]

# Winter: Temperature (°C) vs Humidity (%)
winter_temp = [5, 2, 10, 0, 7]
winter_humidity = [80, 75, 65, 85, 70]

# Summer: Temperature (°C) vs Humidity (%)
summer_temp = [25, 30, 28, 35, 27]
summer_humidity = [60, 50, 55, 45, 65]

plt.scatter(winter_temp,winter_humidity,label = "Winter")
plt.scatter(summer_temp,summer_humidity,label = "Summer")
plt.title("Winter vs Summer")
plt.xlabel("Temp")
plt.ylabel("Humidity")
plt.legend()

plt.show()