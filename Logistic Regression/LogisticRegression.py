import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# set random state for reproducibility
np.random.seed(12)


class LogisticRegression:
	def __init__(self):
		self.weights = None
		self.bias = 0
		self.lmbda = 0.0001
	
	def _sigmoid(self, x):
		return 1/(1+np.exp(-x))

	def train(self, X=None, y=None, lr=1e-3, iters=100, init_intercept=0):
		loss = []
		m = X.shape[0]
		n = X.shape[1]
		y = y.reshape(-1, 1)
		self.weights = np.zeros((n, 1))
		self.bias = init_intercept
		true = y
		for i in range(iters):
			predicted = np.dot(X, self.weights) + self.bias
			predicted = self._sigmoid(predicted)
			dw = np.dot(X.T, true - predicted) + self.lmbda*np.sum(self.weights)**2
			db = np.sum(dw)
			self.weights += (lr / m) * dw
			self.bias += (lr / m) * db
			error = np.sum((true - predicted)**2/m)
			loss.append(error)
		return loss
	
	def predict(self, X):
		res = []
		m = X.shape[0]
		z = np.dot(X,self.weights) + self.bias
		h = self._sigmoid(z)
		res = np.round(h)
		return res
	
	def evaluate(self, X, y):
		m = X.shape[0]
		y_pred = self.predict(X)
		acc = sum(y_pred)/len(y_pred)
		return acc[0]

	def get_test_data(self, num_observations=5000):
		x1 = np.random.multivariate_normal([0, 1], [[1, .75],[.75, 1]],
			num_observations)
		x2 = np.random.multivariate_normal([3, 4], [[1, .75],[.75, 1]],
			num_observations)

		X = np.vstack((x1, x2)).astype(np.float32)
		y = np.hstack((np.zeros(num_observations), np.ones(num_observations)))

		return X, y

if __name__ == "__main__":
	lr = LogisticRegression()
	X, y = lr.get_test_data()

	print("Running on test data from multivariate normal distributions")

	losses = lr.train(X=X,y=y,lr=0.0001,iters=100)
	loss_plot = sns.lineplot(x=range(len(losses)), y=losses)

	print("You can also use evaluate() to test results.")

	plt.title("Loss vs Iterations")
	plt.xlabel("Epoch")
	plt.ylabel("Loss")
	plt.show()