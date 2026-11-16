import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_clean_data(filename="rain.csv"):
    """Loads CSV using Pandas and handles missing or invalid readings."""
    if not os.path.exists(filename):
        print(f"Error: '{filename}' not found.")
        return pd.DataFrame(), False

    # Read CSV using Pandas
    df_raw = pd.read_csv(filename, dtype=str)
    
    # Support both header and headerless CSV inputs if needed
    if 'Month' not in df_raw.columns or 'Rainfall_mm' not in df_raw.columns:
        df_raw = pd.read_csv(filename, names=['Month', 'Rainfall_mm'], dtype=str)

    valid_rows = []
    skipped_any = False

    for idx, row in df_raw.iterrows():
        row_num = idx + 1
        month = str(row['Month']).strip()
        val_str = str(row['Rainfall_mm']).strip()

        # Check for missing or non-numeric values
        try:
            val = float(val_str)
        except ValueError:
            print(f"Row {row_num} skipped: invalid Rainfall '{val_str}'.")
            skipped_any = True
            continue

        # Check for negative rainfall
        if val < 0:
            val_disp = int(val) if val.is_integer() else val
            print(f"Row {row_num} skipped: Rainfall cannot be negative.")
            skipped_any = True
            continue

        valid_rows.append({'Month': month, 'Rainfall_mm': val})

    clean_df = pd.DataFrame(valid_rows)

    # Summary line when invalid rows were skipped (Matches Test Case 3)
    if skipped_any:
        total_valid = int(np.sum(clean_df['Rainfall_mm'])) if not clean_df.empty else 0
        print(f"Valid rows: {len(clean_df)} | Total: {total_valid} mm")

    return clean_df, skipped_any
 

def show_statistics(df):
    """Menu Option 1: Calculate stats using NumPy and detect heavy-rainfall months."""
    if df.empty:
        print("No valid data available to analyze.")
        return

    months = df['Month'].to_numpy()
    rain = df['Rainfall_mm'].to_numpy()

    # NumPy statistical calculations (np.std uses population std dev by default)
    total = np.sum(rain)
    mean = np.mean(rain)
    std_dev = np.std(rain)

    max_idx = np.argmax(rain)
    min_idx = np.argmin(rain)

    # Boolean filtering for heavy rainfall (> 200 mm)
    heavy_mask = rain > 200
    heavy_months = months[heavy_mask]

    # Output formatting for Single Row (Test Case 2) vs Multiple Rows (Test Case 1)
    if len(rain) == 1:
        print(f"Total: {int(total)} mm | Mean: {mean:.2f} | Std Dev: {std_dev:.2f}")
    else:
        print(f"Total: {int(total)} mm | Mean: {mean:.2f}")
        print(f"Max: {months[max_idx]} ({int(rain[max_idx])}) | Min: {months[min_idx]} ({int(rain[min_idx])})")
        print(f"Std Dev: {std_dev:.2f}")

    if len(heavy_months) > 0:
        print(f"Heavy rainfall months: {', '.join(heavy_months)}")
    else:
        print("No month above 200 mm")


def plot_charts(df):
    """Menu Option 2 / Helper: Plot Bar and Line charts using Matplotlib."""
    if df.empty:
        print("No valid data available to plot.")
        return

    months = df['Month'].to_numpy()
    rain = df['Rainfall_mm'].to_numpy()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Bar Chart
    ax1.bar(months, rain, color='steelblue', edgecolor='black')
    ax1.set_title('Monthly Rainfall')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Rainfall (mm)')
    ax1.axhline(np.mean(rain), color='red', linestyle='--', label=f'Mean ({np.mean(rain):.2f} mm)')
    ax1.legend()

    # 2. Line Chart
    ax2.plot(months, rain, marker='o', color='darkgreen', linestyle='-', linewidth=2)
    ax2.set_title('Rainfall Trend')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Rainfall (mm)')
    ax2.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    print("Bar chart 'Monthly Rainfall' displayed")
    plt.show()


def compare_with_average_and_plot(df):
    """Menu Option 3: Compare with average using boolean filtering and display plot."""
    if df.empty:
        print("No valid data available.")
        return

    months = df['Month'].to_numpy()
    rain = df['Rainfall_mm'].to_numpy()
    mean = np.mean(rain)

    # Boolean filtering for Above and Below average
    above_mask = rain > mean
    below_mask = rain < mean

    above_items = [f"{m} ({int(r)})" for m, r in zip(months[above_mask], rain[above_mask])]
    below_items = [f"{m} ({int(r)})" for m, r in zip(months[below_mask], rain[below_mask])]

    print(f"Above average ({mean:.2f}): {' | '.join(above_items) if above_items else 'None'}")
    print(f"Below average: {' | '.join(below_items) if below_items else 'None'}")

    # Plot charts
    plot_charts(df)


def main():
    filename = input("Enter CSV filename (press Enter for 'rain.csv'): ").strip()
    if not filename:
        filename = "rain.csv"

    df, skipped_any = load_and_clean_data(filename)
    if df.empty:
        return

    print("\n--- Rainfall Data Analyzer Menu ---")
    print("1. Statistics (Total, Mean, Max, Min, Std Dev, Heavy Rainfall)")
    print("2. Plot Rainfall Trend (Bar & Line Charts)")
    print("3. Compare with Average and Plot")

    choice = input("Select menu option (1/2/3): ").strip()
    print()

    if choice == '1':
        show_statistics(df)
    elif choice == '2':
        plot_charts(df)
    elif choice == '3':
        compare_with_average_and_plot(df)
    else:
        print("Invalid menu option selected.")


if __name__ == "__main__":
    main()