import matplotlib.pyplot as plt

people = ["Person A", "Person B", "Person C", "Person D", "Person E", 
          "Person F", "Person G", "Person H", "Person I", "Person J"]
age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]
blood_pressure = [110, 115, 120, 122, 125, 130, 135, 123, 145, 150]

colors = ["green" if x<135 else "red" for x in blood_pressure]
plt.scatter(age,blood_pressure , s=blood_pressure , cmap="OrRd" , c=blood_pressure)  # s = size of dots , alpha = Transparecy of dots , cmap = colormap we can find code online , c=which coloum should you represent
plt.title("Age vs Bp")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.grid()
plt.colorbar(label = "Bp")

for i in range(len(people)):
    plt.annotate(people[i],xy=(age[i],blood_pressure[i]),xytext=(age[i]+1,blood_pressure[i]-1))

plt.xlim(min(age),max(age)+10)
plt.ylim(min(blood_pressure)-5,max(blood_pressure)+5)

plt.show( )
