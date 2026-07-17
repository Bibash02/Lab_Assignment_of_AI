import numpy as np

# Input data (XOR)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights
np.random.seed(42)

input_neurons = 2
hidden_neurons = 2
output_neurons = 1

weights_input_hidden = np.random.rand(input_neurons, hidden_neurons)
weights_output_hidden = np.random.rand(hidden_neurons, output_neurons)

learning_rate = 0.5

# Training
for epoch in range(10000):

    # Forward propagation
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_output_hidden)
    predicted_output = sigmoid(final_input)

    # Error
    error = y - predicted_output

    # Backpropagation
    d_output = error * sigmoid_derivative(predicted_output)

    hidden_error = np.dot(d_output, weights_output_hidden.T)
    d_hidden = hidden_error * sigmoid_derivative(hidden_output)

    # Update weights
    weights_output_hidden += hidden_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate

print("Predicted Output:")
print(predicted_output.round(3))