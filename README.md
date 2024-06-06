# Lithology Interval Merging

## Problematic

Given a dataset comprising lithology intervals with corresponding depth ranges, our goal is to merge contiguous intervals of the same lithology while ensuring the integrity of the data and maintaining the ranking of lithology based on input. This problem typically arises in geological interpretations where lithology data from various depths needs to be consolidated for accurate analysis.

## Example

### Input:
```
| lithology | from   | to       |
|-----------|--------|----------|
| Sandstone | 12.20  | 21.00    |
| Sandstone | 20.511 | 35.624   |
| Sandstone | 35.624 | 60.88    |
| Sandstone | 60.88  | 70.64    |
| Limestone | 15.44  | 30.1257  |
| Shale     | 16.33  | 19.5221  |
| Sandstone | 10.00  | 13.00    |
```

### Desired Output:
```
| lithology | from  | to    |
|-----------|-------|-------|
| Sandstone | 10.00 | 15.44 |
| Limestone | 15.44 | 16.33 |
| Shale     | 16.33 | 19.52 |
| Limestone | 19.52 | 30.13 |
| Sandstone | 30.13 | 70.64 |
```

## Solution Method

1. **Data Expansion**: Expand each interval to cover every 0.01 unit within its range.
2. **Sorting**: Sort the expanded data by meter and lithology.
3. **Interval Merging**: Merge contiguous intervals of the same lithology.

## Python Program

Here's the Python script that accomplishes this:

```python
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
```

## Visual Illustration

![lithology_intervals](https://github.com/mikace23/Lithology-Interval-Merging/assets/128716197/885b6345-0eb8-43c5-99e1-be2ed76f9618)

## Final Notes

The Python script provided will expand, sort, and merge the lithology intervals effectively. The output will be a consolidated set of intervals with correct depth ranges and lithology rankings. The visual illustration `lithology_intervals.png` is included to facilitate understanding of the repository.

## License

This project is licensed under the MIT License.
```

### Steps to Add the Image from Smartphone
Here’s a quick guide on how to add the `visualization.png` image from your smartphone:

1. **Open the GitHub App or Mobile Browser:**
   - Use the GitHub app or go to [GitHub](https://github.com) on your mobile browser.

2. **Navigate to Your Repository:**
   - Go to the repository where you want to add the image.

3. **Add the Image:**
   - Tap on "Add file" and then "Upload files".
   - Select the image file (`visualization.png`) from your phone’s storage.

4. **Commit the Changes:**
   - Provide a commit message such as "Add visualization.png for interval merging illustration".
   - Tap "Commit changes".

5. **Update the README.md:**
   - Open the README.md file and tap the edit button.
   - Insert the image link:
     ```markdown
     ![lithology_intervals](https://github.com/mikace23/Lithology-Interval-Merging/assets/128716197/885b6345-0eb8-43c5-99e1-be2ed76f9618)
     ```
   - Save the changes by committing with a suitable message, e.g., "Update README to include visualization image".

By following these steps, your GitHub repository will be properly set up with the image correctly referenced in the README file.
