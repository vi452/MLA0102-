import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Manual data for XOR problem
inputs = [[0,0],[0,1],[1,0],[1,1]]
weights_input_hidden = [[0.2, 0.4],
                        [0.3, 0.7]]
weights_hidden_output = [0.6, 0.9]
bias_hidden = [0.5, 0.5]
bias_output = 0.2

for x in inputs:
    # Hidden layer
    h1 = sigmoid(x[0]*weights_input_hidden[0][0] + x[1]*weights_input_hidden[1][0] + bias_hidden[0])
    h2 = sigmoid(x[0]*weights_input_hidden[0][1] + x[1]*weights_input_hidden[1][1] + bias_hidden[1])

    # Output layer
    output = sigmoid(h1*weights_hidden_output[0] + h2*weights_hidden_output[1] + bias_output)

    print(f"Input: {x} → Output: {round(output, 3)}")
