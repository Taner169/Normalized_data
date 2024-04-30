Project Title: Automobile Data Normalization
This repository contains a Python script for normalizing specific numerical columns in an automobile dataset. The script utilizes Pandas for data handling and scikit-learn's MinMaxScaler for normalization, preparing the data for machine learning models that perform better with scaled input features.

Features
Data Reading: Load data from a CSV file.
Normalization: Apply Min-Max normalization to selected features to scale the data between 0 and 1.
Data Output: Save the normalized data back to a CSV file, with the user-defined filename.
How to Use
Ensure you have Python installed along with Pandas and scikit-learn.
Place your input CSV file in the same directory as the script, or modify the path in the script to match your file's location.
Run the script. It will prompt you to enter a name for the output file where the normalized data will be saved.
Check the output CSV to see the normalized values alongside other data.
Requirements
Python 3.x
Pandas
scikit-learn
Sample Output
After running the script, the normalized data will be printed to the console and saved to a CSV file. This is useful for verifying the transformation and for use in downstream machine learning applications.
