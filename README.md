# Rainfall Data Analyzer (PS No. 23)

## Problem Statement
Analyse monthly rainfall data from a CSV file using NumPy and Pandas to find total and average rainfall, the wettest and driest months, heavy-rainfall months (> 200 mm), and plot the rainfall trend using Matplotlib.

## Features Implemented
1. **CSV Data Loading & Cleaning (Pandas):** Reads `rain.csv` and automatically skips missing, non-numeric, or negative rainfall entries with clear row-level error messages.
2. **Statistical Analysis (NumPy):** Computes Total, Mean, Maximum, Minimum, and Population Standard Deviation (`np.std`).
3. **Boolean Filtering:** Identifies heavy-rainfall months (> 200 mm) as well as months above and below the average rainfall.
4. **Data Visualization (Matplotlib):** Generates both a Bar Chart (`Monthly Rainfall`) and a Line Chart (`Rainfall Trend`) with proper titles and axis labels.

## Prerequisites
Install the required libraries before running the program:
```bash
pip install numpy pandas matplotlib
