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


plt.bar(oscar_years,oscar_revenue,color = "purple")
plt.title("Revenue in each year for oscar movies")
plt.xlabel("Year")
plt.ylabel("Revenue")

# for notation on top of the bar
for i in range(len(oscar_years)):
 plt.text(oscar_years[i],oscar_revenue[i] + 5 ,oscar_revenue[i],ha = "center")

plt.show( )