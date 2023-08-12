import matplotlib.pyplot as plt
import july
from datetime import datetime
import csv
dates = []
consomation = []
with open('courbes_de_charge_microgrid.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)  # Skip the header line
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        consomation_value = float(row[1])
        dates.append(date)
        consomation.append(consomation_value)
# Create a dictionary to aggregate the data for each day
daily_data = {}
# Iterate over the timestamps and data
for timestamp, value in zip(dates, consomation):
    # Extract the date from the timestamp
    date = timestamp.date()
    # Check if the date is already in the dictionary
    if date in daily_data:
        # If the date exists, add the value to the existing data
        daily_data[date] += value
    else:
        # If the date does not exist, create a new entry
        daily_data[date] = value
# Extract the resized arrays
resized_dates = list(daily_data.keys())
resized_data = list(daily_data.values())
resized_dates, resized_data = zip(*sorted(zip(resized_dates, resized_data)))
july.heatmap(resized_dates, resized_data,
        title='Consumption Activity KW/h',
        cmap="github", colorbar=True)
plt.show()
