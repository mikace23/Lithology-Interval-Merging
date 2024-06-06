# Lithology Interval Merging

## Overview

This repository contains a Python script to merge contiguous intervals of the same lithology, ensuring the data integrity and maintaining the ranking of lithology based on input.

## Problem Description

Given a dataset with lithology intervals and their corresponding depth ranges, the goal is to merge overlapping intervals of the same lithology and output a sorted, formatted result.

## Solution Approach

1. **Data Expansion**: Expand each interval to cover every 0.01 unit within its range.
2. **Sorting**: Sort the expanded data by meter and lithology.
3. **Interval Merging**: Merge contiguous intervals of the same lithology.

## Example

Input:
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

Desired Output:
```
| lithology | from  | to    |
|-----------|-------|-------|
| Sandstone | 10.00 | 15.44 |
| Limestone | 15.44 | 16.33 |
| Shale     | 16.33 | 19.52 |
| Limestone | 19.52 | 30.13 |
| Sandstone | 30.13 | 70.64 |
```

## Usage

To run the script, make sure you have `pandas` installed. You can install it using:

```
pip install pandas
```

Run the script using:

```
python merge_intervals.py
```

The output will be saved in `final_output.txt`.

## Visualization

![Interval Merging Visualization](./visualization.png)

## License

This project is licensed under the MIT License.
```
