import numpy as np
import matplotlib.pyplot as plt



class RandomWalk:
    def __init__(self, val = 15, steps  = 100):
        self.steps = steps
        self.val = val
        y = np.zeros(shape=steps)
        y[0] = val
        for i in range(1, steps):
            y[i] = y[i-1] + np.random.randn()
        self.y = y

    def plot(self):
        plt.plot(self.y)
        plt.grid()
        plt.ylabel("y")
        plt.xlabel("steps")
        plt.ylim((min(self.y) - 5, max(self.y)+5))
        plt.xlim((0, self.steps))
        plt.title("Random Walk")
        plt.show()

        

if __name__ == "__main__":
    demo = RandomWalk()
    demo.plot()
