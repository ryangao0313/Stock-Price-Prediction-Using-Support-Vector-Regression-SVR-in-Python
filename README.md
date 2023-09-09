
# Stock Price Prediction with Support Vector Regression

This Python script is designed to predict stock prices using Support Vector Regression (SVR) models. It reads historical stock price data from a CSV file, trains three different SVR models (linear, polynomial, and radial basis function), and provides predictions for a specified date.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- `numpy`
- `scikit-learn` (for SVR)
- `matplotlib`

You can install these libraries using pip:

```
pip install numpy scikit-learn matplotlib
```

## Usage

1. Clone this repository to your local machine.

2. Prepare your historical stock price data in a CSV file. The file should have two columns: "Date" and "Price." Make sure the CSV file is located in the same directory as the script.

3. Open the script and set the desired date for prediction by modifying the `predicted_price` variable. For example:

```python
predicted_price = predict_price(dates, prices, 29)
```

Replace `29` with the date for which you want to predict the stock price.

4. Run the script using a Python interpreter:

```
python stock_price_prediction.py
```

The script will display a plot showing the historical data and the predictions made by the three SVR models. The predicted prices will also be printed to the console.


## Acknowledgments

- This project is inspired by the concept of using SVR for stock price prediction.
- Thanks to the open-source communities behind NumPy, scikit-learn, and Matplotlib for their valuable libraries.
```

Feel free to modify and expand this template to suit the specific details of your project. Make sure to provide clear instructions on how to use your code, prerequisites, and any other relevant information for users and potential contributors.
