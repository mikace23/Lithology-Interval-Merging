import pandas as pd

# Create the input DataFrame
data = {
    'lithology': ['Sandstone', 'Sandstone', 'Sandstone', 'Sandstone', 'Limestone', 'Shale', 'Sandstone'],
    'from': [12.20, 20.511, 35.624, 60.88, 15.44, 16.33, 10.0],
    'to': [21.0, 35.624, 60.88, 70.64, 30.1257, 19.5221, 13.0]
}
df = pd.DataFrame(data)

# Expand each interval to cover every 0.01 unit
expanded_rows = []
step = 0.01  # Define the step size for expansion
for _, row in df.iterrows():
    start = row['from']
    end = row['to']
    meter = start
    while meter < end:
        expanded_rows.append({'lithology': row['lithology'], 'meter': round(meter, 2)})
        meter += step

expanded_df = pd.DataFrame(expanded_rows)

# Sort by meter and prioritize lithology with higher ID
expanded_df = expanded_df.sort_values(by=['meter', 'lithology'], ascending=[True, False])

# Combine consecutive intervals of the same lithology
combined_intervals = []
current_lithology = expanded_df.iloc[0]['lithology']
current_from = expanded_df.iloc[0]['meter']
current_to = current_from + step

for i, row in expanded_df.iterrows():
    if row['lithology'] != current_lithology or round(row['meter'], 2) != round(current_to, 2):
        combined_intervals.append([current_lithology, current_from, round(current_to, 2)])
        current_lithology = row['lithology']
        current_from = row['meter']
    current_to = row['meter'] + step

# Append the last interval
combined_intervals.append([current_lithology, current_from, round(current_to, 2)])

# Create a DataFrame from the combined intervals
result_df = pd.DataFrame(combined_intervals, columns=['lithology', 'from', 'to'])

# Ensure 'to' values correctly represent the start of the next interval
for i in range(1, len(result_df)):
    result_df.at[i-1, 'to'] = result_df.at[i, 'from']

# Save the result to a new file
result_df.to_csv('final_output.txt', sep='\t', index=False)

# Print the result
print(result_df)
    
