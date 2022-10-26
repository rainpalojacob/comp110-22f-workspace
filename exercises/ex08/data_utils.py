"""Dictionary related utility functions."""

__author__ = "730569341"

# Define your functions below

"""0.0 Read an entire CSV into a list of rows."""
from data_utils import read_csv_rows
data_rows: list[dict[str, str]] = read_csv_rows(DATA_FILE_PATH)

if len(data_rows) == 0:
    print("Go implement read_csv_rows in data_utils.py")
    print("Be sure to save your work before re-evaluating this cell!")
else:
    print(f"Data File Read: {DATA_FILE_PATH}")
    print(f"{len(data_rows)} rows")
    print(f"{len(data_rows[0].keys())} columns")
    print(f"Columns names: {data_rows[0].keys()}")

"""0.1 Produce a list of values into a single column."""

from data_utils import column_values

subject_age: list[str] = column_values(data_rows, "subject_age")

if len(subject_age) == 0:
    print("Complete your implementation of column_values in data_utils.py")
    print("Be sure to follow the guidelines above and save your work before re-evaluating!")
else:
    print(f"Column 'subject_age' has {len(subject_age)} values.")
    print("The first five values are:")
    for i in range(5):
        print(subject_age[i])

"""0.2 Transform a table from a list of rows to a dictionary of column."""
from data_utils import columnar

data_cols: dict[str, list[str]] = columnar(data_rows)

if len(data_cols.keys()) == 0:
    print("Complete your implementation of columnar in data_utils.py")
    print("Be sure to follow the guidelines above and save your work before re-evaluating!")
else:
    print(f"{len(data_cols.keys())} columns")
    print(f"{len(data_cols['subject_age'])} rows")
    print(f"Columns names: {data_cols.keys()}")

"""Part 1 Narrowing down a data table."""
from tabulate import tabulate 

"""1.0 Produce a new column table with only first number of rows of data for each column."""

"""1.2 Produce a new column-based table with two column-based tables combined."""

"""2.0 Produce a dictionary of a key and value of the number of times values appeared."""


"""Charting with matplotlib."""
from matplotlib import pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
fig.suptitle("Traffic Stops in Durham - March 21st through 27th - 2015")


axes[0].set_title("By Race")
axes[0].bar(race_counts.keys(), race_counts.values())
axes[0].tick_params(axis='x', labelrotation = 45)

axes[1].set_title("By Sex")
axes[1].bar(sex_counts.keys(), sex_counts.values())