import matplotlib.pyplot as plt


legit_transactions = [
    2.99, 5.49, 8.99, 12.50, 14.99, 19.99, 23.45, 29.99, 34.99, 39.50,
    45.00, 49.99, 55.25, 60.00, 75.99, 89.99, 120.50, 150.00, 199.99,
    249.99, 300.75, 450.00, 600.00, 850.00, 1200.00
]

fraud_transactions = [
    50, 100, 150, 200, 300, 500, 500, 750, 1000, 1000,
    1200, 1500, 1500, 2000, 2500, 3000, 3000
]

plt.hist(fraud_transactions, bins=10, label='Fraud', color='red', alpha=0.5, edgecolor="black")
plt.hist(legit_transactions, bins=10, label='Legit', color='green', alpha=0.5, edgecolor="black")

plt.xlabel('Transaction Amount ($)')
plt.ylabel('Frequency')
plt.title('Transaction Amount Distribution: Legitimate vs Fraudulent')
plt.legend()
plt.grid(True)


plt.show()