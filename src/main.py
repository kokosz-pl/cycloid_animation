from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


class Function(object):
    def __init__(self, r):
        self.x = np.arange(-10, 10, 0.01)
        self.function = np.sin(self.x)
        self.r = r

    def animation_init(self):
        x0 = self.x[0:-1]
        x1 = self.x[1:]
        y0 = self.function[0:-1]
        y1 = self.function[1:]
        dx = x1 - x0
        dy = y1 - y0
        tangent_a = np.divide(dy, dx)
        tangent_b = y0 - np.multiply(tangent_a, x0)
        d = np.sqrt(np.square(dx) + np.square(dy))
        a = tangent_a[0]
        b = -1
        v0 = np.array([a, b])
        v0 = v0 / np.sqrt(np.sum(v0 ** 2))
        v0 = np.multiply(v0, self.r)

        fig, ax = plt.subplots()
        ax.set_xlim(min(self.x), max(self.x))
        ax.set_ylim(-2, 2)
        function, = ax.plot(self.x, self.function)
        circle, = ax.plot(0, 0)
        centre, = ax.plot(0, 0, marker='o')
        trajectory, = ax.plot(0, 0)
        radius, = ax.plot(0, 0)
        trajectory_x = []
        trajectory_y = []

        def animate(i):
            x = x0[i]
            y = tangent_a[i] * x0[i] + tangent_b[i]
            A = tangent_a[i]
            B = -1
            v = np.array([A, B])
            v = v / np.sqrt(np.sum(v ** 2))
            v = np.multiply(v, -self.r)
            alfa = d[i] / self.r * -1
            vx = v0[0] * np.cos(alfa) - v0[1] * np.sin(alfa)
            vy = v0[0] * np.sin(alfa) + v0[1] * np.cos(alfa)
            v0[0] = vx
            v0[1] = vy
            trajectory_x.append(x + v[0] + vx)
            trajectory_y.append(y + v[1] + vy)
            theta = np.linspace(0, 2 * np.pi, 100)
            xc = self.r * np.cos(theta) + x + v[0]
            yc = self.r * np.sin(theta) + y + v[1]
            circle.set_xdata(xc)
            circle.set_ydata(yc)
            centre.set_data(x + v[0], y + v[1])
            trajectory.set_data(trajectory_x, trajectory_y)
            radius.set_data([x + v[0], x + v[0] + vx], [y + v[1], y + v[1] + vy])

            return function, circle, centre, trajectory

        animate = FuncAnimation(fig, func=animate, frames=(len(x0)), interval=1, repeat=False)
        plt.show()


if __name__ == '__main__':
    func = Function(0.4)
    func.animation_init()
