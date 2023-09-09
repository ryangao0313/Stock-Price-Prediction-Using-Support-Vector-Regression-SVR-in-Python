import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


#plt.switch_backend('newbackend')  



dates = []
prices = []

def get_data(filename):
    row_count = 0
    
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # Skipping column names
        
        for row in csvFileReader:
            if row:  # Check if the row is not empty
                prices.append(float(row[1]))
                row_count += 1
                dates.append(row_count)



def predict_price(history_dates, history_prices, x):
    history_dates = np.reshape(history_dates, (len(history_dates), 1)) # Converting to a matrix of n X 1


#create 3 different models, each of them will be a type of support virtual machinec (SVM)
#A SVM is a linear separator, it takes a set of data that is already classified and try to predict
# a set of data that is not classified

#A support vector regression is a type of SVM that uses the space between data points as a margin of error and 
#predict the most likely next point in a dataset


#create models - 3 parameters - kernal is the type of svm, c is penalty parameter(error term)
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1) # Defining the support vector regression models
    
    #train models
    svr_rbf.fit(history_dates, history_prices) # Fitting the data points in the models
    svr_lin.fit(history_dates, history_prices)
    svr_poly.fit(history_dates, history_prices)


#plot
    plt.scatter(history_dates, history_prices, color='black', label='Data') # Plotting the initial datapoints 
    plt.plot(history_dates, svr_rbf.predict(history_dates), color='red', label='RBF model') # Plotting the line made by the RBF kernel
    plt.plot(history_dates, svr_lin.predict(history_dates), color='green', label='Linear model') # Plotting the line made by linear kernel
    plt.plot(history_dates, svr_poly.predict(history_dates), color='blue', label='Polynomial model') # Plotting the line made by polynomial kernel
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    x = np.array(x).reshape(-1, 1) # Reshape 'x' to a 2D array
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('aapl.csv') # Calling get_data method by passing the CSV file to it

# Predicting the price for the date 29
predicted_price = predict_price(dates, prices, 29)
print("Predicted Prices (RBF, Linear, Polynomial):", predicted_price)
