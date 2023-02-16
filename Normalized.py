import pandas as pd
from sklearn.preprocessing import MinMaxScaler

surveyData = pd.read_csv('Automobile_data.csv')
pd.options.display.max_rows = 9999

namn = input('Chose name for the csv-file: ')


scaler = MinMaxScaler()
cols_to_norm = ['wheel-base', 'length',
                'horsepower', 'average-mileage', 'price']


surveyData[cols_to_norm] = scaler.fit_transform(surveyData[cols_to_norm])

surveyData.to_csv(namn + '.csv', index=False)

print(surveyData)