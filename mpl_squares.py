import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.plot(squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick label.
plt.tick_params(axis='both', labelsize=14)

plt.show()
