import autograd.numpy as np
from autograd import grad
import matplotlib.pyplot as plt
import random
import pandas as pd

class LinearRegression():
    def __init__(self, K=1000, alpha=10**-3):
        self.K = K
        self.alpha = alpha

    def load_data(self, csvfile):
        data = np.asarray(pd.read_csv(csvfile, delimiter = ',', header = None))
        self.data = data
        self.x = data[:, :-1]
        self.y = data[:, -1]
        self.y.shape = (len(self.y), 1)
        
    def compute_cost_val(self, w):
        P = len(self.y)
        cost = 0
    
        # run over all data points and weights and compute total error
        for p in range(P):
            # get pth point
            x_p = self.x[p]
            y_p = self.y[p]
        
            # linear combo
            temp = w[0] + sum([v*e for v, e in zip(x_p, w[1:])])
                        
            # add error to cost
            cost += (temp - y_p)**2
        return cost

    # gradient descent loop
    def fit(self):
        # initial point
        dim = self.data.shape[1]
        w = np.array([random.uniform(-2, 2) for i in range(dim)])
        
        # compute gradient of cost function for use in loop
        gradient = grad(self.compute_cost_val)

        # create container to record weights
        self.whist = []
        self.ghist = []

        # descent loop
        self.w_best = w
        g_best = np.inf
        for k in range(self.K):
            # record current weight and cost
            self.whist.append(w)
            g = self.compute_cost_val(w)
            self.ghist.append(g)
            if g < g_best:
                self.w_best = w
                g_best = g
        
            # take descent step
            w = w - self.alpha * gradient(w)
        
    # a short function to perform predictions
    def predict(self, x_input):
        ind = np.argmin()
        output = self.w_best[0] + np.dot(self.w_best[1:], x_input)
        return output[0]


def main():
    # get instance of linear regression class
    test = LinearRegression(K=100, alpha=10**-2)

    # data input
    csvname = '2d_linregress_data.csv'
    test.load_data(csvname)

    # run grad descent
    test.fit()

    # print history
    plt.plot(test.ghist)
    plt.show()

    plt.scatter(test.x,test.y)
    s = np.linspace(0,1)
    w = test.w_best
    t = []

    for i in range(len(s)):
        temp = w[0] + w[1]*s[i]
        t.append(temp)

    plt.plot(s,t,c = 'r',linewidth = 2)
    plt.show()


if __name__ == "__main__":
    main()
