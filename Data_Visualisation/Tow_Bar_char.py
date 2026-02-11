import matplotlib.pyplot as plt
import numpy as np

oscar_movies = [
    "The Dark Knight", 
    "The Hurt Locker",  
    "The King's Speech", 
    "The Artist",     
    "Argo"
]
oscar_years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]


non_oscar_movies = ["Slumdog Millionaire","Avatar","Inception","Hugo","Lincoln"]
non_oscar_years = [2008, 2009, 2010, 2011, 2012]
non_oscar_revenue = [378, 2788, 829, 185, 275]

x = np.arange(len(oscar_years))
width = 0.4 

plt.bar(x - width/2,oscar_revenue,width , label = "Oscar") # limit extend right side 

plt.bar(x + width/2,non_oscar_revenue,width , label = "Non oscar")  # limit extend left side

plt.title("Compair Oscar movies revenue vs Non Oscar movies revenue")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.legend()

plt.xticks(x, oscar_years) # to show x-axis labels

plt.show()

