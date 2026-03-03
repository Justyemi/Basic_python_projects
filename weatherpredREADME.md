### 🌤️ Simple Weather Prediction
```markdown# Simple Weather Prediction
A beginner-friendly machine learning project that predicts temperature using linear regression. The model learns the relationship between the day of the year and historical temperature data to make predictions.
## What It Does
- Loads and explores a synthetic weather dataset
- Trains a linear regression model on historical temperature patterns
- Predicts temperature for any given day
- Visualizes actual vs. predicted temperatures

## Technologies Used
- **Python**: Core programming language-
**pandas**: Data loading and manipulation
- **scikit-learn**: Linear regression model and evaluation
- **matplotlib**: Data visualization

## Key Skills Demonstrated
- Data loading and exploration
- Train/test split methodology
- Model training and prediction- Performance evaluation (RMSE, R²)
- Data visualization

## Sample Code```python# Train a linear regression model for temperature predictionmodel = LinearRegression()model.fit(X_train, y_train)predictions = model.predict(X_test)

---
