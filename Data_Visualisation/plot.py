import matplotlib.pyplot as plt

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

plt.plot(oscar_years,oscar_revenue,"o--r" , label = "Oscar Winners")   #  "o--r" mean fmt = [marker][format][color]

plt.plot(oscar_years,non_oscar_revenue,color = "green" , marker = "<",linestyle = "-.",linewidth = 5,label = "Non-Oscar Winners")

plt.title("Sample")

plt.xlabel("Note")

plt.ylabel("All Revenu")

plt.legend(loc = "upper right")

plt.grid() # Background line

plt.tight_layout() 



plt.show()