import matplotlib.pyplot as plt

def plotData(data):
    x = [p[0] for p in data]
    y = [p[1] for p in data]
    plt.plot(x, y, "-o")

data1 = [
    (1,2), (3,4), (5,2), (7,5), (9,8)
]

plotData(data1)
plt.show()
