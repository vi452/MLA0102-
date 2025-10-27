import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
inputs = [[0,0],[0,1],[1,0],[1,1]]
weights_input_hidden = [[0.2, 0.4],
                        [0.3, 0.7]]
weights_hidden_output = [0.6, 0.9]
bias_hidden = [0.5, 0.5]
bias_output = 0.2
for x in inputs;
    h1 = sigmoid(x[0]*weights_input_hidden[0][0] + x[1]*weights_input_hidden[1][0] + bias_hidden[0])
    h2 = sigmoid(x[0]*weights_input_hidden[0][1] + x[1]*weights_input_hidden[1][1] + bias_hidden[1])
    output = sigmoid(h1*weights_hidden_output[0] + h2*weights_hidden_output[1] + bias_output)

    print(f"Input: {x} → Output: {round(output, 3)}")


output:
Input: [0, 0] → Output: 0.757
Input: [0, 1] → Output: 0.787
Input: [1, 0] → Output: 0.776
Input: [1, 1] → Output: 0.8
