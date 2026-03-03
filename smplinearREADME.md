---
### 📈 Simple Linear Regression from Scratch
```markdown# Simple Linear Regression from Scratch
An educational implementation of linear regression using only NumPy, without relying on scikit-learn. This project demonstrates a deep understanding of how regression algorithms work under the hood.
## What It Does
- Implements linear regression using gradient descent
- Generates synthetic data to test the algorithm
- Visualizes the fitted regression line against actual data points
- Compares results with scikit-learn's implementation

## Technologies Used
- **Python**: Core programming language
- **NumPy**: Numerical computations and matrix operations
- **matplotlib**: Visualization of regression line

## Key Skills Demonstrated
- Understanding of gradient descent optimization
- Manual implementation of machine learning algorithms
- Cost function calculation and minimization
- Parameter tuning (learning rate, iterations)

## Sample Code```
python# Gradient descent implementationfor iteration in range(n_iterations):    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)    theta -= learning_rate * gradients
