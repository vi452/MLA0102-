
data = [
    [25, 40000, 0],
    [35, 60000, 1],
    [45, 80000, 1],
    [20, 20000, 0],
    [30, 50000, 1]
]
def predict(age, income):
    if age < 27:
        return 0   # Too young → No
    elif income > 55000:
        return 1   # High income → Yes
    else:
        return 1 if age > 28 else 
age = 40
income = 70000
result = predict(age, income)

print("Predicted Output for [Age=40, Income=70000]:", "Yes" if result == 1 else "No")


