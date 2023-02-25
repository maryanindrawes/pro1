import matplotlib.pyplot as plt

X1 = [1, 2, 3, 4, 5, 6]
Y1 = [2, 4, 5, 9, 7, 2]
X2 = [8, 9, 5, 7]
Y2 = [7, 6, 3, 2]
plt.plot(X1, Y1, linestyle="dashdot")
plt.plot(X2, Y2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Title", fontsize=20, color="red")
plt.show()


