import matplotlib.pyplot as plt

expenses = ["Salaries", "Rent", "Marketing", "R&D", "Miscellaneous"]
amounts = [500, 150, 120, 100, 50]

explodes = [0,0,0.1,0,0]
plt.pie(amounts, labels=expenses , autopct="%1.1f%%",
        wedgeprops={
            "edgecolor" : "black",
            "linewidth" : 1,
        },
        explode=explodes,
        shadow=True,
        startangle=90
        )


plt.show( )